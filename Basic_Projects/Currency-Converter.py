import requests

API_KEY = 'b826b425eed2c9c7e89bad27'

# Function to fetch exchange rates from the API
def get_exchange_rate(api_key, base_currency, target_currencies):
   
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rates = data['conversion_rates']
        return {currency: rates[currency] for currency in target_currencies if currency in rates}
    else:
        print('Error:', data.get('error', 'Unknown error'))
        return None

# Function to convert currency based on exchange rate
def convert_currency(amount, exchange_rate):

    return amount * exchange_rate

# Main function to run the currency converter program
def main():
    
    while True:
        base_currency = input("Enter the base currency (e.g., USD): ").upper()
        target_currencies = input("Enter the target currencies (comma-separated, e.g., INR,GBP): ").upper().split(',')
        amount = float(input(f"Enter the amount in {base_currency}: "))
        
        exchange_rates = get_exchange_rate(API_KEY, base_currency, target_currencies)
        
        if exchange_rates:
            for target_currency in target_currencies:
                if target_currency in exchange_rates:
                    exchange_rate = exchange_rates[target_currency]
                    converted_amount = convert_currency(amount, exchange_rate)
                    print(f'{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency} at an exchange rate of {exchange_rate:.4f}')
                else:
                    print(f"Exchange rate for {target_currency} not available.")
        else:
            print("Failed to retrieve exchange rates.")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

if __name__ == '__main__':
    main()
input()