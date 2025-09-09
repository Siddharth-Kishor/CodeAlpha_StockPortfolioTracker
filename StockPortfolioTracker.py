import csv

stock_prices = {
    "APLE" : 180,
    "TSLA" : 250,
    "GOGL" : 2750,
    "AMZN" : 3100,
    "MSFT" : 390,
    "NVDA" : 3250
}

def calculate_total_investment(stocks_owned):
    total_value = 0
    for stock, quantity in stocks_owned.items():
        if stock in stock_prices:
            total_value += stock_prices[stock] * quantity
        else:
            print(f"Warning: Stock {stock} not found in the price list.")
    return total_value

def save_to_file(total_value, filename="portfolio.txt"):
    with open(filename, "w") as file:
        file.write(f"Total Investment Value: ${total_value:.2f}\n")
    print(f"Result saved to {filename}")

def save_to_csv(stocks_owned, total_value, filename="portfolio.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, quantity in stocks_owned.items():
            if stock in stock_prices:
                writer.writerow([stock, quantity, stock_prices[stock], stock_prices[stock] * quantity])
        writer.writerow(["", "", "Total Investment", total_value])
    print(f"Result saved to {filename}")

def main():
    stocks_owned = {}
    print("\nEnter your stock portfolio. Type 'done' when you are finished.")
    while True:
        print()
        stock = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print(f"Stock {stock} not found in our price list. Please try again.")
            continue
        
        try:
            quantity = int(input(f"How many shares of {stock} do you own? "))
        except ValueError:
            print("Please enter a valid integer for quantity.")
            continue
        
        stocks_owned[stock] = quantity
    
    total_investment = calculate_total_investment(stocks_owned)
    print(f"\nTotal Investment Value: ${total_investment:.2f}")
    
    save_option = input("\nDo you want to save the result to a file? (txt/csv/none): ").lower()
    if save_option == "txt":
        save_to_file(total_investment)
    elif save_option == "csv":
        save_to_csv(stocks_owned, total_investment)
    else:
        print("Result not saved to a file.")

if __name__ == "__main__":
    main()
