import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class InstaFollower:
    def __init__(self, username, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.username = username
        self.password = password

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        allow_cookies_btn = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > '
                  'div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76'
                  '.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > '
                  'div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > '
                  'div > button._a9--._ap36._a9_0'
        )
        allow_cookies_btn.click()

        time.sleep(2)
        username_input = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        username_input.send_keys(self.username)
        password_input = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        password_input.send_keys(self.password)
        login_btn = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="loginForm"]/div/div[3]/button'
        )
        login_btn.click()
        time.sleep(10)

        notification_not_now = self.driver.find_element(
            by=By.XPATH,
            value="//button[contains(text(), 'Not Now')]"
        )
        notification_not_now.click()
        time.sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{os.getenv('SIMILAR_ACCOUNT')}/")
        time.sleep(10)
        followers = self.driver.find_element(
            by=By.XPATH,
            value="//a[contains(text(), ' followers')]"
        )
        followers.click()
        time.sleep(3)

        followers_popup = self.driver.find_element(
            by=By.XPATH,
            value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        )
        for i in range(10):
            time.sleep(3)
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                       followers_popup)

    def follow(self):
        follow_buttons = self.driver.find_elements(
            by=By.XPATH,
            value='//button[.//div[text()="Follow"]]'
        )
        print(follow_buttons)
        for button in follow_buttons:
            button.click()
            time.sleep(1.1)
            # except ElementClickInterceptedException:
            #     cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
            #     cancel_button.click()
