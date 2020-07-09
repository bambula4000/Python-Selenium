from selenium import webdriver
from Tools.Path import *


driver = webdriver.Chrome(path_to_driver)
driver.implicitly_wait(10)  # wait for any element, max time 10 seconds
driver.get("https://www.phptravels.net/admin")

assert "Administator Login" in driver.title

driver.find_element_by_name("email").send_keys("admin@phptravels.com")
driver.find_element_by_name("password").send_keys("demoadmin")

driver.find_element_by_class_name(
    "btn.btn-primary.btn-block.ladda-button.fadeIn.animated.btn-lg"
).click()

driver.find_element_by_id('select_all')

driver.quit()
