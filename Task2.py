# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Enter stock symbols and quantity (type 'done' to finish)\n")
# Input loop
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc. OR type DONE for program end ) : ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Display and calculate
print("\n💼 Investment Summary:")
lines = ["Stock,Quantity,Price,Total Value"]
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} × ${price} = ${value}")
    lines.append(f"{stock},{qty},{price},{value}")

print(f"\n🧾 Total Investment Value: ${total_investment}")
lines.append(f"\nTotal Investment Value: ${total_investment}")

# Always save to file
filename = "portfolio.txt"
try:
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ Portfolio saved to '{filename}'")
except Exception as e:
    print(f"❌ Error saving file: {e}")
