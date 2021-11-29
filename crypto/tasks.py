from celery import shared_task
from crypto.telegram_bot import telegram_bot_sendtext
from crypto.transaction import trongrid_balance, get_transactions


@shared_task()
def send_message():
    # Get total balance of given transaction address.
    total_balance = trongrid_balance()
    total_in, total_out = get_transactions()
    Message = "Total In: %s, Total Out: %s, Net: %s" % (str(total_in), str(total_out), str(total_balance))
    # Sending total in, total out & net balance message on telegram.
    telegram_bot_sendtext(Message)
    return "Message Sent Successfully!!"
