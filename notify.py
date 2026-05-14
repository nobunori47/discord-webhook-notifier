import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1504485712135852033/i1dhN7b0_ShiyL5EMKfzzEvn3DiSj6RQiHE4YZMplCKgDUeD0Idi4kCGt9rUU_ds2hr7"

def send_notification(message: str) -> bool:
    payload = {
        "content": message,
        "username": "Spidey Bot"
    }
    res = requests.post(WEBHOOK_URL, json=payload)
    print(f"ステータスコード: {res.status_code}")
    return res.status_code == 204

send_notification("🚀 テスト通知！Webhookが動いています！")

# 例：エラー発生時に通知
try:
    # 何らかの処理
    pass
except Exception as e:
    send_notification(f"⚠️ エラーが発生しました: {e}")