# Web scraping cells: check my MSRP column against Wikipedia's launch-price tables.
# Paste each "# %%" block into a notebook cell (or open this file in VS Code and run the blocks). Needs an internet connection.
# If you see "No module named lxml", run:  %pip install lxml
# It uses Wikipedia's API, which allows this, with a polite User-Agent and one request per second.
# I did NOT scrape store sites: they usually forbid it and block bots.

# %% scrape
import re
import time
import requests
import pandas as pd
from io import StringIO

API = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'gpu-capstone/1.0 (student project; contact: [blakeevans200@outlook.com])'}

def get_tables(title):
    """Download one Wikipedia article through the API and return its HTML tables as DataFrames."""
    r = requests.get(API, headers=HEADERS, timeout=30,
                     params={'action': 'parse', 'page': title, 'prop': 'text',
                             'format': 'json', 'formatversion': 2, 'redirects': 1})
    r.raise_for_status()
    html = r.json()['parse']['text']
    return pd.read_html(StringIO(html))

def clean(x):
    x = re.sub(r'\[.*?\]', '', str(x))                      # drop footnote marks like [27]
    return re.sub(r'\s+', ' ', x).strip()                   # tidy spaces, including hidden non-breaking ones

def to_prices(x):
    """Every price in a cell, e.g. '$379 / $429' gives [379.0, 429.0]."""
    return [float(n.replace(',', '')) for n in re.findall(r'\d{1,3}(?:,\d{3})+|\d{3,}', clean(x))]

def model_key(text):
    """'GeForce RTX 4070 Ti' and '4070 Ti' both become '4070ti'. Laptop parts are skipped."""
    t = clean(text)
    if re.search(r'laptop|mobile|notebook|max-q', t, re.I):
        return None
    m = re.search(r'(\d{4})\s*(Ti\s*Super|Super|Ti|XTX|XT|GRE)?(?![A-Za-z0-9])', t, re.I)
    if not m:
        return None
    return m.group(1) + (re.sub(r'\s+', '', m.group(2)).lower() if m.group(2) else '')

def prices_from_tables(tables):
    """Wikipedia uses two layouts: one row per model, or one column per model. Returns {model key: [prices]}."""
    found = {}
    def add(label, prices):
        key = model_key(label)
        if key and prices:
            found.setdefault(key, []).extend(prices)
    for t in tables:
        t = t.copy()
        t.columns = [' '.join(dict.fromkeys(clean(p) for p in c)) if isinstance(c, tuple) else clean(c) for c in t.columns]
        money = [j for j, c in enumerate(t.columns) if re.search(r'MSRP|price', c, re.I)]
        if money:                                           # layout 1: one row per model
            for _, row in t.iterrows():
                for j in money:
                    add(row.iloc[0], to_prices(row.iloc[j]))
        else:                                               # layout 2: one column per model
            labels = t.iloc[:, 0].astype(str)
            hit = labels[labels.str.contains('MSRP|price', case=False, regex=True)]
            if len(hit):
                row = t.loc[hit.index[0]]
                for j in range(1, len(t.columns)):
                    add(t.columns[j], to_prices(row.iloc[j]))
    return found

# %% compare
hw = pd.read_csv('hardware_data.csv', keep_default_na=False)
hw['key'] = hw['Full_Model_Name'].map(model_key)

pages = ['GeForce RTX 50 series', 'GeForce 40 series', 'Radeon RX 7000 series', 'Radeon RX 9000 series']
scraped = {}
for title in pages:
    found = prices_from_tables(get_tables(title))
    print(f'{title}: {len(found)} models with a launch price')
    for key, prices in found.items():
        scraped.setdefault(key, []).extend(prices)
    time.sleep(1)                                           # be polite: one request per second

def status(key, msrp):
    prices = set(scraped.get(key, []))
    return 'not found' if not prices else ('match' if msrp in prices else 'differs')

check = hw[['Full_Model_Name', 'key', 'MSRP_Price']].copy()
check['wikipedia_msrp'] = check['key'].map(lambda k: ' / '.join(f'{p:g}' for p in sorted(set(scraped.get(k, [])))) or 'not found')
check['status'] = [status(k, m) for k, m in zip(check['key'], check['MSRP_Price'])]
print(f"{(check['status'] == 'match').sum()} of {len(check)} launch prices match")
check[check['status'] != 'match']

# %%
