import requests

# Replace with your ExchangeRate-API key
API_KEY = 'b826b425eed2c9c7e89bad27'

def get_exchange_rate(api_key, base_currency, target_currencies):
    """
    Fetch the exchange rates from ExchangeRate-API.
    
    Parameters:
        api_key (str): Your API key for ExchangeRate-API.
        base_currency (str): The base currency (e.g., USD).
        target_currencies (list): List of target currencies (e.g., ['EUR', 'JPY']).
    
    Returns:
        dict: A dictionary with target currencies as keys and exchange rates as values.
    """
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rates = data['conversion_rates']
        return {currency: rates[currency] for currency in target_currencies if currency in rates}
    else:
        print('Error:', data.get('error', 'Unknown error'))
        return None

def convert_currency(amount, exchange_rate):
    """
    Convert the amount based on the exchange rate.
    
    Parameters:
        amount (float): The amount to convert.
        exchange_rate (float): The exchange rate.
    
    Returns:
        float: The converted amount.
    """
    return amount * exchange_rate

def main():
    """
    Main function to run the currency converter program.
    """
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currencies = input("Enter the target currencies (comma-separated, e.g., EUR,JPY): ").upper().split(',')
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

if __name__ == '__main__':
    main()