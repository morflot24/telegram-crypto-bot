import os
import requests
import time

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_funding_rate():
    # Пример: получаем funding с Coinalyze (заглушка)
    return "Funding Rate: +0.01% на Binance (пример)"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        msg = get_funding_rate()
        send_message(msg)
        time.sleep(3600)  # раз в час
