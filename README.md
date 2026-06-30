# 📊 Trading Data Analyzer

A terminal-based Python application that analyzes trading performance using **Pandas** for data processing and **Matplotlib** for visualization. Turn raw trade history into actionable insights.

---

## 🚀 Features

- ✅ Load and display trading data from CSV
- ✅ Calculate key statistics (total, average, best/worst trade)
- ✅ Group and visualize profit/loss per trading pair with bar chart
- ✅ Win rate analysis (win/loss count and percentage)
- ✅ Clean menu-driven terminal interface
- ✅ Error handling for missing data files

---

## 📸 Preview

```
==============================
   TRADING DATA ANALYZER
==============================
1. View All Trades
2. Show Statistics Summary
3. Profit/Loss per Pair (with Chart)
4. Win Rate Analysis
5. Exit
==============================
Choose menu (1-5): 2

📈 --- STATISTICS SUMMARY ---
Total Profit/Loss : 230
Average PNL       : 23.00
Best Trade (🏆)   : 80
Worst Trade (💀)  : -25
```

```
Choose menu (1-5): 4

🎯 --- WIN RATE ANALYSIS ---
Total Trades  : 10
Wins          : 6 ✅
Losses        : 4 ❌
Win Rate      : 60.0%
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Data Format | CSV |
| Interface | Terminal / Command Line |

---

## ⚙️ How to Use

**1. Clone this repository:**
```bash
git clone https://github.com/aryawirawicaksana029-ui/trading-data-analyzer.git
cd trading-data-analyzer
```

**2. Install dependencies:**
```bash
pip install pandas matplotlib
```

**3. Prepare your data:**

Create a `trading_data.csv` file with the following format:

```csv
date,pair,position,profit_loss
2026-06-01,BTCUSDT,LONG,50
2026-06-02,ETHUSDT,SHORT,-20
2026-06-03,BTCUSDT,LONG,80
```

**4. Run the program:**
```bash
python analyzer.py
```

---

## 📋 Menu Options

| Option | Description |
|--------|-------------|
| 1 | View all trade records in a formatted table |
| 2 | Display total, average, best, and worst trade |
| 3 | Group profit/loss by trading pair with bar chart |
| 4 | Calculate win rate percentage |
| 5 | Exit the program |

---

## 📊 Data Structure

| Column | Type | Description |
|--------|------|-------------|
| `date` | string | Date of the trade |
| `pair` | string | Trading pair (e.g. BTCUSDT) |
| `position` | string | LONG or SHORT |
| `profit_loss` | number | Profit (positive) or loss (negative) in USDT |

---

## 🧠 Key Pandas Concepts Used

```python
pd.read_csv()           # Load CSV into a DataFrame
df["col"].sum()         # Sum all values in a column
df["col"].mean()        # Calculate average
df.groupby("pair")      # Group data by category
df[df["col"] > 0]       # Filter rows by condition
```

---

## 📁 Project Structure

```
trading-data-analyzer/
│
├── analyzer.py          # Main program with analysis functions
├── trading_data.csv     # Sample trading data
└── README.md            # Project documentation
```

---

## 👨‍💻 Author

**Arya Wira Wicaksana**
🐍 Python Developer | AI Enthusiast
📧 aryawirawicaksana029@gmail.com
🔗 [GitHub](https://github.com/aryawirawicaksana029-ui)

---

## 🔮 Future Plans

- [ ] Import data directly from Binance API
- [ ] Monthly/weekly performance breakdown
- [ ] Risk-to-reward ratio analysis
- [ ] Export analysis report to PDF
- [ ] Web dashboard version with Streamlit
- [ ] Equity curve visualization
