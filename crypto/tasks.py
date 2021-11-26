from celery import shared_task
from crypto.transaction import trongrid_balance
from crypto.telegram_bot import telegram_bot_sendtext


@shared_task()
def send_message():
    # Get total balance of given transaction address.
    total_balance = trongrid_balance()
    # Sending net balance message on telegram.
    telegram_bot_sendtext("Net: " + str(total_balance))
    return "Message Sent Successfully!!"
