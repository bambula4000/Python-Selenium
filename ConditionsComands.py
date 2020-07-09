from selenium import webdriver
from time import sleep
from Tools.Path import *


driver = webdriver.Chrome(path_to_driver)

driver.get("https://www.phptravels.net/admin")

email_elem = driver.find_element_by_name("email")
print(email_elem.is_enabled())
print(email_elem.is_displayed())

password_elem = driver.find_element_by_name("password")
print(password_elem.is_enabled())
print(password_elem.is_displayed())

email_elem.send_keys("admin@phptravels.com")
password_elem.send_keys("demoadmin")

driver.find_element_by_class_name(
    "btn.btn-primary.btn-block.ladda-button.fadeIn.animated.btn-lg"
).click()
sleep(5)

button = driver.find_element_by_id('select_all')
print(button.is_selected())

driver.quit()

