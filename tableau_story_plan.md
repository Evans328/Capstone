# Tableau story plan: Price vs. Performance, choosing the best CPU and GPU for my budget

This turns the 68-slide deck into a Tableau story with 25 story points. You do not need all 25: for 15 minutes, keep about 20 and cut the weakest. Tableau has no speaker notes, so keep `presentation_script.md` open on a second screen.

## Set up once

**Data sources** (Data > New Data Source > Text file, one per file; they can all live in one workbook):

| File | Used for |
|---|---|
| gpu_tableau_ready.csv | my own 16 cards (tier, premium, VRAM per $100 already calculated). **Re-download: the premium column was corrected for the RTX 4070.** |
| gpu_price_history_tableau.csv | the Kaggle price history (your existing data source) |
| tableau_funnel.csv, tableau_pairs.csv, tableau_swap_test.csv, tableau_median_by_year.csv | small files made for specific charts |
| synthetic_vs_real_gap.csv, cpu_data_clean.csv | your gap file and the clean CPU table |

**Rules that prevent wrong charts:**

- Tableau defaults to **Sum**. For any per-card or per-month value (Price_per_Mark, VRAM per $100, retail_price, used_price, threedmark, watts, G3D_Mark), right-click the pill, choose Measure, then **Average**. Sum adds up every month and distorts the comparison.
- Colors: AMD **#D9692F**, Nvidia **#085041**. Set them once (click the Brand legend, Edit Colors). The Kaggle file spells the brands "AMD" and "NVIDIA".
- Make every dashboard the same fixed size (for example 1280 x 720) and set the story size to match, so nothing shifts between points.
- Native Tableau charts earn more credit than pasted pictures. Use the images in `tableau_story_images.zip` only where a point says Image or as a fallback.

## The story points

### 1. Title

**Deck slides:** 1, 2

**Text on the dashboard:**

- Price vs. Performance: Choosing the Best CPU and GPU for My Budget
- [Your name] | Savvy Coders Data Analytics Capstone
- The question: which CPU and GPU give me the most for my budget, and how do AMD and Nvidia compare along the way?
- I will finish with what I chose, and why.

**Build:** Text objects only. Make the title large (36 pt or more).

### 2. Agile

**Deck slides:** 3, 4

**Text on the dashboard:**

- My role: [Scrum Master / Product Owner / Developer] and what it involved
- Jira: [backlog, sprints, user stories, story points]
- Example user story: As a budget-conscious PC builder, I want to compare GPU value by price tier, so I can pick the best card for my budget.
- Ceremonies: [standups, planning, review and grooming, retrospective]. ICAgile: [status]

**Build:** Text objects plus an Image object for your Jira screenshot. Only list what you really did.

**You supply:** Your Jira screenshot

### 3. Hypothesis and approach

**Deck slides:** 5

**Text on the dashboard:**

- Hypothesis: with a fixed budget, the card with the biggest name is not automatically the best buy, and AMD may offer comparable real-world performance for less money.
- 1. Collect: two public Kaggle datasets for history, plus my own data for the current generation
- 2. Clean and join: SQL for cleaning and joins, Python and Excel to cross-check
- 3. Compare: value per tier, memory per dollar, price against launch price

**Build:** Text objects only. Three short boxes side by side make the approach easy to read.

### 4. What the numbers mean

**Deck slides:** 6, 7, 8, 10

**Text on the dashboard:**

- G3D Mark: PassMark's graphics score, averaged from thousands of test runs. Higher is faster. A point has no unit and is not frames per second.
- 3DMark: a different benchmark, used in the price-history file. Never mix it with G3D Mark.
- Price per point = price / score. RX 9070 XT: $799.50 / 27,183 = $0.0294, about $29 per 1,000 points.
- VRAM: the card's own memory. TDP: rated watts. MSRP: launch price. Street price: what stores charge now.

**Build:** NATIVE: a bar chart of four cards to show the scale. Data: gpu_tableau_ready.csv. Rows: Full_Model_Name (filter to RX 7600, RTX 4060, RX 9070 XT, RTX 5080). Columns: AVG(G3D_Mark). Color: Brand. Put it beside the text.

**You supply:** chart built in Tableau

### 5. Why VRAM matters

**Deck slides:** 9

**Text on the dashboard:**

- VRAM is the card's own memory. When it runs short, the card borrows slower system memory, which can cause stutter or lower texture quality.
- Tom's Hardware tested the RTX 5060 Ti with 8GB and 16GB: about 5% slower with 8GB in 15 games without ray tracing, about 26% slower in 6 ray-traced games at 1080p ultra.
- Results vary by game. More memory is a cheap way to make a card last longer.
- [Cite Tom's Hardware]

**Build:** Two big-number text objects (5% and 26%) plus a short paragraph.

### 6. Datasets and what was missing

**Deck slides:** 12, 13, 14, 15, 22, 23

**Text on the dashboard:**

- Main file: 2,317 rows, GPU prices and scores, 2009 to 2022 (Kaggle). Price history: 1,087 rows, Nov 2022 to Dec 2024 (Kaggle). My own file: 16 current cards, Sept 2026 prices.
- Missing: 76% of prices in the main file; no AMD consumer cards in one public dataset; public files stop in 2022 and 2024; three current cards in no file.
- Distorted: zeros standing in for missing prices; two value figures I entered wrongly; SQL imports that lost decimals and 8 rows; 7 workstation cards over $3,000.

**Build:** Text objects. A two-column layout (Missing | Distorted) reads well.

### 7. Cleaning funnel

**Deck slides:** 21, 24, 25

**Text on the dashboard:**

- 2,317 raw rows, 1,926 NVIDIA or AMD, 513 with a price, 506 after removing 7 outliers.
- 76% of the raw rows had no price. Cleaned in SQL; cross-checked in Python and Excel.

**Build:** NATIVE funnel. Data: tableau_funnel.csv. Rows: Stage. Columns: SUM(Rows). Sort Stage by name (the numbers in the names keep the order). Label the bars. Beside it, add your before-and-after screenshots from DB Browser.

**You supply:** Your DB Browser before/after screenshots

### 8. Same question, three tools

**Deck slides:** 27, 28

**Text on the dashboard:**

- One question, three tools: average price per point by tier and brand.
- Python: one groupby line. SQL: a CASE statement for the tier, then GROUP BY. Excel: a formula column and a PivotTable.
- All three agree. Budget 0.0157 vs 0.0152. Mid-range 0.0234 vs 0.0219. High-end 0.0308 vs 0.0350 (AMD vs Nvidia).

**Build:** Three Image objects: screenshots of your notebook cell, your SQL query with results, and your Excel formula bar with the PivotTable. Add the three results as a text object.

**You supply:** Your Python, SQL and Excel screenshots

### 9. Web scraping

**Deck slides:** 29

**Text on the dashboard:**

- I scraped Wikipedia's launch-price tables through its API and compared them with my MSRP column. I did not scrape store sites.
- 15 of 16 launch prices matched. The RTX 4070 launched at $599; my file had $549, the price after NVIDIA's cut.
- Fixing it moved the RTX 4070 from +7.5% to -1.5% against launch price. The 2025 to 2026 results did not change.

**Build:** Image object: a screenshot of the scraper code and its output from your notebook (run scrape_launch_prices.py first). Text objects for the three lines.

**You supply:** Your scraper screenshot

### 10. Value by price tier

**Deck slides:** 30

**Text on the dashboard:**

- Lower is better. AMD averages 0.0243 and Nvidia 0.0259 per point overall.
- Budget: 0.0157 vs 0.0152. Mid-range: 0.0234 vs 0.0219. High-end: 0.0308 vs 0.0350.
- AMD budget and Nvidia mid-range are one card each, so this is a pattern, not proof.

**Build:** NATIVE. Data: gpu_tableau_ready.csv. Columns: Price_Tier (sort Budget, Mid-range, High-end). Rows: AVG(Price_per_Mark). Color: Brand. Label: AVG. Tooltip: CNT(Full_Model_Name). Set AMD to #D9692F and Nvidia to #085041.

### 11. Matched pairs

**Deck slides:** 31, 32

**Text on the dashboard:**

- Each bar: how an AMD card's price per point compares with its Nvidia pair. Left of zero means AMD is cheaper.
- AMD is 2% to 23% cheaper in the five higher-priced pairs, and 3% to 64% dearer in the three entry-level pairs. I matched the pairs myself.

**Build:** NATIVE. Data: tableau_pairs.csv. Rows: Pair (sort by the measure). Columns: SUM(AMD_Price_per_Point_vs_Nvidia_Pct). Color: Cheaper_per_Point. Analytics tab: add a constant line at 0. Expect -23, -21, -23, -10, -2, +64, +34, +3.

### 12. Price against performance

**Deck slides:** 33, 34

**Text on the dashboard:**

- Each dot is a card. Up and to the left is better value.
- The RX 7900 XT ($699.99, 28,900) outscores the RTX 5070 ($979.65, 28,679) for about $280 less.

**Build:** NATIVE. Data: gpu_tableau_ready.csv. Columns: AVG(Current_Street_Price). Rows: AVG(G3D_Mark). Mark type: Circle. Color: Brand. Label: Full_Model_Name. For the wider field of 48 cards, make a second sheet from gpu_price_history_tableau.csv (filter price_date to Dec 2024; columns AVG(retail_price), rows AVG(threedmark)).

### 13. Memory per dollar

**Deck slides:** 37

**Text on the dashboard:**

- Gigabytes of VRAM per $100. Higher is more memory for the money.
- From $300 to $999, AMD gives far more. In the $300 to $599 tier: 3.35 vs 1.82 GB (Dec 2024).
- Above $1,000 there is only one AMD card, so I do not read much into that tier.

**Build:** NATIVE (this is your existing sheet). Data: gpu_price_history_tableau.csv. Columns: price_tier. Rows: AVG(vram_gb_per_100_usd), NOT SUM. Color: brand. Filter price_date to December 2024. Expect 2.97/2.65, 3.35/1.82, 2.39/1.39, 1.06/1.09 (AMD/Nvidia). With all months instead: 3.20/2.72, 3.12/1.95, 2.28/1.50, 1.66/1.23.

### 14. Used prices and efficiency

**Deck slides:** 38, 39

**Text on the dashboard:**

- Used discount, Dec 2024: in the $300 to $599 tier, used AMD cards sit about 12% below new and used Nvidia cards about 49% below. One month, small groups: a lead, not a finding.
- Efficiency: Nvidia is more efficient in three of four same-generation pairs (RTX 4060: 92 points per watt vs 66 for the RX 7600).

**Build:** NATIVE, two sheets from gpu_price_history_tableau.csv. Used: Columns price_tier, Rows AVG(used_saving_pct), Color brand, filter Dec 2024. Efficiency: calculated field AVG([threedmark]) / AVG([watts]); Rows gpu_name (filter to RTX 4060, 4060 Ti, 4070, 4070 Ti, RX 7600, 7700 XT, 7800 XT, 7900 XT); Color brand. This is the same data as your second existing sheet.

### 15. Street price against launch price

**Deck slides:** 40, 41

**Text on the dashboard:**

- 2022 to 2024 cards sell near launch price. 2025 to 2026 cards sell well above it: AMD +27% on average, Nvidia +50%.
- RTX 5070 +78%, RTX 5070 Ti +60%, RTX 5080 +50%, RX 9070 XT +33%.
- One month of prices and small samples: a pattern, not proof. I show what moved, not why.

**Build:** NATIVE. Data: gpu_tableau_ready.csv (the corrected file). Rows: Full_Model_Name sorted by the measure. Columns: AVG(Premium_vs_MSRP_Pct). Color: Brand. Constant line at 0.

### 16. Value over time

**Deck slides:** 42

**Text on the dashboard:**

- Median price per G3D point by year, log scale. From 2009 to 2019 the median card got about 19 times cheaper for Nvidia and 27 times for AMD.
- Nvidia was lower in 9 of those 11 years. AMD was lower in 2021 (0.037 vs 0.045, on five cards).
- Years with fewer than 5 priced cards for a brand (2020, 2022) are left out. Only 31 of 506 priced cards are from 2020 to 2022.

**Build:** NATIVE. Data: tableau_median_by_year.csv. Filter Enough_Cards = Yes. Columns: Test_Year (discrete). Rows: AVG(Median_Price_per_Point), right-click the axis, Edit Axis, Logarithmic. Color: Brand.

### 17. Benchmark against real games

**Deck slides:** 20, 43

**Text on the dashboard:**

- The RTX 5070 Ti looks 19% faster than my RX 9070 XT on the synthetic G3D Mark. Across 55 real games it is about 5% faster at both 1440p and 4K.
- A likely reason: the synthetic score includes work games do not do. I stopped trusting any single score without asking what it measures.

**Build:** NATIVE. Data: synthetic_vs_real_gap.csv. Columns: Metric_Type or Resolution. Rows: SUM(Nvidia_Lead_Pct). Label the bars. Expect 19, 5, 5.

### 18. CPUs: benchmark against games

**Deck slides:** 44, 45, 47

**Text on the dashboard:**

- CPU Mark (productivity): Core Ultra 9 285K 67,300 vs Ryzen 7 9800X3D about 40,000. Real 1080p gaming, 45 games: the 9800X3D is about 24% faster, and $130 cheaper.
- My analogy: a straight pipe is smooth; a manifold that merges four cylinders is where flow congests. A single thread has one clean path; cores sharing one cache merge. An analogy, not a measurement.
- [Your sentence connecting the analogy to the result]

**Build:** Image object for pipe_analogy.png (in the image zip). For the lineup, use cpu_data_clean.csv as a text table sheet (CPU, Price, CPU Mark), or a screenshot.

**You supply:** pipe_analogy.png

### 19. Challenges

**Deck slides:** 55, 56

**Text on the dashboard:**

- 1. Imports silently lost data (decimals, then 8 rows). Row counts exposed it. Lesson: check counts after every import.
- 2. A value column was wrong for two cards. Excel disagreed with the imported column. Mid-range Nvidia fell from 0.0340 to 0.0219. Lesson: cross-check across tools.
- 3. A benchmark overstated a gap: 19% on paper, 5% in games. Lesson: match the metric to the use.
- 4. One dataset covered only Nvidia and others ended in 2022. I layered three sources and stated each limit.

**Build:** Text objects. Optionally a small before/after table for challenge 2 (RTX 4070 Ti 0.040 to 0.0269, RTX 4070 0.034 to 0.0219).

### 20. Takeaways and limits

**Deck slides:** 61, 60, 58, 59

**Text on the dashboard:**

- 1. Value is close overall: 0.0243 for AMD, 0.0259 for Nvidia. 2. AMD's clearer edge is memory per dollar from $300 to $999. 3. The newest cards cost the most over launch price. 4. Match the benchmark to the use.
- Limits: small samples; one price snapshot; G3D Mark and 3DMark are different scales; the public files stop in 2022 and 2024 with few priced cards after 2019; gaming only; one pair checked against real games.

**Build:** Text objects. Keep the Q&A answers (slides 58, 59 in the deck) in your script as backup rather than on a story point.

### 21. My budget

**Deck slides:** 63

**Text on the dashboard:**

- My whole PC: $2,200 [confirm before or after tax]. Ryzen 7 7800X3D, RX 9070 XT 16GB, 64GB DDR5-6000, 2TB storage.
- CPU and GPU: about $1,148.50. Everything else: about $1,051.50.
- I needed: 1080p now with headroom for 1440p; 16GB of VRAM; room to upgrade cooling, memory and the motherboard later; a budget of [about $2,250 before tax].

**Build:** Three big-number text objects ($2,200, $1,148.50, $1,051.50) plus a short list.

### 22. What if I had spent differently?

**Deck slides:** 64, 65

**Text on the dashboard:**

- Hold the rest of the PC fixed and change only the graphics card.
- RTX 5080: +$700. RTX 5070 Ti: +$400. RTX 5070: +$180. Below my pick: RX 7900 XT -$100, RTX 4070 -$210.
- Real games: RTX 5070 Ti within about 5% (TechSpot 5% ahead; KitGuru 9070 XT 6% ahead). RX 7900 XT: 9070 XT 6% to 14% faster in three games (Tech4Gamers), mixed in TechSpot. 9070 XT 11% to 14% ahead of the RTX 4070 Super. [Cite each source]

**Build:** NATIVE. Data: tableau_swap_test.csv. Rows: GPU sorted by PC_Cost_With_GPU. Columns: SUM(PC_Cost_With_GPU). Color: My_Pick. Analytics tab: constant line at 2200. Label with Difference_vs_My_2200_PC. Real-game findings as a text object.

### 23. Why the 7800X3D

**Deck slides:** 66

**Text on the dashboard:**

- 7800X3D: $320 to $375 (I use $349), CPU Mark 34,278. 9800X3D: about $449, 39,977.
- In games the 9800X3D is about 8% faster at 1080p with a top-end GPU, about 3% at 1440p, about the same at 4K. It would add about $75 to $130.
- With my RX 9070 XT the gap is likely smaller (my inference). [Cite TechSpot, Tech4Gamers, TechPowerUp]

**Build:** Text objects, or a small three-row table.

### 24. My choice

**Deck slides:** 67

**Text on the dashboard:**

- Ryzen 7 7800X3D and Radeon RX 9070 XT, 64GB DDR5-6000, 2TB storage, $2,200.
- It fits: the RTX 5070 Ti would add about $400 for a gap of 5% or less.
- The GPU: the fastest current-generation card I priced that fits. The CPU: about 8% behind the 9800X3D at 1080p for $75 to $130 less.
- Room to grow: 16GB VRAM, 64GB memory, 2TB storage, and budget to upgrade cooling, memory and the motherboard later.

**Build:** Text objects; make the first line the largest thing on the page.

### 25. The End

**Deck slides:** 68, 62

**Text on the dashboard:**

- I did not look for the brand that wins everything. I looked for the best CPU and GPU that fit my budget, and checked each alternative against real games.
- Next: add the missing cards, productivity workloads, automatic price history, used-price analysis.
- Thank you. Questions? [Your name] | [email or LinkedIn] | [GitHub link]

**Build:** Text objects only.

## Before you present

- Check every chart against the expected numbers above. A mismatch almost always means a Sum that should be an Average, or a filter left on.
- Replace every [bracket] with your own words or screenshots.
- Practice with Presentation Mode (F7) over Google Meet, and keep the story point order matching your script.