import requests
from config.settings import DISCORD_WEBHOOK_URL
from datetime import datetime


def send_message(msg):
    """디스코드 메세지 전송"""
    now = datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(msg)}"}
    requests.post(DISCORD_WEBHOOK_URL, data=message)
    print(message)

## utils/notifier.py (디스코드 알림)
import requests
from config import DISCORD_WEBHOOK_URL

def send_discord_alert(message: str):
    """ 디스코드 웹훅을 이용한 알림 전송 """
    payload = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)