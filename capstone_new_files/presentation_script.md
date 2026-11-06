# Presentation script: Price vs. Performance, choosing the best CPU and GPU for my budget

Each script is written to be spoken, about 30 to 60 seconds per slide. Put it in your own words, but keep the rhythm: one idea per slide, a number or example after each definition, and limits said plainly.

**Anything in [brackets] is yours to fill in:** your name and date, the Agile slides, screenshots (including your Tableau dashboard and your scraper output), the Kaggle dataset name and author, whether the $2,200 includes tax, your budget figure, sources to cite, how your pipe analogy connects to the CPU results, and your career next steps.

The same text is in the speaker notes of each slide in the deck, so presenter view shows it.

## Slide 1: Price vs. Performance: Choosing the Best CPU and GPU for My Budget

Hi everyone, I'm [your name]. This is my capstone for the Savvy Coders data analytics program. It started with a real decision. I was building a gaming PC, and I had a fixed budget. So I used data to answer one question: what is the best CPU and graphics card I can fit in that budget? I'll show you where the data came from, how I cleaned it, what it said, and what I bought.

## Slide 2: The question

Here's the question. Which CPU and GPU give me the most for my budget, and how do AMD and Nvidia compare on price and performance along the way? My audience is gamers building a PC on a budget, like me and my friends. Other users, like animators and developers, are a next step. It matters because names like Ti, XT and bigger model numbers can hide what a card is really worth, and GPU prices have moved a lot this year. I'll finish by telling you what I chose and why.

## Slide 3: Agile: my role and Jira

[Fill this in with what you actually did.] For Agile, my role was [Scrum Master, Product Owner or Developer]. [In a sentence or two, say what that involved, for example keeping the board current and deciding which question to answer first.] I used Jira to track [the backlog, sprints, user stories and story points]. Here's one example of a user story. As a budget-conscious PC builder, I want to compare GPU value by price tier, so that I can pick the best card for my budget. The acceptance criteria were that Python, SQL and Excel all give the same answer. [Swap in your own story and story points if you have them.]

## Slide 4: Agile: ceremonies and certification

[Only list what you really did.] These are the Agile ceremonies I took part in. Daily standups: [how often, and what you reported]. Sprint planning: [what you planned and estimated]. Sprint review and backlog grooming: [what you demoed and what changed afterward]. Retrospective: [one thing that worked, one thing you changed]. For example, after an import dropped rows in my database, I started checking row counts after every import. And for certification, I'm [ICAgile Foundations of Agile certified, or working toward it].

## Slide 5: Hypothesis and approach

My hypothesis was this. With a fixed budget, the card with the biggest name isn't automatically the best buy, and AMD may offer comparable real-world performance for less money. To test it, I did three things. First, I collected data: two public Kaggle datasets for history, and my own data for the current generation. Second, I cleaned and joined it in SQL, and cross-checked the results in Python and Excel. Third, I compared value by price tier, memory per dollar, and street price against launch price.

## Slide 6: G3D Mark: the score behind most of my charts

Before I show any charts, I need to explain the main number in them. It's called G3D Mark, and it's a score from a company called PassMark. They average test results from thousands of people running the same benchmark, and give each card one number. A higher score means a faster card on that test. The score has no unit, and it isn't frames per second. It only means something next to another card's score. The RX 9070 XT scores about 27,000, and the RTX 5080 about 36,000. I used it because it covers cards across many years. Its weakness is that it's a synthetic test, and I'll show you where that mattered.

## Slide 7: 3DMark: the score in the price-history charts

One more score to know. One of my data files uses a different benchmark called 3DMark. Same idea, different test, so the same card gets different points. The RTX 4060 scores about 19,700 on G3D Mark but about 10,600 on 3DMark. That's why I never put the two on one chart. I also noticed something. Across the nine cards that are in both files, AMD cards earn about 81 percent as many points on 3DMark as on G3D Mark, and Nvidia cards about 63 percent. So the two tests don't rank the brands exactly the same way. I treat the price-history charts as one view, not the final word.

## Slide 8: Price per point: what the number means

Now the number I use most: price per point. It's just the price divided by the score, so it tells you how many dollars you pay for each point of speed. The RX 9070 XT costs 799 dollars and 50 cents for about 27,000 points. That's roughly 3 cents a point, or about 29 dollars for every 1,000 points. The RTX 5070 Ti comes out around 37 dollars. Lower is better. A 1,200 dollar card can still be the better deal if it's more than twice as fast as a 600 dollar one. The catch is that this number ignores memory, power use and features, so I never use it alone.

## Slide 9: Why VRAM matters

That's why I also look at memory, called VRAM. It's the graphics card's own memory, where it keeps the textures and data it's working on right now. When it runs short, the card borrows slower system memory, and you can get stutter or lower texture quality. Tom's Hardware tested the same chip with 8 gigabytes and with 16. In games without ray tracing, the 8 gigabyte card was only about 5 percent slower. In ray-traced games at 1080p ultra, it was about 26 percent slower. So it depends on the game, but more memory is a cheap way to make a card last longer. [Add Tom's Hardware to your sources slide.]

## Slide 10: Terms and card names

Here are the other terms you'll hear. VRAM is the graphics card's own memory. TDP is its rated power in watts, which is a rating, not a measurement. MSRP is the launch price, and street price is what stores charge now. I split cards into three price tiers: budget up to 350 dollars, mid-range up to 700, and high-end above that. On names, Ti and Super mean a faster version of an Nvidia card, XT and XTX mean a faster AMD card, and X3D means an AMD processor with extra cache that helps games. And finally, synthetic scores come from a test program, while real-world results come from timing actual games.

## Slide 11: How I measured value

I used three measures, because each answers a different question. Price per point is the street price divided by the G3D score. Its limit is that it's a synthetic score. The premium over launch price is how far the street price sits above or below the launch price, and its limit is that it's one month of prices, September 2026. Memory per hundred dollars is gigabytes of VRAM divided by price, times 100, and its limit is that more memory doesn't mean a faster card. No single measure decides anything. I look at all three together.

## Slide 12: Datasets and resources

Here are my data sources. The main file has 2,317 rows of GPU prices and benchmark scores from 2009 to 2022, from Kaggle. [Confirm the exact dataset name and author.] The second is a Kaggle price history, 1,087 rows of monthly retail and used prices from late 2022 to the end of 2024, with a small file of specs. The third is my own file of 16 current-generation cards with September 2026 street prices. The fourth is a small CPU comparison, also compiled by me. I also used PassMark and TechSpot reviews, and Wikipedia's launch-price tables, which I scraped to check my data. The two Kaggle files are my main data. My own files cover the current generation, which the public data doesn't reach.

## Slide 13: Dataset profile: the benchmark file

Let me profile the main file. It has 2,317 rows and 10 columns, covering 2009 to 2022. The first thing to know is that 76 percent of the prices are missing, and 70 percent of the power ratings. By brand, there are 1,188 AMD cards, 738 Nvidia, 364 other, and a few Intel and Apple. After cleaning, 506 rows remain, but prices thin out after 2019, and only 31 of those rows are from 2020 to 2022. Across all of them, the median price per point is 0.144 for AMD and 0.140 for Nvidia, within 3 percent of each other. So the older data alone doesn't crown a winner.

## Slide 14: Dataset profile: the price history

The second file is a price history. It has 48 GPUs, 24 AMD and 24 Nvidia, with 26 monthly snapshots from November 2022 to December 2024. That's 1,087 price rows. About 114 prices are missing, 62 retail and 52 used. The newest cards are the RTX 40 and RX 7000 families, and only 20 of the 48 have all 26 months. This file uses a different score, 3DMark, so I never put it and my own data on the same axis.

## Slide 15: Dataset profile: my own data

My own file has 16 current cards, eight AMD and eight Nvidia. On average, the AMD cards cost 616 dollars and the Nvidia cards 759. AMD averages 16 gigabytes of memory against 11.5 for Nvidia, and the average price per point is 0.0243 for AMD and 0.0259 for Nvidia. The prices are retailer listings from September 2026, and the scores come from PassMark. Two prices still need checking, the RX 7700 XT and the RTX 4060 Ti. Sixteen cards is small, so I use this file for the current generation and lean on the public files for scale.

## Slide 16: Why these 16 cards

Why these 16 cards? Four were the cards I was actually choosing between: the RTX 5060, the RTX 5070, the RTX 5070 Ti and the RX 9070 XT. For each Nvidia card, I matched an AMD card of the same tier and era, which gives eight pairs. And I added the previous generation, so someone on a smaller budget is covered too. What this leaves out is other cards you might ask about. The next two slides show which ones, and what I did about them.

## Slide 17: Cards people will ask about

I checked the cards people usually ask about against my three files, by name. Older cards like the RTX 3060 and the RX 6600 are covered by the public files. But three current cards aren't in any of my files: the RTX 5090, the RTX 5060 Ti and the Intel Arc B580. That's because the public files stop in 2022 and 2024, and my own list followed my build decision. So I looked those three up separately.

## Slide 18: The cards missing from my data

Here's what I found for those three. The RTX 5060 Ti has 16 gigabytes and sells for between 560 and 805 dollars depending on the source. At 560 it costs 0.0248 per point, more than the RX 9060 XT or the RTX 5060, though it has more memory. The RTX 5090 is the fastest card, but at about 2.6 times the RTX 5080's price per point, it's a different kind of purchase. The Intel Arc B580 has 12 gigabytes. At its 249 dollar launch price it matches the RTX 4060 and RX 7600 per point, but at 369 dollars it doesn't. Because prices disagree, I show ranges, and I kept these cards out of my averages. [Cite each source.]

## Slide 19: Why the three cards are not in my averages

Why not just add them to the data? Three reasons. First, the prices disagree. The 5060 Ti ranges from 560 to 805 dollars, so any single price would be a guess that flows into every average. Second, the RTX 5090 alone would lift the Nvidia high-end average from 0.0350 to about 0.050, so it needs a tier of its own. Third, my notebook, SQL and Excel results all match today, and adding cards changes all three. So the next step is to add them as flagged rows, with one price rule and a separate top tier.

## Slide 20: What surprised me

This is what surprised me most. On a synthetic benchmark, the RTX 5070 Ti looks 19 percent faster than my RX 9070 XT. Across 55 real games at 1440p and 4K, it's about 5 percent faster. The same thing happened with processors. The Core Ultra 9 285K wins the productivity benchmark, but the Ryzen 7 9800X3D, an X3D chip like the one I chose, is about 24 percent faster in games at 1080p. After that, I stopped trusting any single score without asking what it actually measures.

## Slide 21: Wrangling the data

Now, wrangling the data. The main file started at 2,317 rows. Keeping only NVIDIA and AMD cards left 1,926. Only 513 of those had a price. And after removing seven workstation cards priced over 3,000 dollars, 506 rows remained. In other words, 76 percent of the raw rows had no price. I did the cleaning in SQL, and used Python and Excel to cross-check the results.

## Slide 22: Data that was missing, and what I did

Here's what was missing, and what I did about it. Most benchmark prices were missing, so I dropped those rows, which took 2,317 rows down to 506. One public dataset had no AMD consumer cards at all, which would have biased the comparison toward Nvidia, so I replaced it with sources that cover both brands. The public files stop in 2022 and 2024, so I used them as history, and my own data for the current generation. And three current cards aren't in any file, so I looked them up separately. Every gap is named on this slide, so nothing is hidden.

## Slide 23: Data that was distorted, and how I fixed it

These are the problems where the data was there, but wrong. In the price history, zeros stood in for missing prices, 62 retail and 52 used. A zero would read as free and drag averages down, so I turned them into blanks. Two value figures I'd entered by hand were wrong, for the RTX 4070 and the 4070 Ti. That overstated Nvidia's mid-range cost by more than half, so I recalculated the whole column and reran Python, SQL and Excel. My SQL imports lost decimals and then eight rows, which I caught by checking row counts. And seven workstation cards over 3,000 dollars would have skewed the averages, so I removed them. Two benchmark scales also rank the brands differently, so I keep them on separate charts.

## Slide 24: Before and after: the benchmark file

Here's the benchmark file before and after cleaning. At the top are four sample rows. The RTX 3080 Ti stays. The Radeon Pro VII has no price, so it's dropped. The TITAN V isn't labeled NVIDIA or AMD in this file, so it's dropped. And the RTX A6000 is a workstation card over 3,000 dollars, so it's dropped too. In total I removed 391 other brands, 1,413 rows with no price, and seven workstation cards. That leaves 506 rows, and I added one new column, price per point, which is price divided by score.

## Slide 25: Before and after: the price history

Same idea for the price history. Before, I had two separate files. The dates were text in day-month-year order, a zero meant no data, and the specs had units stuck to the numbers, like 75W and 2GB. After, the files are joined on the GPU name, the units are gone, the zeros are blanks, and the dates are real dates. It's the same GTX 1050 in the same months. This is the cleaning I did in SQL, and it's the reason my Tableau charts work.

## Slide 26: Data manipulation: my toolkit

Here's my toolkit. Pandas for loading, filtering and calculating. Jupyter notebooks, one cell per step, so every result sits next to the code that made it. Matplotlib for the charts. SQLite as the database for my raw and cleaned tables, and DB Browser for importing files and running queries, which is also where I caught my import problems. [Show a screenshot of a notebook cell and the DB Browser table list here.]

## Slide 27: Coding process: one question, three tools

This is the most important coding slide. It shows one question answered three ways: Python, SQL and Excel. In Python it's one line: group by tier and brand, and average the price per point. In SQL, a CASE statement gives each card a tier, then groups and averages. In Excel, a formula divides price by score, and a PivotTable does the grouping. All three give the same answer. Budget is 0.0157 for AMD against 0.0152 for Nvidia. Mid-range is 0.0234 against 0.0219. High-end is 0.0308 against 0.0350. That match is how I know the numbers are right.

## Slide 28: Coding process: show the code

Here's where I show the code itself. [Add a screenshot of your Python cell with its output, then your SQL query with its results, then your Excel formula bar and PivotTable.] I wrote and ran everything in VS Code, and I committed my work to GitHub as I went. I also used web scraping to check my data, and I'll show that next. [Mention any other API you used.]

## Slide 29: Web scraping: checking my launch prices

Here's the web scraping I added. I wanted to check my launch price column, so I wrote a script that downloads Wikipedia's launch-price tables for the RTX 40 and 50 series and the RX 7000 and 9000 series, through Wikipedia's API, and compares every price with my data. I used the API and sent one request a second, and I did not scrape store sites, because they usually forbid it and block bots. 15 of my 16 launch prices matched. One didn't. The RTX 4070 launched at 599 dollars, and my file had 549, which is the price after NVIDIA's cut. Fixing it moves that card from 7.5 percent over launch price to 1.5 percent under, and Nvidia's 2022 to 2024 average from about minus 1 to minus 3 percent. The 2025 and 2026 results didn't change. [Show a screenshot of your notebook output here.]

## Slide 30: Value by price tier

This is my first main result, straight from my notebook. Each bar is dollars paid per G3D Mark point, so lower is better. Overall, AMD averages 0.0243 and Nvidia 0.0259. The tiers are close. AMD is cheaper per point only at the high end, 0.0308 against 0.0350. In budget and mid-range, Nvidia is a hair cheaper. I need to be honest about sample size, though. The AMD budget bar and the Nvidia mid-range bar are one card each. So no brand wins every tier, and the best choice depends on your budget.

## Slide 31: Head-to-head: matched pairs

A more direct way to compare is card against card. Each row pairs an Nvidia card with an AMD card of the same tier and era. I matched these pairs myself. In the five higher-priced pairs, the AMD card is cheaper per point, by 2 to 23 percent. For example, the RX 9070 XT is 400 dollars less than the RTX 5070 Ti, and 21 percent cheaper per point. In the three entry-level pairs, the Nvidia card is cheaper per point, because AMD charges more for more memory. So AMD wins from the 4070 class upward, and Nvidia wins at the entry level.

## Slide 32: Head-to-head: price per point

Here's the same comparison as a picture. Each bar shows how an AMD card's price per point compares with its Nvidia pair. Left of zero means the AMD card is cheaper. You can see the five higher-priced pairs sit on the left, and the three entry-level pairs sit on the right. The code is short: one division per card, then one comparison per pair. AMD's edge starts at the 4070 class and above, which is where my own choice sits.

## Slide 33: Price against performance

This is price against performance. Each dot is a card. Further left is cheaper, higher is faster, so up and to the left is better value. You can see that price climbs faster than speed. The RTX 5080 costs nearly six times as much as an RX 7600, for about twice the score. And here's one concrete example. The RX 7900 XT, at about 700 dollars, scores slightly higher than the RTX 5070 at about 980. That's about 280 dollars less. More money still buys speed, but each extra point costs more.

## Slide 34: The wider field: all 48 cards

People will ask what else is out there, so here's the wider field. Each dot is one of the 48 cards in the price history, for December 2024, scored on 3DMark. Left is cheaper and higher is faster. My shortlist is outlined, and the faded dots are everything else. Most AMD cards sit along the upper-left edge, and Nvidia cards tend to sit lower and further right. My shortlist is on the good-value side of the field, and older, slower cards fill in the lower left.

## Slide 35: Best value among all 48 cards

If I rank all 48 cards by price per point for December 2024, this is the top eight. Ten of the best twelve are AMD, including four older RX 6000 cards like the RX 6650 XT and the RX 6600. My shortlist ranks from second to twenty-second. The cheapest per point include older, slower cards, which is why I look at the score as well as the price. And remember this uses the 3DMark scale and 2024 prices, so the numbers differ from my 2026 table.

## Slide 36: Entry level: value against VRAM

This chart is for friends on a tighter budget. The bars are price per point, lower is better, on the left axis. The line is memory in gigabytes, on the right axis. The RTX 4060, RX 7600 and RTX 5060 are almost tied, around 0.015 to 0.016. The RX 9060 XT costs more per point, 0.0214, but it's the only one with 16 gigabytes, double the others. That's a trade-off, not a winner. Whether it's worth it depends on how long you want the card to last.

## Slide 37: VRAM per dollar

Now memory per dollar, from the price history for December 2024. Each bar is gigabytes of VRAM per hundred dollars, so higher means more memory for the money. From 300 to 999 dollars, AMD gives far more. In the 300 to 599 dollar tier, it's 3.35 gigabytes per hundred dollars for AMD against 1.82 for Nvidia. Under 300 dollars it's close, and above 1,000 there's only one AMD card, so I don't read much into that. This matters because memory decides how long a card stays useful.

## Slide 38: Used prices

This one is about used prices. Each bar is how far the used price sits below the new price. In the 300 to 599 dollar tier, used AMD cards are about 12 percent below new, and used Nvidia cards about 49 percent below. That could help a tight budget, because used Nvidia cards drop further. But I'd call it a lead, not a finding. It's one month, the groups are seven and eight cards, and six cards had a used price above the new price, which I can't explain.

## Slide 39: Efficiency: points per watt

I want to be fair to Nvidia, so here's efficiency. Each bar is 3DMark points per watt of rated power, so higher means more efficient. Nvidia is more efficient in three of the four same-generation pairs. The RTX 4060 gets 92 points per watt, against 66 for the RX 7600. The RTX 4070 Ti and the RX 7900 XT are about even. Efficiency affects heat, noise and the power supply you need. It's a real Nvidia strength that my value numbers leave out.

## Slide 40: Street price against launch price

This shows how far street prices sit from launch prices, in percent. Cards from 2022 to 2024 sell right around launch price. Cards from 2025 and 2026 sell well above it: about 27 percent above for AMD on average, and 50 percent above for Nvidia. The RTX 5070 is 78 percent above. I can't tell you why from this data, so I describe the pattern and don't claim a cause. And it's one month with small samples, so it's a pattern, not proof.

## Slide 41: Price over time, 2023 to 2024

This sets up the last slide. Each line is a card's retail price by month. Through 2024, mid-range cards got cheaper. The RTX 4070 fell 14 percent, from 628 to 539 dollars. The RX 7700 XT fell 10 percent, and the RX 7800 XT 9 percent. Entry cards stayed within 3 percent. So prices were flat or falling through 2024, which is why the 2025 and 2026 premiums stand out.

## Slide 42: Value over time, 2009 to 2021

This answers a question from my planning board: how has value changed over time? Each point is the middle card's price per point that year, on a log scale. From 2009 to 2019, the median card got about 19 times cheaper per point for Nvidia, and 27 times for AMD. In this older file, Nvidia had the lower median in 9 of those 11 years. You'll see a gap at 2020. I only plot a year when both brands have at least five priced cards, and 2020 has only four Nvidia cards. 2021 qualifies, and it's the one year where AMD is lower, 0.037 against 0.045, though that's five AMD cards. 2022 is left out for the same reason. In fact, only 31 of my 506 priced cards are from 2020 to 2022, so those years are thin, and that's why the story picks up again with the price history. So value has always moved with the era, and any AMD edge is recent, not a rule.

## Slide 43: A benchmark gap that shrinks

This is the finding that most affected my own purchase. Each bar is how much faster the RTX 5070 Ti is than the RX 9070 XT. The synthetic G3D Mark says 19 percent faster. Across 55 real games, it's about 5 percent, at both 1440p and 4K. Paying for the 19 percent would have meant paying for speed that games don't use. A likely reason is that the synthetic score includes non-gaming work, though I haven't proven that.

## Slide 44: CPU: benchmark against real games

The same lesson applies to processors. On the left is the Ryzen 7 9800X3D, on the right the Core Ultra 9 285K. On the PassMark productivity benchmark, the 285K wins, 67,300 to about 40,000. But in real 1080p gaming, across 45 games, the 9800X3D is about 24 percent faster, and it costs 130 dollars less. CPU Mark rewards core count. In games, the extra cache on X3D chips, like the 7800X3D I chose, matters more. And the gap narrows at higher resolutions, where the graphics card becomes the limit.

## Slide 45: A way to picture CPU cores: the straight pipe

Here's a way I picture CPU cores, using something I know: exhaust pipes. On the top left, a straight pipe has one source and nothing merges, so the flow stays smooth. On the top right, a manifold merges four cylinders into one pipe, and that merge point is where flow can congest. A processor follows the same pattern. On the bottom left, a single thread has one clean path from a core to memory. On the bottom right, when several cores share one cache, their requests merge, and that merge point can congest. This is an analogy, not a measurement. [Connect it to your point in your own words, for example how the CPU Mark benchmark adds up many cores, while games lean on a few fast paths.]

## Slide 46: CPU advantage by resolution

This shows that gap by resolution. About 24 percent at 1080p comes from a 45-game test. The 6 and 2 percent bars for 1440p and 4K are my estimates, not measurements, and I want to be clear about that. The pattern is solid, though. At higher resolutions the graphics card sets the frame rate, so the CPU matters less. This is also why I felt my combination is well suited to future-proofing and upgrading in a couple of years.

## Slide 47: The CPUs I compared

Here's the full CPU lineup, so my choice doesn't look cherry-picked. My chip is highlighted. On CPU Mark per dollar, the Core Ultra 7 265K and the Core i5-14600K look best. But CPU Mark measures multi-core work, not gaming, and I don't have gaming results for those chips, so I make no gaming claim about them. I chose the 7800X3D for gaming performance and price. Its price is a mid-2026 range of 320 to 375 dollars, and I use 349.

## Slide 48: Tableau: interactive view

This is the interactive view I built in Tableau, from the same cleaned price history. [Show the dashboard here.] The chart on the left shows memory per hundred dollars by brand and price tier. The chart on the right shows each card's 3DMark score, shaded by its wattage and labeled with its used price. There are filters for GPU name and retail price, so you can look at one card or a price range. Averaged over all 26 months, AMD gives more memory per hundred dollars in every tier, and the widest gap is in the 300 to 599 dollar tier, 3.12 against 1.95. It ties together three things from earlier: memory per dollar, efficiency and used prices. [Before you present, check that every measure in Tableau is set to Average, not Sum. Sum adds up the monthly values, so the bars would be inflated and the brands compared unfairly.]

## Slide 49: Applying it: did I choose well?

Now let me apply this to my own decision. Of the three high-end cards I compared, the RX 9070 XT costs 799 dollars and 50 cents and comes out at 0.0294 per point, the best of the three. The RTX 5070 is 0.0342 and the RTX 5070 Ti is 0.0371. In 55 real games, the 5070 Ti is only about 5 percent faster, for about 400 dollars more. I also liked the 9070 XT for its 16 gigabytes of memory, and for the headroom at 1440p if I upgrade my monitor.

## Slide 50: My upgrade in numbers

Here's my upgrade in numbers. The graphics score goes up 65 percent, from my RTX 2060 Super at 16,500 to the RX 9070 XT at 27,183. The CPU Mark goes up 40 percent, from my Ryzen 7 3800X at 24,463 to the 7800X3D at 34,278. My new CPU and GPU cost about 1,148 dollars at today's prices. CPU Mark measures productivity work, and the X3D cache likely helps games more than the score shows, but I haven't measured that, so I won't claim it.

## Slide 51: Cost of four builds

This chart compares four builds by cost, CPU and GPU only. My 2019 parts cost 728 dollars at launch prices. A budget rebuild costs 629, a mid-range rebuild 823, and my build about 1,148. The point for anyone on a budget is that a modern rebuild can cost less than the parts it replaces. The budget one is 99 dollars less.

## Slide 52: Performance of four builds

Here are the same four builds by performance. Red is CPU Mark, teal is the graphics score. The graphics score rises at every step. My build's CPU Mark is a little below the mid-range rebuild's, because CPU Mark measures productivity work and the 7800X3D's cache is built for games. Against my 2019 parts, my build is up 40 percent on the CPU and 65 percent on the graphics card. The budget rebuild is up 10 and 22 percent.

## Slide 53: What each CPU + GPU budget buys

This table is for different wallets, and it's about CPU and GPU spending only. Balanced picks a strong gaming CPU first, using the 9800X3D, and spends the rest on the GPU. Max-GPU buys the cheapest CPU and the biggest GPU. At 800 dollars, both pick the same parts. From 2,000 dollars up, nothing in my data beats the RTX 5080. The last row is my actual build. Its 2,200 dollars is the whole PC, and the CPU and GPU took about 1,148 of it. It uses the 7800X3D, which is about 100 dollars cheaper.

## Slide 54: Where more money stops helping

Here's the same idea as a chart. Each pair of bars is a CPU and GPU budget, and the bars show the GPU score you can reach. The flat top is the finding: from 2,000 dollars up, nothing beats the RTX 5080, so 2,300 buys the same parts. My build is the single bar on the right. It spends about 1,148 dollars on CPU and GPU, because the rest of my 2,200 dollar PC took about 1,051. A 1,949 dollar CPU and GPU would have made the whole PC about 3,000.

## Slide 55: Challenges and how I solved them

Here are four challenges. First, my SQL imports silently lost data, first decimals, then eight rows. Row counts, 498 against 506, exposed it. I set column types and the quote character. The lesson: check counts after every import. Second, a value column was wrong. Excel disagreed with the imported column for two cards, I recomputed it and reran everything, and the mid-range result changed. The lesson: cross-check across tools. Third, a benchmark overstated a gap, 19 percent on paper and 5 in real games. The lesson: match the metric to the use. Fourth, one dataset only covered Nvidia and another ended in 2022, so I layered three sources and stated each limit. The lesson: check coverage before building on data. I also caught a wrong 1,600 dollar budget pick by asking why only one brand appeared.

## Slide 56: Before and after: correcting my own data

Let me show the second challenge in detail. This is the price-per-point column as I first entered it, against price divided by score. For the RTX 4070 Ti, I had 0.040, and the right answer is 0.0269. For the RTX 4070, 0.034 against 0.0219. The other rows only changed by rounding. The effect was large. The mid-range Nvidia figure fell from 0.0340 to 0.0219, and Nvidia's overall average from 0.0290 to 0.0259. AMD barely moved. I caught it because Excel's formula column disagreed with the imported column. Then I recalculated the whole column and reran Python and SQL.

## Slide 57: The chart that exposed a gap

This chart exposed a gap. It shows memory as bars and rated power as a line, and all nine cards are Nvidia. That's because the public spec dataset I used had no AMD consumer cards. I noticed because every bar was the same brand. I replaced it with sources that cover both brands. It also lists the 16 gigabyte RTX 4060 Ti, while my price and score are for the 8 gigabyte version, which is a second reason to compare like with like.

## Slide 58: Questions I expect: the cards

I expect questions about the cards. Why not the RTX 5060 Ti? It isn't in my public datasets, so I looked it up separately. At 560 dollars it costs 0.0248 per point, above the RX 9060 XT and RTX 5060, though it has 16 gigabytes. What about Intel Arc? None are in my data. The B580 has 12 gigabytes, and at its 249 dollar launch price it matches the RTX 4060 and RX 7600 per point. Why only 16 cards? They're the cards I was choosing between, plus a rival for each, and the public files add 48 and 2,317 cards for context. And why not the RTX 5090? It's the fastest card, but at about 2.6 times the RTX 5080's price per point, it's a different kind of purchase.

## Slide 59: Questions I expect: the method

And the method questions. Is G3D Mark a fair measure? It exists for every card, so I can compare across years. It's synthetic, so I checked one pair against real games: 19 percent on paper, about 5 in practice. What about DLSS and ray tracing? I didn't measure them. They're Nvidia strengths that my value numbers leave out. Why September 2026 prices? They were current when I collected them, prices move fast, and two still need checking. And what would I do differently? [Your answer. For example, collect prices on several dates, add the missing cards to my main data, and time real games myself.]

## Slide 60: What my data cannot show

Here's what my data can't show. Several tiers hold only one or two cards, so my tier results are patterns, not proof. My own prices are one September 2026 snapshot, and two still need checking. G3D Mark and 3DMark are different scores, so I never combine them, and AMD cards score relatively higher on 3DMark. The benchmark file has very few priced cards after 2019, just 31 of 506 from 2020 to 2022, and the price history only covers late 2022 to 2024, so there is a thin stretch in the middle, and only my own data covers the newest cards. I only looked at gaming, not rendering or AI. And I checked synthetic scores against real games for one pair, not all of them.

## Slide 61: Conclusions and takeaways

Here's what the data told me. One, value is close overall: 0.0243 for AMD and 0.0259 for Nvidia, with no blowout winner in any tier. Two, AMD's clearer edge is memory per dollar, between 300 and 999 dollars. Three, the newest cards cost the most over launch price, 27 percent for AMD and 50 percent for Nvidia on average. Four, match the benchmark to the use, because a synthetic score showed 19 percent where real games showed 5. What I learned is to cross-check results across tools, say what a sample can't show, and match the measure to the use.

## Slide 62: Next steps

Next steps for the project. I'd add productivity workloads like rendering and AI, for the other audiences on my planning board. I'd pull 2025 and 2026 price history automatically with an API or web scraping. I'd test CPU and GPU pairings for bottlenecks, and add the missing cards to my main data as flagged rows, with one price rule and a top tier. And I'd look at used prices, since used Nvidia cards looked more heavily discounted in the December 2024 data. For my career, [say the roles you're applying for, the skills you want to deepen, and where people can find your work, like your GitHub and Tableau Public link].

## Slide 63: My budget: what had to fit

Now to the decision. My whole PC cost 2,200 dollars, with a 7800X3D, an RX 9070 XT, 64 gigabytes of DDR5-6000 memory, and 2 terabytes of storage. [Confirm whether that's before or after tax.] The CPU and GPU took about 1,148 dollars of it, and everything else, memory, storage, board, cooler, power supply and Windows, took about 1,051. What I needed was to play at 1080p now with headroom for a 1440p monitor later, 16 gigabytes of VRAM, and room to upgrade cooling, memory and the motherboard later, inside a budget of [about 2,250 dollars before tax]. So the question is: what's the best CPU and GPU that fits inside this?

## Slide 64: What if I had spent differently?

Here's the swap test. I hold the rest of the PC fixed and change only the graphics card. An RTX 5080 would push the PC to about 2,900 dollars. The RTX 5070 Ti, to about 2,600. The RX 7900 XTX, to about 2,400, and the RTX 5070 to about 2,380, which is 180 more than my pick. Below my pick, the RX 7900 XT would save about 100 dollars and the RTX 4070 about 210. So cards above my pick add 50 to 700 dollars, and cards below it save about 100 to 210. The next slide checks what each trade is worth in real games.

## Slide 65: What real games say about the cards that fit

For each card near my pick, I used reviews of real games, not the synthetic score. The RTX 5070 Ti is within about 5 percent of the 9070 XT. TechSpot's 55 games had it 5 percent ahead, and KitGuru's tests had the 9070 XT 6 percent ahead. The RX 7900 XT is last generation with 20 gigabytes. Tech4Gamers measured the 9070 XT 6 to 14 percent faster in three games, though TechSpot found it mixed. Comparison sites put the 9070 XT 11 to 14 percent ahead of the RTX 4070 Super, and the plain 4070 is slower still. And Tom's Hardware called the matchup with the RTX 5070 lopsided in the 9070 XT's favor. One note: on the synthetic score, the 9070 XT looks level with the 4070 and behind the 7900 XT. Real games disagree, so I used real games for this decision. [Cite each source.]

## Slide 66: Why the 7800X3D, not the 9800X3D

Why the 7800X3D and not the 9800X3D? The 9800X3D is faster, but in games the gap is about 8 percent at 1080p with a top-end graphics card, about 3 percent at 1440p, and about the same at 4K. The 7800X3D costs between 320 and 375 dollars, and I use 349, against about 449 for the 9800X3D. So the 9800X3D would add about 75 to 130 dollars for a gap of about 8 percent at most. Those tests used the fastest graphics cards, so with my RX 9070 XT the gap is likely smaller. That's my inference, not a measurement. I kept that money in the build, so I have room to upgrade cooling, memory and the motherboard later. [Cite TechSpot, Tech4Gamers and TechPowerUp.]

## Slide 67: My choice: the best fit for my budget

So here's what I chose: a Ryzen 7 7800X3D and a Radeon RX 9070 XT, with 64 gigabytes of DDR5-6000 and 2 terabytes of storage, in a 2,200 dollar PC. It fits. The PC is under my [2,250 dollar before-tax] budget, and the next step up in graphics cards, the RTX 5070 Ti, would add about 400 dollars for a gap of 5 percent or less in real games. The GPU is the fastest current-generation card I priced that fits, about 11 to 14 percent ahead of the RTX 4070 Super. The CPU is about 8 percent behind the 9800X3D at 1080p, for 75 to 130 dollars less. And there's room to grow: 16 gigabytes of VRAM, 64 gigabytes of memory, and budget to upgrade cooling, memory and the motherboard later. A different budget or use could lead to a different choice. For my 2,200 dollars, this was the best fit.

## Slide 68: I chose the Ryzen 7 7800X3D and the Radeon RX 9070 XT.

So, to answer the question I started with: I didn't look for the brand that wins everything. I looked for the best CPU and GPU that fit my budget, and I checked each alternative against real games. For my budget, the Ryzen 7 7800X3D and the Radeon RX 9070 XT gave me the fastest current-generation graphics card I could fit, a gaming CPU within a few percent of the 9800X3D, plenty of memory and storage, and room to upgrade. Thank you. I'm happy to take questions. [Add your name and contact details.]
