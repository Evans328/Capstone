NEW AND UPDATED FILES: unzip these straight into your capstone folder, next to your old files.

WHEN YOUR COMPUTER ASKS "REPLACE?", SAY YES FOR THESE THREE (they are corrected versions of files you already have):
  gpu_tableau_ready.csv      premium column fixed for the RTX 4070
  build_combinations.csv     last row is now the Ryzen 7 7800X3D build
  budget_tier_builds.csv     corrected $800 row, and my build

EVERYTHING ELSE IS NEW (nothing of yours is overwritten):
  scrape_launch_prices.py        web scraper that checks the MSRP column against Wikipedia
  hardware_data_corrected.csv    hardware_data.csv with the RTX 4070 launch price fixed to $599
  new_chart_cells.py             notebook cells for the new charts
  cpu_data_clean.csv             clean CPU file, includes the 7800X3D
  other_cards_supplement.csv     RTX 5060 Ti, RTX 5090 and Arc B580, with price ranges and sources
  tableau_funnel.csv, tableau_pairs.csv, tableau_swap_test.csv, tableau_median_by_year.csv   small files for Tableau charts
  tableau_story_plan.md          the Tableau story, point by point
  presentation_script.md         the spoken script, one section per slide
  tableau_images/                chart images and the pipe analogy (the only subfolder; drag them out if you prefer)

DO THIS IN ORDER
1. Run scrape_launch_prices.py against your CURRENT hardware_data.csv (the old one, RTX 4070 at $549).
   It should print "15 of 16 launch prices match". Screenshot it for the scraping slide.
   Nothing in this zip overwrites hardware_data.csv, so your old copy is safe until you are ready.
2. THEN replace hardware_data.csv with hardware_data_corrected.csv (delete the old one, rename the new one).
   Rerun your notebook. In SQL: UPDATE hardware_data SET MSRP_Price = 599 WHERE Full_Model_Name = 'GeForce RTX 4070';
   In Excel: change the RTX 4070 MSRP cell to 599.
3. Tableau: follow tableau_story_plan.md. Switch Sum to Average on per-card and per-month values.
   Your existing Tableau connections keep working, because the files stay in the same place.
4. Not included, because you already have them and they did not change: gpu_price_history_tableau.csv,
   synthetic_vs_real_gap.csv, GPU_benchmarks_v7.csv, gpu_metadata.csv, gpu_price_history.csv.
   The chart cells read the three Kaggle files, so keep them in the same folder as your notebook.
