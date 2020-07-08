# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets
# import telegram
# bot = telegram.Bot(token="1245776688:AAESLGzyeOMygu5t9V1Ka2aLQEb2NWbw8ww")

# # This Chat ID could be find out using this procedure :
# # https://api.telegram.org/bot<YourBOTToken>/getUpdates
# chat_id=-1001187181732
# bot.send_message(chat_id=chat_id, text="www.google.com")

# **************************************

# Setting up guide
# https://notify.run/
# from notify_run import Notify
# notify = Notify()
# notify.send("Hiii There")

# **************************************

# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "test.mail.bluepi@gmail.com"
# receiver_email = "rishabh@bluepi.in"
# password = "wfsgwvsegjnukxzt"

# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)







