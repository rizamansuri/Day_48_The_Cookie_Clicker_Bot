import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep browser open even after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# cnt = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
cnt = driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
print(cnt.text)

# cnt.click()
content_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# content_portals.click()

search = driver.find_element(By.NAME, value='search')
search.send_keys('Python', Keys.ENTER)