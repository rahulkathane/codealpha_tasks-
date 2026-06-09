"""
╔══════════════════════════════════════════════════════════════╗
║           STOCK PORTFOLIO TRACKER — CodeAlpha Task 2         ║
║  • Enter stock symbols and quantities                        ║
║  • View real-time portfolio value & summary                  ║
║  • Save results to .txt or .csv                              ║
╚══════════════════════════════════════════════════════════════╝
Key concepts: dictionary, input/output, arithmetic, file handling
"""

import csv
import os
from datetime import datetime

# ── Hardcoded stock price dictionary (price in USD) ──────────────────────────
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple Inc.
    "TSLA":  250.00,   # Tesla Inc.
    "GOOGL": 140.00,   # Alphabet Inc.
    "MSFT":  380.00,   # Microsoft Corp.
    "AMZN":  185.00,   # Amazon.com Inc.
    "META":  500.00,   # Meta Platforms
    "NFLX":  650.00,   # Netflix Inc.
    "NVDA":  875.00,   # NVIDIA Corp.
    "RELIANCE": 28.00, # Reliance Industries (NSE, approx USD)
    "TCS":   45.00,    # Tata Consultancy Services (approx USD)
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def divider(char="─", width=55):
    print(char * width)


def show_available_stocks():
    """Print the catalogue of available stocks."""
    print("\n  Available Stocks:")
    divider()
    print(f"  {'Symbol':<12} {'Company / Description':<28} {'Price (USD)':>10}")
    divider()
    names = {
        "AAPL": "Apple Inc.", "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.", "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.", "META": "Meta Platforms",
        "NFLX": "Netflix Inc.", "NVDA": "NVIDIA Corp.",
        "RELIANCE": "Reliance Industries", "TCS": "Tata Consultancy Svc",
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<12} {names[symbol]:<28} ${price:>9.2f}")
    divider()


def get_portfolio_from_user() -> dict:
    """
    Interactively ask the user which stocks and quantities to add.
    Returns a dict  { 'AAPL': 10, 'TSLA': 5, ... }
    """
    portfolio = {}
    print("\n  Enter stock symbol and quantity (type 'done' when finished).")
    print("  Type 'list' to see available stocks.\n")

    while True:
        symbol = input("  Stock symbol : ").strip().upper()

        if symbol == "DONE":
            break
        if symbol == "LIST":
            show_available_stocks()
            continue
        if symbol == "":
            continue
        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found. Type 'list' to see options.\n")
            continue

        # Get quantity
        while True:
            qty_str = input(f"  Quantity for {symbol}: ").strip()
            if qty_str.isdigit() and int(qty_str) > 0:
                qty = int(qty_str)
                break
            print("  ⚠  Please enter a positive whole number.")

        # Accumulate (allow adding same stock multiple times)
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        price = STOCK_PRICES[symbol]
        print(f"  ✔  Added {qty} × {symbol} @ ${price:.2f} = ${qty * price:,.2f}\n")

    return portfolio


def display_portfolio(portfolio: dict) -> float:
    """Print a formatted portfolio table. Returns total value."""
    if not portfolio:
        print("\n  ⚠  Portfolio is empty — nothing to display.")
        return 0.0

    print("\n")
    divider("═")
    print("         PORTFOLIO SUMMARY")
    divider("═")
    print(f"  {'Symbol':<10} {'Qty':>6}  {'Price (USD)':>12}  {'Value (USD)':>13}")
    divider()

    total = 0.0
    for symbol, qty in sorted(portfolio.items()):
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<10} {qty:>6}  ${price:>11,.2f}  ${value:>12,.2f}")

    divider()
    print(f"  {'TOTAL INVESTMENT':>30}   ${total:>12,.2f}")
    divider("═")
    print(f"\n  📊 You hold {len(portfolio)} stock(s) worth  ${total:,.2f}  USD total.\n")
    return total


def save_to_txt(portfolio: dict, total: float, filename: str) -> None:
    """Save portfolio summary to a plain-text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO TRACKER — Summary Report\n")
        f.write(f"Generated : {timestamp}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<10} {'Qty':>6}  {'Price':>10}  {'Value':>12}\n")
        f.write("-" * 50 + "\n")
        for symbol, qty in sorted(portfolio.items()):
            price = STOCK_PRICES[symbol]
            value = price * qty
            f.write(f"{symbol:<10} {qty:>6}  ${price:>9,.2f}  ${value:>11,.2f}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'TOTAL':<10}        {'':>10}  ${total:>11,.2f}\n")
    print(f"  ✅ Portfolio saved to '{filename}'.")


def save_to_csv(portfolio: dict, total: float, filename: str) -> None:
    """Save portfolio to a CSV file (opens in Excel / Sheets)."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Portfolio Tracker"])
        writer.writerow(["Generated", timestamp])
        writer.writerow([])
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for symbol, qty in sorted(portfolio.items()):
            price = STOCK_PRICES[symbol]
            value = price * qty
            writer.writerow([symbol, qty, f"{price:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
    print(f"  ✅ Portfolio saved to '{filename}'.")


def ask_save(portfolio: dict, total: float) -> None:
    """Ask the user if they want to save, and in which format."""
    print("  Save your portfolio?")
    print("  [1] Save as .txt")
    print("  [2] Save as .csv  (opens in Excel / Google Sheets)")
    print("  [3] Save both")
    print("  [4] Don't save\n")

    choice = input("  Your choice (1-4): ").strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"portfolio_{timestamp}"

    if choice in ("1", "3"):
        save_to_txt(portfolio, total, f"{base}.txt")
    if choice in ("2", "3"):
        save_to_csv(portfolio, total, f"{base}.csv")
    if choice == "4":
        print("  (Results not saved.)")
    if choice not in ("1", "2", "3", "4"):
        print("  ⚠  Invalid choice — skipping save.")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "═" * 55)
    print("      STOCK PORTFOLIO TRACKER  📈")
    print("      CodeAlpha Internship — Task 2")
    print("═" * 55)

    while True:
        show_available_stocks()

        portfolio = get_portfolio_from_user()

        if not portfolio:
            print("\n  No stocks entered. Exiting.")
            break

        total = display_portfolio(portfolio)
        ask_save(portfolio, total)

        again = input("\n  Track another portfolio? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thank you for using the Portfolio Tracker! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
