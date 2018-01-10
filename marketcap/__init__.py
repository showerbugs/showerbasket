import requests
from bs4 import BeautifulSoup


class MarketCap:
    def get(self, limit=50):
        ticker_cap = {}

        html = requests.get('https://www.coingecko.com/en').text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id='gecko-table').tbody
        for tr in table.find_all('tr'):
            ticker = tr.find_all('div', class_='coin-icon')[0].span.string
            ticker = ticker.strip()
            cap = tr.find_all('div', class_='cap-price')[0].span.string
            cap = cap.replace('$', '').replace(',', '').strip()

            ticker_cap[ticker] = cap

        return ticker_cap
