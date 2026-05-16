import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_notification(message: str) -> bool:
    payload = {
        "content": message,
        "username": "Spidey Bot"
    }
    res = requests.post(WEBHOOK_URL, json=payload)
    print(f"ステータスコード: {res.status_code}")
    return res.status_code == 204

send_notification("🚀 テスト通知！Webhookが動いています！")

try:
    pass
except Exception as e:
    send_notification(f"⚠️ エラーが発生しました: {e}")
