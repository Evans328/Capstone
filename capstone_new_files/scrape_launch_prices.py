# Web scraping cells: check my MSRP column against Wikipedia's launch-price tables.
# Paste each "# %%" block into a notebook cell (or open this file in VS Code and run the blocks). Needs an internet connection.
# It uses Wikipedia's API, which allows this, with a polite User-Agent and one request per second.
# I did NOT scrape store sites: they usually forbid it and block bots.

# %% scrape
import re
import time
import requests
import pandas as pd
from io import StringIO

API = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'gpu-capstone/1.0 (student project; contact: [your email])'}

def get_tables(title):
    """Download one Wikipedia article through the API and return its HTML tables as DataFrames."""
    r = requests.get(API, headers=HEADERS, timeout=30,
                     params={'action': 'parse', 'page': title, 'prop': 'text',
                             'format': 'json', 'formatversion': 2, 'redirects': 1})
    r.raise_for_status()
    html = r.json()['parse']['text']
    return pd.read_html(StringIO(html))

def clean(x):
    return re.sub(r'\[.*?\]', '', str(x)).strip()          # drop footnote marks like [27]

def to_price(x):
    m = re.search(r'([\d,]+)', clean(x))
    return float(m.group(1).replace(',', '')) if m else None

def prices_from_tables(tables, prefix):
    """Wikipedia uses two layouts: one row per model, or one column per model."""
    found = {}
    for t in tables:
        t = t.copy()
        t.columns = [' '.join(clean(p) for p in c) if isinstance(c, tuple) else clean(c) for c in t.columns]
        money = [c for c in t.columns if re.search(r'MSRP|launch price', c, re.I)]
        if money:                                          # layout 1: one row per model
            for _, row in t.iterrows():
                found.setdefault(clean(row.iloc[0]), to_price(row[money[0]]))
        else:                                              # layout 2: one column per model
            labels = t.iloc[:, 0].astype(str)
            hit = labels[labels.str.contains('MSRP|launch price', case=False, regex=True)]
            if len(hit):
                row = t.loc[hit.index[0]]
                for col in t.columns[1:]:
                    found.setdefault(f'{prefix} {clean(col)}', to_price(row[col]))
    return found

# %% compare
hw = pd.read_csv('hardware_data.csv', keep_default_na=False)
short = lambda name: re.sub(r'^(GeForce|Radeon)\s+', '', clean(name))
hw['key'] = hw['Full_Model_Name'].map(short)

pages = {'GeForce RTX 50 series': 'RTX', 'GeForce 40 series': 'RTX',
         'Radeon RX 7000 series': 'RX', 'Radeon RX 9000 series': 'RX'}
scraped = {}
for title, prefix in pages.items():
    for name, price in prices_from_tables(get_tables(title), prefix).items():
        scraped.setdefault(short(name), price)
    time.sleep(1)                                          # be polite: one request per second

check = hw[['Full_Model_Name', 'key', 'MSRP_Price']].copy()
check['wikipedia_msrp'] = check['key'].map(scraped)
check['match'] = check['MSRP_Price'] == check['wikipedia_msrp']
print(f"{check['match'].sum()} of {len(check)} launch prices match")
check[~check['match']]
