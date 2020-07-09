from selenium import webdriver
from Tools.Path import *


driver = webdriver.Chrome(path_to_driver)

driver.get("https://www.w3schools.com/howto/")  # first site
print(driver.title)

driver.get("https://phptravels.com/demo")  # second site
print(driver.title)

driver.back()
print(driver.title)  # print first title

driver.forward()
print(driver.title)  # print second title

driver.quit()
