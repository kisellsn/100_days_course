from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# wanted_product_url = "https://www.amazon.pl/Fjallraven-Classic-Backpack-Everyday-Graphite/dp/B002OWETK4/ref=sr_1_22?crid=696I0X2T2HN4&dib=eyJ2IjoiMSJ9.1Kmn_Q7PC1i54y_B-luaUs2PKU44E2gdrgjBrJ5I5U0a2v-JU0OddFj9NJ9GjwgbCFUdBulsAvWpkQlRxFvZqfz0Pcy1LVBAgj4_CfEM68EIrtCWPP4SRlGuUHxKn3XjB76aqZFauqVKZJhE48Q_6ALh16yA4KMmznQISWZBjNDh7YWc6fAe-2y82K2VNWVyDd_75tT1HXLodk4vwc_NVw-y_760g1KcZcFaLmYU30g.YWGUOH4-2aMevqWvUtVgdkMDxlsswXFHjPBJakstfe0&dib_tag=se&keywords=korean+backpack&qid=1722284046&sprefix=korean+backpack%2Cspecialty-aps%2C634&sr=8-22"
#
# driver.get("https://www.eurosport.com/artistic-gymnastics/olympic-games-paris-2024/2024/simone-biles-hits-hardest-vault-in-the-world-in-magnificent-olympic-showing-at-paris-2024-the-greatest_vid2193744/video.shtml")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.text)

# title_by_XPATH = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/h1')
# print(title_by_XPATH.text)


driver.get("https://www.python.org/")
event_times = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
event_names = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
# event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

event_data = {i: {'time': time.text.split("T")[0], "name": event_names[i].text} for i, time in enumerate(event_times)}
print(event_data)

# driver.quit()