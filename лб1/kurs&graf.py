import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_exchange_rates(base_url, start_date, end_date):
    rates = {}
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime('%Y%m%d')
        response = requests.get(f"{base_url}?date={formatted_date}&json")
        if response.status_code == 200:
            data = response.json()
            for item in data:
                currency = item['cc']
                rate = item['rate']
                if currency not in rates:
                    rates[currency] = []
                rates[currency].append({'date': current_date, 'rate': rate})
        else:
            print(f"Failed to fetch data for date {formatted_date}")
        current_date += timedelta(days=1)
    return rates

def plot_exchange_rates(rates, currencies_to_plot):
    for currency in currencies_to_plot:
        if currency in rates:
            dates = [entry['date'] for entry in rates[currency]]
            values = [entry['rate'] for entry in rates[currency]]
            plt.plot(dates, values, label=currency)
    
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.title('Зміна курсів валют за тиждень')
    plt.legend()
    plt.grid(True)
    plt.show()

base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
end_date = datetime.strptime("20241202", "%Y%m%d")
start_date = end_date - timedelta(days=6)

exchange_rates = get_exchange_rates(base_url, start_date, end_date)
currencies = ['USD', 'EUR']
plot_exchange_rates(exchange_rates, currencies)