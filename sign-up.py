from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("riza")
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("pn")
email = driver.find_element(By.NAME, value="email")
email.send_keys("riza.pn@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
button.click()