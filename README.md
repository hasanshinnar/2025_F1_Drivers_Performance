#🏎️ Formula 1 Driver Performance Analysis (2025)
#📌 Project Overview

This project analyzes and compares the 2025 Formula 1 season performance of Max Verstappen, Lando Norris, and Oscar Piastri using real race data.
The goal is to move beyond simple standings and explore performance trends, consistency, race pace, and strategic impact throughout the season.

The analysis is built using Python (FastF1) for data extraction and processing, and Power BI for modeling, visualization, and storytelling.

#🎯 Objectives

Analyze season-long performance trends for top drivers

Identify turning points during the championship battle

Compare speed, consistency, and race outcomes

Demonstrate professional data modeling and visualization practices

#🛠️ Tools & Technologies

Python

fastf1

pandas

Power BI

Data modeling (Star Schema)

DAX measures

Advanced visual comparisons

GitHub (version control & documentation)

#📊 Data Source

Official Formula 1 timing and telemetry data via the FastF1 Python library

Race-level and lap-level data, including:

Lap times

Positions

Pit stops

Fastest laps

Points

#🧱 Data Model

The project follows a Star Schema design:

FactLaps

Lap-level performance data

DimRace

Race name, round number, event date

DimDriver

Driver metadata

This structure ensures:

Correct aggregation levels

Accurate comparisons between drivers

Proper chronological sorting of races

#📈 Key Analyses & Visuals

Cumulative Points Progression
Shows how the championship battle evolved round by round.

Fastest Lap & Average Speed Comparison
Highlights raw pace differences between drivers.

Consistency Analysis
Evaluates performance volatility across races.

Race Outcome Distribution
Wins, podiums, DNFs, and lower finishes.

Pit Strategy Impact
Relationship between pit stops and race results.

#🔍 Key Insights

Lando Norris leads in total points despite having the most DNFs, driven by consistent top-4 finishes and the highest average speed.

Max Verstappen demonstrates strong reliability and a clear performance resurgence after mid-season, competing consistently in the top 3.

Oscar Piastri shows high peak performance but the greatest variability across races.

#📂 Repository Structure
├── data/
│   └── processed_race_data.csv
├── scripts/
│   └── fastf1_data_extraction.py
├── powerbi/
│   └── F1_2025_Analysis.pbix
├── visuals/
│   └── dashboard_screenshots/
└── README.md

#🚀 How to Run

Install dependencies:

pip install fastf1 pandas


Enable FastF1 cache and run the data extraction script.

Load the processed CSV into Power BI.

Refresh the model and explore the dashboards.

#📌 Notes

This project focuses on analytical accuracy, not just visual appeal.

KPI cards were intentionally avoided in favor of trend-based and distribution-based visuals.

All insights are derived from race data, not subjective opinions.

# 👤 Author

Hasan Shinnar
Computer Information Systems Graduate
Aspiring Data Analyst / Data Engineer
Interested in motorsport analytics and performance analysis
