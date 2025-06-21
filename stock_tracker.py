def main():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "AMZN": 3500, "MSFT": 300}
    portfolio = {}
    total_investment = 0

    print("Welcome to Stock Portfolio Tracker!")
    print("Enter stock name and quantity (type 'done' to finish):")

    while True:
        stock = input("Stock Symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not in list. Available stocks:", ', '.join(stock_prices.keys()))
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("========================\n")
        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            total_investment += investment
            summary_line = f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}"
            print(summary_line)
            file.write(summary_line + "\n")

        total_line = f"\nTotal Investment: ${total_investment}"
        print(total_line)
        file.write(total_line)

    print("\nPortfolio summary saved to 'portfolio_summary.txt'.")

if __name__ == "__main__":
    main()
