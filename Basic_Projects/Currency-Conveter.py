from forex_python.converter import CurrencyRates

c = CurrencyRates()
rate = c.get_rate('USD', 'INR')
print(f"The current exchange rate from USD to INR is: {rate}")