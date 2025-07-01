import requests
import time
import os

os.system("clear")

API_URL = "https://api.gateio.ws/api/v4/spot/tickers"
params = {
    "currency_pair": "BTC_USDT"
}

def fetch_ticker_data():
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()[0]  
        return data
    except requests.exceptions.RequestException as e:
        print("Gagal mengambil data dari API:", e)
        return None

def update_data_loop(interval_seconds=10):
    while True:
        print("🔄 Mengambil data ticker terbaru...")
        ticker = fetch_ticker_data()
        if ticker:
            print(f"💰 Harga: {ticker['last']} USDT")
            print(f"📈 High: {ticker['high_24h']}, 📉 Low: {ticker['low_24h']}")
            print(f"📊 Volume 24h: {ticker['base_volume']} BTC\n")
        else:
            print("⚠️ Data tidak tersedia\n")

        time.sleep(interval_seconds)

if __name__ == "__main__":
    update_data_loop(1)  # update teros
