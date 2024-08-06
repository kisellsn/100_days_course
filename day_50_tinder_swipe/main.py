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



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

time.sleep(5)
facebook_login = driver.find_element(By.XPATH, value='//*[@id="o-1596989266"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]')
facebook_login.click()



base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(os.getenv("FB_EMAIL"))
password.send_keys(os.getenv("FB_PASS"))
password.send_keys(Keys.ENTER)

time.sleep(5)
driver.find_element(By.XPATH, '//*[text()="Continue as Sonia"]').click()
#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)


time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


# dislike everyone
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    # try:
    print("called")
    dislike_button = driver.find_element(By.XPATH, value=
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    dislike_button.click()

    # #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
    #         match_popup.click()
    #
    #     #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    #     except NoSuchElementException:
    #         time.sleep(2)

driver.quit()