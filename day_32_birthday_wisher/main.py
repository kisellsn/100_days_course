import os
import random
import smtplib
import datetime as dt
import pandas

SENDER_EMAIL = "sonyakondratskaya@gmail.com"
PASSWORD = "ereo ozya axce vkqp"
SENDER_NAME = "Sonia"
letters_folder_path = "letter_templates"

# ---------------------------- LOAD BIRTHDAY DATA ------------------------------- #
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row
                  for (index, data_row) in data.iterrows()}

# ----------------------------SEND WISHES ------------------------------- #
today_date = dt.date.today()
today_month_day = (today_date.month, today_date.day)

if today_month_day in birthdays_dict:
    birthday_person = birthdays_dict[today_month_day]

    templates = os.listdir(letters_folder_path)
    letter_file = random.choice(templates)
    with open(f"{letters_folder_path}/{letter_file}", "r") as file:
        text = file.read()
        text = text.replace("[NAME]", birthday_person["name"])
        text = text.replace("[SENDER_NAME]", SENDER_NAME)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)

        recipient_email = birthday_person["email"]
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=recipient_email,
                            msg=f"Subject:Happy Birthday!\n\n"
                                f"{text}")

