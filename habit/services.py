from config.settings import TELEGRAM_BOT_KEY
import requests


def send_tg_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
    else:
        print(f"Message sent successfully to chat_id {chat_id}: {text}")


def is_today(periodicity, start_date, today):
    delta_days = (today - start_date).days

    if periodicity == "day":
        return True
    if periodicity == "2 days":
        return delta_days % 2 == 0
    if periodicity == "3 days":
        return delta_days % 3 == 0
    if periodicity == "week":
        return delta_days % 7 == 0

    return False
