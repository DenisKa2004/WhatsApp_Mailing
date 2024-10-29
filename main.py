import schedule
import time
import requests
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env файла
load_dotenv()

# Функция для отправки сообщения в WhatsApp
def send_whatsapp_message(api_url, id_instance, api_token, chat_id):
    message = {
        "chatId": chat_id,
        "message": "+"  # Замените на ваш текст сообщения
    }
    
    response = requests.post(
        f"{api_url}/waInstance{id_instance}/sendMessage/{api_token}",
        json=message
    )
    
    if response.status_code == 200:
        print(f"Сообщение успешно отправлено в группу {chat_id}.")
    else:
        print(f"Не удалось отправить сообщение в группу {chat_id}:", response.text)

# Функция для генерации случайного времени между 09:00 и 09:30
def get_random_time():
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("09:30", "%H:%M")
    random_time = start_time + timedelta(minutes=random.randint(0, 30))
    return random_time.strftime("%H:%M")

# Функция для планирования отправки сообщений каждый день кроме воскресенья
def schedule_daily_messages():
    accounts = [
        {
            "api_url": os.getenv("API_URL_1"),
            "id_instance": os.getenv("ID_INSTANCE_1"),
            "api_token": os.getenv("API_TOKEN_1"),
            "chat_id": os.getenv("GROUP_CHAT_ID_1")
        },
        {
            "api_url": os.getenv("API_URL_2"),
            "id_instance": os.getenv("ID_INSTANCE_2"),
            "api_token": os.getenv("API_TOKEN_2"),
            "chat_id": os.getenv("GROUP_CHAT_ID_2")
        }
    ]

    for account in accounts:
        # Генерируем случайное время для отправки сообщения
        random_time = get_random_time()

        # Планируем отправку сообщения каждый день, кроме воскресенья
        schedule.every().monday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )
        schedule.every().tuesday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )
        schedule.every().wednesday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )
        schedule.every().thursday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )
        schedule.every().friday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )
        schedule.every().saturday.at(random_time).do(
            send_whatsapp_message,
            account["api_url"],
            account["id_instance"],
            account["api_token"],
            account["chat_id"]
        )

        print(f"Сообщение для аккаунта с ID инстанса {account['id_instance']} будет отправляться в {random_time}.")

    # Бесконечный цикл для выполнения запланированных задач
    while True:
        schedule.run_pending()  # Выполняем задачи, если наступило запланированное время
        time.sleep(60)  # Проверяем каждую минуту

# Запуск программы
if __name__ == "__main__":
    schedule_daily_messages()
