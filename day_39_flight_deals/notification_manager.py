import os
import smtplib

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")



class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
            body=message_body
        )
        print(message.status)

    def send_email(self, email_body, email_list):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            for email in email_list:
                connection.sendmail(from_addr=SENDER_EMAIL,
                                    to_addrs=email["email"],
                                    msg=f"Low price alert!\n\n"
                                        f"{email_body}")
