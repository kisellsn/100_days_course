import random
import smtplib
import datetime as dt

# connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
# connection.close()

# ---------------------------- SEND QUOTE ON RANDOM DAY ------------------------------- #

EMAIL1 = "sonyakondratskaya@gmail.com"
PASSWORD1 = "ereo ozya axce vkqp"
EMAIL2 = "kisellsn@yahoo.com"

now = dt.datetime.now()
if now.weekday() == 1:
    with open('quotes.txt') as file:
        data = file.readlines()

    quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()  # for security
        connection.login(user=EMAIL1, password=PASSWORD1)

        connection.sendmail(from_addr=EMAIL1,
                            to_addrs=EMAIL1,
                            msg=f"Subject:Your quote for today\n\n{quote }")




# today = dt.date.today()  # 2024-07-16
# now = dt.datetime.now()  # 2024-07-16 10:54:41.168770
#
# yesterday = today - dt.timedelta(days=1)
#
# year = yesterday.day
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2004, month=1, day=3, hour=11)
# print(date_of_birth)