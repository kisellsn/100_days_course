from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, "fName")
last_name_field = driver.find_element(By.NAME, "lName")
email_field = driver.find_element(By.NAME, "email")

first_name_field.send_keys("fName")
last_name_field.send_keys("lName")
email_field.send_keys("email@gmail.com")
submit_button = driver.find_element(By.CSS_SELECTOR, "body > form > button").click()