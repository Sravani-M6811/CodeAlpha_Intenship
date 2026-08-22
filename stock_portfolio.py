stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, "=", "$" + str(price))

print("\nEnter the stocks you want to buy.")
print("Type 'done' when finished.")

while True:
    stock = input("\nEnter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid number.")

print("\n================================")
print("          PORTFOLIO")
print("================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(
        stock,
        "- Quantity:",
        quantity,
        "- Price: $",
        price,
        "- Value: $",
        value
    )

    total_investment += value

print("\nTotal Investment: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock} - Quantity: {quantity} - "
            f"Price: ${price} - Value: ${value}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")