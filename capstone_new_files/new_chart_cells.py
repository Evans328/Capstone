# New chart cells for gpu_cpu_analysis.ipynb
# Each "# %%" block is one cell: paste it into a new code cell, or open this file in VS Code and run the blocks as-is.
# They read these files from the same folder: hardware_data.csv, gpu_metadata.csv, gpu_price_history.csv,
# GPU_benchmarks_v7.csv, budget_tier_builds.csv

# %% setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

AMD, NVIDIA = '#D9692F', '#085041'

# %% scatter
# Price against performance for my 16 cards
hw = pd.read_csv('hardware_data.csv', keep_default_na=False)
hw['short'] = hw['Full_Model_Name'].str.replace('GeForce ', '').str.replace('Radeon ', '')
colors = {'AMD': AMD, 'Nvidia': NVIDIA}
offset = {'RX 7600': (9, -4), 'RTX 4060': (9, -14), 'RTX 5060': (9, 5), 'RTX 4060 Ti': (9, 5),
          'RX 9060 XT': (9, -4), 'RX 7700 XT': (9, -4), 'RX 7800 XT': (9, -4), 'RTX 4070': (-64, 8),
          'RX 9070': (9, -14), 'RX 9070 XT': (9, 3), 'RX 7900 XT': (-82, 6), 'RTX 4070 Ti': (-84, 4),
          'RTX 5070': (9, -4), 'RX 7900 XTX': (9, -4), 'RTX 5070 Ti': (9, 4), 'RTX 5080': (-68, 6)}

plt.figure(figsize=(10, 6.4))
for brand, d in hw.groupby('Brand'):
    plt.scatter(d['Current_Street_Price'], d['G3D_Mark'], s=130,
                color=colors[brand], label=brand, zorder=3)
for _, r in hw.iterrows():
    plt.annotate(r['short'], (r['Current_Street_Price'], r['G3D_Mark']),
                 textcoords='offset points', xytext=offset[r['short']], fontsize=11)
plt.xlabel('Street price (USD, Sept 2026)')
plt.ylabel('G3D Mark (higher is faster)')
plt.legend(frameon=False, loc='lower right')
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()

# %% pairs
# AMD price per point against its Nvidia pair (the pairing is my own judgment, by tier and era)
hw = pd.read_csv('hardware_data.csv', keep_default_na=False)
hw['ppm'] = hw['Current_Street_Price'] / hw['G3D_Mark']
ppm = hw.set_index('Full_Model_Name')['ppm']

pairs = [('GeForce RTX 5080', 'Radeon RX 7900 XTX'),
         ('GeForce RTX 5070 Ti', 'Radeon RX 9070 XT'),
         ('GeForce RTX 5070', 'Radeon RX 9070'),
         ('GeForce RTX 4070 Ti', 'Radeon RX 7900 XT'),
         ('GeForce RTX 4070', 'Radeon RX 7800 XT'),
         ('GeForce RTX 4060 Ti', 'Radeon RX 7700 XT'),
         ('GeForce RTX 5060', 'Radeon RX 9060 XT'),
         ('GeForce RTX 4060', 'Radeon RX 7600')]   # (Nvidia, AMD)

diff = [(ppm[amd] / ppm[nv] - 1) * 100 for nv, amd in pairs]
labels = [f"{nv.replace('GeForce ', '')}  vs  {amd.replace('Radeon ', '')}" for nv, amd in pairs]

plt.figure(figsize=(10, 6.4))
bars = plt.barh(labels[::-1], diff[::-1],
                color=[AMD if d < 0 else NVIDIA for d in diff[::-1]])
plt.axvline(0, color='gray', linewidth=1)
for bar, d in zip(bars, diff[::-1]):
    plt.text(d + (2 if d >= 0 else -2), bar.get_y() + bar.get_height() / 2, f'{d:+.0f}%',
             va='center', ha='left' if d >= 0 else 'right')
plt.xlim(-34, 78)
plt.xlabel('AMD price per point vs its Nvidia pair (negative: AMD is cheaper per point)')
plt.tight_layout()
plt.show()

# %% used
# How far below the new price the used price sits, by price tier (December 2024)
meta = pd.read_csv('gpu_metadata.csv')
hist = pd.read_csv('gpu_price_history.csv')
meta['brand'] = np.where(meta['Name'].str.startswith('GeForce'), 'NVIDIA', 'AMD')
h = hist.merge(meta[['Name', 'brand']], on='Name')
h['dt'] = pd.to_datetime(h['Date'], format='%d-%m-%y')
h = h.replace({'Retail Price': 0, 'Used Price': 0}, np.nan)      # 0 means missing

dec = h[h['dt'] == '2024-12-01'].copy()
dec['saving'] = ((dec['Retail Price'] - dec['Used Price']) * 100
                 / dec['Retail Price'])
dec['tier'] = pd.cut(dec['Retail Price'], [0, 299.99, 599.99, 999.99, 1e9],
                     labels=['Under $300', '$300-$599', '$600-$999', '$1000+'])
g = dec.groupby(['tier', 'brand'], observed=False)['saving'].agg(['mean', 'count']).unstack()

x, w = np.arange(4), 0.36
plt.figure(figsize=(10, 6.2))
for shift, brand, col in ((-w / 2, 'AMD', AMD), (w / 2, 'NVIDIA', NVIDIA)):
    bars = plt.bar(x + shift, g['mean'][brand], w, color=col, label=brand)
    for bar, val, n in zip(bars, g['mean'][brand], g['count'][brand]):
        plt.text(bar.get_x() + bar.get_width() / 2, val + 1.5, f'{val:.0f}%', ha='center', fontweight='bold')
        plt.text(bar.get_x() + bar.get_width() / 2, 2, f'n={int(n)}', ha='center', color='white')
plt.xticks(x, g.index)
plt.ylabel('Used price discount below new price (%), Dec 2024')
plt.ylim(0, 95)
plt.legend(frameon=False, loc='upper left')
plt.tight_layout()
plt.show()

# %% efficiency
# 3DMark points per watt in four same-generation pairs
meta = pd.read_csv('gpu_metadata.csv')
meta['watts'] = meta['Wattage'].str.replace('W', '').astype(int)
meta['pts_per_watt'] = (meta['3DMARK']
                        / meta['watts'])
eff = meta.set_index('Name')['pts_per_watt']

pairs = [('GeForce RTX 4060', 'Radeon RX 7600'),
         ('GeForce RTX 4060 Ti', 'Radeon RX 7700 XT'),
         ('GeForce RTX 4070', 'Radeon RX 7800 XT'),
         ('GeForce RTX 4070 Ti', 'Radeon RX 7900 XT')]   # (Nvidia, AMD)
nv = [eff[a] for a, b in pairs]
amd = [eff[b] for a, b in pairs]

x, w = np.arange(len(pairs)), 0.36
plt.figure(figsize=(10, 6.2))
for shift, vals, col, lab in ((-w / 2, amd, AMD, 'AMD'), (w / 2, nv, NVIDIA, 'Nvidia')):
    bars = plt.bar(x + shift, vals, w, color=col, label=lab)
    for bar, v in zip(bars, vals):
        plt.text(bar.get_x() + bar.get_width() / 2, v + 1.2, f'{v:.0f}', ha='center', fontweight='bold')
plt.xticks(x, [f"{a.replace('GeForce ', '')}\nvs {b.replace('Radeon ', '')}" for a, b in pairs])
plt.ylabel('3DMark points per watt (higher is more efficient)')
plt.ylim(0, 108)
plt.legend(frameon=False, loc='upper right')
plt.tight_layout()
plt.show()

# %% price_time
# Retail price over time for six mid-range and entry cards
meta = pd.read_csv('gpu_metadata.csv')
hist = pd.read_csv('gpu_price_history.csv')
h = hist.copy()
h['dt'] = pd.to_datetime(h['Date'], format='%d-%m-%y')
h = h.replace({'Retail Price': 0, 'Used Price': 0}, np.nan)

cards = {'GeForce RTX 4070': (NVIDIA, '-'), 'GeForce RTX 4060 Ti': (NVIDIA, '--'), 'GeForce RTX 4060': (NVIDIA, ':'),
         'Radeon RX 7800 XT': (AMD, '-'), 'Radeon RX 7700 XT': (AMD, '--'), 'Radeon RX 7600': (AMD, ':')}

nudge = {'Radeon RX 7700 XT': 9, 'GeForce RTX 4060 Ti': -9}   # keeps the two end labels near $400 apart

plt.figure(figsize=(10, 6.2))
for name, (color, style) in cards.items():
    s = (h[h['Name'] == name]
         .dropna(subset=['Retail Price'])
         .sort_values('dt'))
    plt.plot(s['dt'], s['Retail Price'],
             color=color, linestyle=style, linewidth=2.6)
    plt.text(s['dt'].iloc[-1] + pd.Timedelta(days=12), s['Retail Price'].iloc[-1] + nudge.get(name, 0),
             name.replace('GeForce ', '').replace('Radeon ', ''), color=color, va='center')
plt.xlim(pd.Timestamp('2023-03-01'), pd.Timestamp('2025-04-15'))
plt.ylabel('Retail price (USD)')
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()

# %% median_year
# Median price per G3D point by year, from the benchmark file. Years where either brand has fewer than 5 priced cards are left out.
raw = pd.read_csv('GPU_benchmarks_v7.csv')
cl = raw[raw['brand'].isin(['NVIDIA', 'AMD']) & raw['price'].notna() & (raw['price'] <= 3000)].copy()
cl['ppm'] = cl['price'] / cl['G3Dmark']
med = (cl.groupby(['testDate', 'brand'])
         ['ppm'].median().unstack())
n = cl.groupby(['testDate', 'brand']).size().unstack()
keep = (n >= 5).all(axis=1)                       # years where both brands have 5+ priced cards
plot = med.reindex(range(2009, 2022))
plot.loc[~keep.reindex(plot.index)] = np.nan      # 2020 has only 4 Nvidia cards, so it becomes a gap

ax = plot.plot(logy=True, marker='o', linewidth=2.6, color=[AMD, NVIDIA], figsize=(10, 6.2))
ax.axvspan(2019.5, 2020.5, color='#d3d1c7', alpha=0.5)
ax.text(2020, plot.max().max() * 0.8, 'too few\ncards', ha='center', va='top', fontsize=11, color='#5f5e5a')
ax.set_xticks(list(plot.index))
ax.set_xlabel('Test year (2020 and 2022 are left out: fewer than 5 priced cards for one brand)')
ax.set_ylabel('Median price per G3D point (USD, log scale)')
ax.grid(alpha=0.2, which='both')
plt.legend(['AMD', 'Nvidia'], frameon=False)
plt.tight_layout()
plt.show()

# %% budget
# GPU score you can reach at each budget, two strategies
b = pd.read_csv('budget_tier_builds.csv')
p = b.pivot(index='Budget_Target',
            columns='Strategy',
            values='GPU_G3D_Mark')
order = ['$800', '$1,200', '$1,600', '$2,000', '$2,300', 'My build']

ax = p.loc[order].plot(kind='bar', color=['#1F5F8B', '#B4B2A9'], figsize=(10, 6.2), rot=0)
ax.set_xlabel(r'CPU + GPU budget (My build = \$1,148.50 inside a \$2,200 PC)')   # \$ stops matplotlib reading $...$ as math
ax.set_ylabel('GPU score (G3D Mark)')
ax.legend(['Balanced: stronger CPU first', 'Max-GPU: cheapest CPU, biggest GPU'], frameon=False, loc='lower right')
plt.tight_layout()
plt.show()

# %% wider_field
# All 48 cards in the price history (December 2024): price against 3DMark score, my shortlist outlined
meta = pd.read_csv('gpu_metadata.csv')
hist = pd.read_csv('gpu_price_history.csv')
meta['brand'] = np.where(meta['Name'].str.startswith('GeForce'), 'NVIDIA', 'AMD')
h = hist.replace({'Retail Price': 0, 'Used Price': 0}, np.nan)
h['dt'] = pd.to_datetime(h['Date'], format='%d-%m-%y')
dec = h[h['dt'] == '2024-12-01'].merge(meta[['Name', 'brand', '3DMARK']], on='Name')

shortlist = ['GeForce RTX 4060', 'GeForce RTX 4060 Ti', 'GeForce RTX 4070', 'GeForce RTX 4070 Ti',
             'Radeon RX 7600', 'Radeon RX 7700 XT', 'Radeon RX 7800 XT', 'Radeon RX 7900 XT', 'Radeon RX 7900 XTX']
dec['on_list'] = dec['Name'].isin(shortlist)
colors = {'AMD': AMD, 'NVIDIA': NVIDIA}

plt.figure(figsize=(10, 6.4))
for brand, d in dec.groupby('brand'):
    others, mine = d[~d['on_list']], d[d['on_list']]
    plt.scatter(others['Retail Price'], others['3DMARK'], s=50, color=colors[brand], alpha=0.45)
    plt.scatter(mine['Retail Price'], mine['3DMARK'], s=150, color=colors[brand],
                edgecolor='black', linewidth=1.6, label=f'{brand}: shortlist outlined, others faded')

named = {'GeForce RTX 4090': (-84, -4), 'GeForce RTX 4080 SUPER': (9, -4), 'Radeon RX 6900 XT': (9, 4)}   # only the clear outliers
for name, shift in named.items():
    r = dec[dec['Name'] == name].iloc[0]
    plt.annotate(name.replace('GeForce ', '').replace('Radeon ', ''), (r['Retail Price'], r['3DMARK']),
                 textcoords='offset points', xytext=shift, fontsize=11)
plt.xlabel('Retail price (USD), December 2024')
plt.ylabel('3DMark score (higher is faster)')
plt.legend(frameon=False, loc='lower right')
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()
