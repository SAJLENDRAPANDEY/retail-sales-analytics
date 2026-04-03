# 📊 Retail Sales Analytics Pipeline

> An end-to-end data analytics project that transforms raw multi-table retail sales data into actionable business insights using Python, KPI analysis, and data visualization.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-orange?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-76b900?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

---

## 👨‍💻 Author

**Sajlendra Pandey** — B.Tech CSE (Data Science)

[![GitHub](https://img.shields.io/badge/GitHub-SAJLENDRAPANDEY-181717?style=flat&logo=github)](https://github.com/SAJLENDRAPANDEY)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sajlendra%20Pandey-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/sajlendra-pandey-37378627b/)

---

## 🎯 Project Objective

Analyze a multi-table retail dataset to uncover revenue trends, evaluate product and store performance, and support data-driven business decisions — all through a clean, modular Python pipeline.

---

## ❓ Key Business Questions Answered

- Does discounting lead to profit loss?
- Which products generate the highest revenue vs profit margin?
- Which countries and store types dominate revenue?
- What is the relationship between revenue and profit?
- Which product categories are most profitable?

---

## 🗂️ Project Structure

```
retail-sales-analytics/
│
├── sales_analytics.py       # Main analysis pipeline
├── README.md                # Project documentation
│
└── data/                    # Source Excel files (not tracked by Git)
    ├── sales data.xlsx
    ├── customer data.xlsx
    ├── product data.xlsx
    ├── store data.xlsx
    └── calendar.xlsx
```

---

## 🔍 Pipeline Overview

| Stage | Description |
|---|---|
| **1. Data Loading** | Reads 5 Excel source files — sales, product, customer, store, calendar |
| **2. Data Merging** | Joins all dimension tables onto the central sales fact table |
| **3. Data Cleaning** | Drops duplicates and removes artefact columns |
| **4. Feature Engineering** | Creates `profit_flag`, `profit_margin`, and `month` features |
| **5. KPI Summary** | Prints revenue, profit, margins, and business rankings |
| **6. Visualization** | Generates 9 charts covering trends, rankings, and correlations |

---

## 📈 KPIs Reported

- Total Revenue & Total Profit
- Average Profit per Order & Average Profit Margin
- Country-wise Revenue Ranking
- Top 5 Products by Profit Margin
- Store Performance Ranking
- Top Brand by Quantity Sold
- Highest Profit Country

---

## 📊 Charts Generated

| # | Chart | Type |
|---|---|---|
| 1 | Revenue by Country | Bar |
| 2 | Monthly Revenue Trend | Line |
| 3 | Monthly Profit Trend | Line |
| 4 | Profit by Category | Bar |
| 5 | Top 5 Products by Revenue | Bar |
| 6 | Revenue by Store Type | Bar |
| 7 | Discount vs Profit | Scatter |
| 8 | Revenue vs Profit | Scatter |
| 9 | Profit Distribution across Discount Levels | Box Plot |

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Core language |
| Pandas | 2.0+ | Data manipulation & analysis |
| NumPy | 1.24+ | Vectorised feature engineering |
| Matplotlib | 3.7+ | Chart rendering |
| Seaborn | 0.12+ | Statistical visualizations |
| OpenPyXL | 3.1+ | Excel file reading |

---

## 📂 Dataset

Due to GitHub file size limitations, the dataset is **not included** in this repository.
Download all required files from the Google Drive link below:

> 🔗 **[Download Dataset from Google Drive](https://drive.google.com/drive/folders/1HMao00qE4BupNhH9PRH-ld50plhDkShw?usp=drive_link)**

| File | Description |
|---|---|
| `sales data.xlsx` | Core transaction records |
| `customer data.xlsx` | Customer demographics |
| `product data.xlsx` | Product catalogue |
| `store data.xlsx` | Store details |
| `calendar.xlsx` | Date dimension table |

---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/SAJLENDRAPANDEY/retail-sales-analytics.git
cd retail-sales-analytics
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### 3. Download & place the dataset
Download all files from the **[Google Drive link](https://drive.google.com/drive/folders/1HMao00qE4BupNhH9PRH-ld50plhDkShw?usp=drive_link)**, create a `data/` folder in the project directory, and place all `.xlsx` files inside it.

### 4. Run the pipeline
```bash
python sales_analytics.py
```

---

## 💡 Key Business Insights

- **Discounting hurts margins** — lower discount strategies consistently produce higher profit margins.
- **Revenue ≠ Profitability** — several high-revenue products rank lower on profit margin.
- **Geographic concentration** — a few countries generate a disproportionately large share of total revenue.
- **Stable pricing** — no loss-making products were identified, indicating healthy cost control across the catalogue.
- **Airport stores lead** — airport store type generates the highest revenue among all store types.

---

## 🧠 Skills Demonstrated

- Data Cleaning & Preprocessing
- Multi-table Data Merging
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Business KPI Analysis
- Data Visualization (Matplotlib & Seaborn)
- Data-driven Decision Making

---

## 🚀 Future Improvements

- [ ] Interactive dashboard with **Streamlit** or **Power BI**
- [ ] Live data pipeline from **MySQL / PostgreSQL**
- [ ] Sales forecasting using **ARIMA / Prophet**
- [ ] Unit tests with **pytest**
- [ ] Docker containerization for reproducibility

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
