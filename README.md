# 🚴 2024 Olympic Cycling Data Cleaning & Processing

An automated Python data-pipeline designed to extract, clean, and structure rider standings from the 2024 Paris Olympics Cycling dataset and export formatted analytical reports to Excel.

## 📌 Project Overview
Raw sports standings often contain unstructured string columns combining rider names, team details, and country codes. This project automates the extraction and cleaning workflow using **Python, Pandas, and Regular Expressions (Regex)**, outputting clean structured data ready for analysis.

## 🛠️ Key Technical Features
* **Regex Pattern Extraction:** Uses `str.extract(r"\((.*?)\)")` to accurately parse 3-letter country codes (e.g., `BEL`, `ITA`, `SLO`).
* **Data Standardization:** Strips inline parenthetical strings and trailing whitespace to isolate standard `Rider Name` values.
* **Automated Data Export:** Direct output processing to formatted `.xlsx` files using `Pandas` and `OpenPyXL`.

## 💻 Code Architecture (`main.py`)
```python
import pandas as pd

# Data Ingestion
df = pd.DataFrame(data)

# Regex Parsing & Data Cleaning
df["Rider Name"] = df["Rider"].str.replace(r"\s*\(.*\)", "", regex=True).str.strip()
df["Country"] = df["Rider"].str.extract(r"\((.*?)\)")
df["Team"] = df["Team"].str.strip()

# Excel Report Generation
df.to_excel("Olympics_Cycling_2024_Cleaned.xlsx", index=False)
