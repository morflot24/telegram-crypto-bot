import os
import requests
import time

# ПРАВИЛЬНО: переменные читаются по ИМЕНИ
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_funding_rate():
    return "⚡ BTC Funding Rate: +0.01% (пример)"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    print(f"Sent message, response: {response.status_code} - {response.text}")

if __name__ == "__main__":
    while True:
        try:
            msg = get_funding_rate()
            send_message(msg)
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(3600)
