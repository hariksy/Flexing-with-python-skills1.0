from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")
    print("Enter the amount and the currencies to convert between.")
    print("Example: 100 USD EUR (converts 100 US Dollars to Euros)")

    while True:
        try:
            amount, from_currency, to_currency = input("\nEnter amount and currencies (e.g., 100 USD EUR): ").split()
            amount = float(amount)
            converted_amount = convert_currency(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except ValueError:
            print("Please enter a valid input.")
        except Exception as e:
            print(f"An error occurred: {e}")

        choice = input("\nDo you want to convert another amount? (y/n): ")
        if choice.lower() != 'y':
            break

    print("\nThank you for using the Currency Converter!")

if __name__ == "__main__":
    main()
