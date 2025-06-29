# stock-portfolio-tracker
A beginner-friendly Python console app to track stock investments. Users enter stock symbols and quantities, and the app calculates total value using hardcoded prices. It displays a summary and saves it to portfolio.txt. Great for learning input handling, loops, and file writing in Python.
# 📊 Stock Portfolio Tracker (Python Console App)

A simple Python script that lets users **track their stock investments** by entering stock symbols and quantities. The app calculates total investment value based on hardcoded prices and **saves a summary to a text file** (`portfolio.txt`).

---

## ✅ Features

- 🧮 Calculate total investment value based on predefined stock prices
- 🗃️ Auto-saves summary as a CSV-formatted `.txt` file
- 🔁 Supports multiple entries of the same stock symbol
- 📉 Input validation with user-friendly error messages
- 🖥️ Console-based; no external dependencies

---

## 💼 How It Works

1. User is prompted to enter stock symbols (e.g., `AAPL`, `GOOGL`).
2. For each symbol, the user enters a quantity.
3. The app multiplies quantity × price and shows total investment.
4. Typing `DONE` ends the program and writes the summary to `portfolio.txt`.

---

## 🧪 Example

```text
📊 Stock Portfolio Tracker
Enter stock symbols and quantity (type 'done' to finish)

Enter stock symbol (AAPL, TSLA, etc. OR type DONE for program end ) : AAPL
Enter quantity of AAPL: 5
Enter stock symbol (AAPL, TSLA, etc. OR type DONE for program end ) : TSLA
Enter quantity of TSLA: 3
Enter stock symbol (AAPL, TSLA, etc. OR type DONE for program end ) : DONE

💼 Investment Summary:
AAPL: 5 × $180 = $900
TSLA: 3 × $250 = $750

🧾 Total Investment Value: $1650
✅ Portfolio saved to 'portfolio.txt'

🧑‍💻 Author
Developed by Malik Kamran Ali
