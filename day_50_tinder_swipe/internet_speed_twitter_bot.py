import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        self.driver.implicitly_wait(5)
        privacy_allow = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        privacy_allow.click()

        go_btn = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > '
                  'div.speedtest-container.main-row > div.start-button > a > span.start-text'
        )
        go_btn.click()

        time.sleep(60)
        down = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                  '1]/div[1]/div/div[2]/span'
        ).text
        up = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                  '1]/div[2]/div/div[2]/span'
        ).text
        return down, up

    def tweet_at_provider(self, curr_down, curr_up):
        if float(curr_down) >= self.down and float(curr_up) >= self.up:
            return None

        self.driver.get("https://x.com/i/flow/login")

        time.sleep(10)
        login_field = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='#layers > div:nth-child(2) > div > div > div > div > div > '
                  'div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > '
                  'div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div '
                  '> div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > '
                  'div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div > div > '
                  'div.css-175oi2r.r-1mmae3n.r-1e084wi.r-13qz1uu > label > div > '
                  'div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div '
                  '> input'
        )
        login_field.send_keys(os.getenv("X_USERNAME"))
        next_btn = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
        )
        next_btn.click()

        time.sleep(2)
        try:
            email_field = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                      '1]/div/div[2]/label/div/div[2]/div/input'
            )
            email_field.send_keys(os.getenv("X_EMAIL"))
        except NoSuchElementException:
            pass
        else:
            next_btn = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                      '2]/div/div/div/button'
            )
            next_btn.click()

        time.sleep(2)
        password_field = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                  '3]/div/label/div/div[2]/div[1]/input'
        )
        password_field.send_keys(os.getenv("X_PASSWORD"))
        login_btn = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                  '1]/div/div/button'
        )
        login_btn.click()

        time.sleep(2)
        try:
            next_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="confirmationSheetConfirm"]')
            next_btn.click()
        except NoSuchElementException:
            pass

        time.sleep(5)
        tweet_compose = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > '
                  'div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > '
                  'div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > '
                  'div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > '
                  'div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > '
                  'div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > '
                  'div.DraftEditor-editorContainer > div > div > div > div')
        tweet_compose.send_keys(f"Hey @<MY_PROVIDER, why is my internet speed {curr_down}down/{curr_up}up "
                              f"when i pay for {self.down}down/{self.up}up ?")

        time.sleep(2)
        post_btn = self.driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_btn.click()

        time.sleep(2)
        self.driver.quit()
