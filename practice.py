from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

time_of_event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
name_of_event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# name_of_event.pop(0)
dict_of_event = {}
for index in range(len(time_of_event)):
    dict_of_event[index] = {
        "time": time_of_event[index].text,
        "name": name_of_event[index].text
    }


pprint(dict_of_event)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # Keep chrom browser after the program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=chrome_options)
# #
# # driver.get("https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904")
# #
# # wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
# #
# # try:
# #     # Wait until the element with class name 'a-price-whole' is located
# #
# #     # Once located, you can perform actions on the element
# #     price_dollars = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))).text
# #     price_cents = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"a-price-fraction"))).text
# #     print(f"The price is {price_dollars}.{price_cents}")
# # except Exception as e:
# #     print("An error occurred:", e)
#
# # scarping using name
# driver.get("https://www.google.com/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("name"))
# print(search_bar.get_attribute("title"))
#
# # can do using BY.ID
# # can do using BY.CSS_SELECTOr
# link = driver.find_element(By.CSS_SELECTOR, value="#SIvCob a")
# print(link.text)
#
# # find element using xpath
# xpath_of_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
# print(xpath_of_btn.tag_name)
# print(xpath_of_btn.get_attribute("name"))
# print(xpath_of_btn.get_attribute("value"))
# print(xpath_of_btn.size)

# price_dollars = driver.find_element(by="class name", value="a-price-whole")
# price_cents = driver.find_element(by="class name", value="a-price-fraction")
# print(f"The price is {price_dollars.text}.{price_cents.text}")
# # To close browser automatically
# driver.close() # closes single tab
# driver.quit() # closes entire browser