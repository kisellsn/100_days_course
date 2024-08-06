from bs4 import BeautifulSoup
import requests
import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()


ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
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
response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

prices = [price.text.split("+")[0].replace("/mo", "")
          for price in soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]
links = [link["href"] for link in soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")]
addresses = [address.text.replace("| ", "").strip()
             for address in soup.find_all("address", attrs={"data-test": "property-card-addr"})]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)


for i, _ in enumerate(prices):
    driver.get(os.getenv("GOOGLE_FORM_LINK"))
    time.sleep(4)

    inputs = driver.find_elements(by=By.XPATH, value="//input[@class='whsOnd zHQkBf']")
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    submit = driver.find_element(By.XPATH, value="//div[@role='button']")
    submit.click()


