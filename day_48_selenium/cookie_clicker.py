import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

five_min = time.time() + 60*5   # 5 minutes from now
timeout = time.time() + 5
while time.time() > five_min:
    cookie.click()

    if time.time() > timeout:
        money = driver.find_element(By.CSS_SELECTOR, "#money").text

        most_expensive_upgrade = driver.find_elements(
            by=By.XPATH,
            value="//div[@id='store']/div[not(contains(@class, 'grayed'))]"
        )
        try:
            most_expensive_upgrade[-1].click()
        except IndexError:
            pass

        timeout = time.time() + 5

print(driver.find_element(By.CSS_SELECTOR, "#cps"))