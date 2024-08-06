import os

from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")

wanted_product_url = "https://www.amazon.pl/Fjallraven-Classic-Backpack-Everyday-Graphite/dp/B002OWETK4/ref=sr_1_22?crid=696I0X2T2HN4&dib=eyJ2IjoiMSJ9.1Kmn_Q7PC1i54y_B-luaUs2PKU44E2gdrgjBrJ5I5U0a2v-JU0OddFj9NJ9GjwgbCFUdBulsAvWpkQlRxFvZqfz0Pcy1LVBAgj4_CfEM68EIrtCWPP4SRlGuUHxKn3XjB76aqZFauqVKZJhE48Q_6ALh16yA4KMmznQISWZBjNDh7YWc6fAe-2y82K2VNWVyDd_75tT1HXLodk4vwc_NVw-y_760g1KcZcFaLmYU30g.YWGUOH4-2aMevqWvUtVgdkMDxlsswXFHjPBJakstfe0&dib_tag=se&keywords=korean+backpack&qid=1722284046&sprefix=korean+backpack%2Cspecialty-aps%2C634&sr=8-22"
# wanted_product_url = "https://appbrewery.github.io/instant_pot/"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,en-US;q=0.9,uk;q=0.8,uk-UA;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}
response = requests.get(wanted_product_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# price = float(f"{soup.find(class_="a-price-whole").get_text()}{soup.find(class_="a-price-fraction").get_text()}")
# name = soup.find(class_="a-size-large product-title-word-break").get_text()
price = float(soup.find(class_="a-offscreen").get_text())
name = soup.find(class_="a-size-large product-title-word-break").get_text()
print(price)
target_price = 100

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(from_addr=SENDER_EMAIL,
                        to_addrs=SENDER_EMAIL,
                        msg=f"Subject:Low price Alert!\n\n"
                            f"{name} is now only {price}\n"
                            f"{wanted_product_url}".encode("utf-8"))