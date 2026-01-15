# 🏎️ Formula 1 Driver Performance Analysis (2025)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![FastF1](https://img.shields.io/badge/FastF1-Latest-red.svg)](https://github.com/theOehrly/Fast-F1)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A comprehensive performance analysis of Max Verstappen, Lando Norris, and Oscar Piastri during the 2025 Formula 1 season, utilizing race telemetry data and advanced analytics.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Data Source](#-data-source)
- [Tools & Technologies](#️-tools--technologies)
- [Analysis & Insights](#-analysis--insights)
- [Visualizations](#-visualizations)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Key Findings](#-key-findings)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

This project moves beyond traditional championship standings to provide an in-depth analysis of driver performance throughout the 2025 F1 season. By leveraging official FIA timing data and telemetry, the analysis explores:

- **Performance trends** across the season
- **Championship battle dynamics**
- **Speed and consistency metrics**
- **Strategic impact** on race outcomes
- **Race pace analysis**

The project demonstrates professional data engineering practices, from data extraction to interactive visualization in Power BI.

---

## ✨ Key Features

- 📊 **Comprehensive Data Pipeline**: Automated data extraction using FastF1 API
- 🔄 **ETL Process**: Clean, structured data transformation with pandas
- 📈 **Advanced Analytics**: DAX measures and calculated columns in Power BI
- 🎨 **Interactive Dashboards**: Professional visualizations with drill-through capabilities
- 🏁 **Race-by-Race Analysis**: Lap times, positions, pit stops, and performance metrics
- 🔍 **Driver Comparison**: Head-to-head performance across multiple dimensions

---

## 📊 Data Source

Official Formula 1 timing and telemetry data accessed through the **FastF1 Python library**, including:

| Data Type | Description |
|-----------|-------------|
| **Lap Times** | Individual lap performance for all sessions |
| **Race Positions** | Position changes throughout each race |
| **Fastest Laps** | Quickest lap times per driver per race |
| **Championship Points** | Official FIA points allocation |
| **Pit Stop Data** | Timing and strategy information |
| **Tire Compounds** | Tire selection and performance impact |

---

## 🛠️ Tools & Technologies

<div align="center">

| Technology | Purpose |
|:----------:|:-------:|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Data extraction & processing |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data manipulation |
| ![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) | Visualization & modeling |
| ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) | Version control |

</div>

### Core Libraries

```python
fastf1==3.0+      # F1 data access
pandas==2.0+      # Data manipulation
numpy==1.24+      # Numerical operations
```

---

## 📈 Analysis & Insights

### Analytical Dimensions

1. **Performance Trends**
   - Cumulative points progression
   - Race-by-race performance evolution
   - Mid-season momentum shifts

2. **Speed Analysis**
   - Fastest lap comparisons
   - Average race pace
   - Top speed metrics

3. **Consistency Metrics**
   - Performance volatility
   - Finish position variance
   - Reliability assessment

4. **Strategic Impact**
   - Pit stop effectiveness
   - Tire strategy analysis
   - Race outcome correlations

---

## 🎨 Visualizations

### Individual Driver Performance Dashboards

<details>
<summary><b>Oscar Piastri - Performance Analysis</b></summary>

![Oscar Piastri Analysis](visuals/oscar_piastri_dashboard.png)

**Key Metrics:**
- Total Points: **381**
- Average Finish Position: **4th**
- Average Lap Time: **89.11s**
- World Titles: **0**

</details>

<details>
<summary><b>Lando Norris - Performance Analysis</b></summary>

![Lando Norris Analysis](visuals/lando_norris_dashboard.png)

**Key Metrics:**
- Total Points: **394**
- Average Finish Position: **4th**
- Average Lap Time: **89.66s**
- World Titles: **1** 🏆

</details>

<details>
<summary><b>Max Verstappen - Performance Analysis</b></summary>

![Max Verstappen Analysis](visuals/max_verstappen_dashboard.png)

**Key Metrics:**
- Total Points: **389**
- Average Finish Position: **4th**
- Average Lap Time: **90.82s**
- World Titles: **4** 🏆

</details>

### Comparative Analysis

<details>
<summary><b>Head-to-Head Performance Comparison</b></summary>

![Driver Comparison](visuals/driver_comparison_dashboard.png)

**Comparative Insights:**
- Fastest lap competition across all races
- Finish position trends and variability
- Total points accumulation
- Average top speed analysis

</details>

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Power BI Desktop (latest version)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/f1-performance-analysis-2025.git
   cd f1-performance-analysis-2025
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Enable FastF1 cache** (optional but recommended)
   ```python
   import fastf1
   fastf1.Cache.enable_cache('path/to/cache')
   ```

---

## 💻 Usage

### Data Extraction

```bash
# Run the data extraction script
python scripts/fastf1_data_extraction.py
```

This will:
- Download race data for the 2025 season
- Process telemetry and timing information
- Export cleaned data to `data/processed_race_data.csv`

### Power BI Analysis

1. Open `powerbi/F1_2025_Analysis.pbix`
2. Refresh data sources if needed
3. Navigate through dashboard pages:
   - **Overview**: Season summary and key metrics
   - **Driver Analysis**: Individual performance deep-dives
   - **Race Comparison**: Head-to-head by circuit
   - **Trends**: Performance evolution over time

---

## 📂 Project Structure

```
f1-performance-analysis-2025/
│
├── data/
│   ├── raw/                          # Raw data from FastF1
│   └── processed_race_data.csv       # Cleaned dataset
│
├── scripts/
│   ├── fastf1_data_extraction.py     # Data extraction script
│   ├── data_processing.py            # Data cleaning & transformation
│   └── utils.py                      # Helper functions
│
├── powerbi/
│   └── F1_2025_Analysis.pbix         # Power BI dashboard
│
├── visuals/
│   ├── oscar_piastri_dashboard.png
│   ├── lando_norris_dashboard.png
│   ├── max_verstappen_dashboard.png
│   └── driver_comparison_dashboard.png
│
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
└── LICENSE                           # MIT License
```

---

## 🔍 Key Findings

### 🏆 Championship Battle Summary

> **Lando Norris** leads in total points despite having the most DNFs, driven by consistent top 4 finishes and the highest average speed (273 km/h).

### 📊 Performance Insights

| Driver | Strength | Area for Improvement |
|--------|----------|---------------------|
| **Lando Norris** | Consistent podiums, highest top speed | Reliability (most DNFs) |
| **Max Verstappen** | Strong reliability, mid-season surge | Average lap time |
| **Oscar Piastri** | Peak performance capability | Consistency across races |

### 🎯 Detailed Analysis

- **Max Verstappen** demonstrates strong reliability with only one retirement, showing a clear performance resurgence after Hungary, competing consistently in the top 3 until season's end while dominating most fastest laps.

- **Oscar Piastri** displays the most volatility, capable of top performance in select races but lacking the consistency of his competitors throughout the season.

- **Strategic Excellence**: Tire change ratios reveal distinct strategic approaches, with varying impacts on race outcomes across different circuit types.

---

## 📌 Notes

- This project prioritizes **analytical accuracy** over purely aesthetic visuals
- KPI cards were intentionally avoided in favor of **trend-based and distribution-based visualizations**
- All insights are **data-driven**, derived from official race telemetry
- The analysis focuses on **objective performance metrics** rather than subjective opinions

---

## 👤 Author

**Hasan Shinnar**

🎓 Computer Information Systems Graduate  
💼 Aspiring Data Analyst / Data Engineer  
🏎️ Formula 1 Motorsport Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hasan-shinnar)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hasanshinnar)

---

## 🙏 Acknowledgments

- [FastF1](https://github.com/theOehrly/Fast-F1) for providing access to F1 data
- Formula 1 and FIA for official timing data
- The F1 analytics community for inspiration

---

<div align="center">

### ⭐ If you found this project interesting, please consider giving it a star!

**Built with ❤️ and ☕ by Hasan Shinnar**

</div>
