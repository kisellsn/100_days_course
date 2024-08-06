from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
print(articles_number.text)

search_bar = driver.find_element(By.NAME, "search")
query = "Python"
search_bar.send_keys(query, Keys.ENTER)
