import requests
from project.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


# send message in telegram bot
def telegram_bot_sendtext(BOT_MESSAGE):
    send_text = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=Markdown&text=%s' % (
    TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, BOT_MESSAGE)
    response = requests.get(send_text)
    return response.json()
