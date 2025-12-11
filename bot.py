import requests
import time

TOKEN = "AAGbSf4tAl3EabHVc95olm__XIIhbXyTSZU"
CHAT_ID = "8457305838"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

while True:
    send_message("Bot radi 24/7 ✅")
    time.sleep(3600)  # šalje poruku na svakih sat vremena
