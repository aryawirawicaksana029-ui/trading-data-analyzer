import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Data loader function with error handling."""
    try:
        return pd.read_csv("trading_data.csv")
    except FileNotFoundError:
        print("❌ Oops, trading_data.csv not found! Make sure the file is in the same folder.")
        return None

def view_all_trades(df):
    """Display all trading records."""
    print("\n📊 --- ALL TRADE HISTORY ---")
    print(df.to_string(index=False))  # index=False to hide the 0,1,2 row numbers

def show_statistics(df):
    """Calculate basic statistics."""
    print("\n📈 --- STATISTICS SUMMARY ---")
    total = df["profit_loss"].sum()
    average = df["profit_loss"].mean()
    best = df["profit_loss"].max()
    worst = df["profit_loss"].min()

    print(f"Total Profit/Loss : {total}")
    print(f"Average PNL       : {average:.2f}")
    print(f"Best Trade (🏆)   : {best}")
    print(f"Worst Trade (💀)  : {worst}")

def profit_per_pair(df):
    """Group and summarize profit/loss per trading pair, plus chart visualization."""
    print("\n🪙 --- PROFIT/LOSS PER PAIR ---")
    summary = df.groupby("pair")["profit_loss"].sum()
    print(summary)

    print("\n[Displaying Matplotlib chart... Close the chart window to return to the menu]")
    # Build interactive bar chart
    summary.plot(kind="bar", color=["#F3BA2F", "#F0B90B", "#627EEA"])
    plt.title("Total Profit/Loss Per Trading Pair", fontsize=14, fontweight='bold')
    plt.xlabel("Trading Pair", fontsize=12)
    plt.ylabel("Profit / Loss (USDT)", fontsize=12)
    plt.axhline(0, color="red", linestyle="--", linewidth=1.5, label="Break Even")
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.show()

def win_rate(df):
    """Calculate win rate performance."""
    print("\n🎯 --- WIN RATE ANALYSIS ---")
    # Filter profitable trades (above 0) and losing trades (below 0)
    win_trades = df[df["profit_loss"] > 0]
    loss_trades = df[df["profit_loss"] < 0]

    # Count rows using .shape[0] or len()
    total_win = win_trades.shape[0]
    total_loss = loss_trades.shape[0]
    total_trades = len(df)

    # Correct percentage formula (multiply by 100, not 180! 😂)
    wr_percentage = (total_win / total_trades) * 100

    print(f"Total Trades  : {total_trades}")
    print(f"Wins          : {total_win} ✅")
    print(f"Losses        : {total_loss} ❌")
    print(f"Win Rate      : {wr_percentage:.1f}%")

def main():
    df = load_data()
    if df is None:
        return  # Stop if CSV file doesn't exist

    while True:
        print("\n" + "="*30)
        print("   TRADING DATA ANALYZER   ")
        print("="*30)
        print("1. View All Trades")
        print("2. Show Statistics Summary")
        print("3. Profit/Loss per Pair (with Chart)")
        print("4. Win Rate Analysis")
        print("5. Exit")
        print("="*30)

        choice = input("Choose menu (1-5): ")

        if choice == "1":
            view_all_trades(df)
        elif choice == "2":
            show_statistics(df)
        elif choice == "3":
            profit_per_pair(df)
        elif choice == "4":
            win_rate(df)
        elif choice == "5":
            print("\n👋 Program ended! Protect your trading psychology and always set a Stop Loss! 🚀")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()