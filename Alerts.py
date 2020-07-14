from selenium import webdriver
from Tools.Path import path_to_driver
from Tools.Urls import test_auto_practice
import time


driver = webdriver.Chrome(path_to_driver)
driver.get(test_auto_practice)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(2)
#  Deprecated way
# driver.switch_to_alert().accept()   # Closes alert window by using OK button
# driver.switch_to_alert().dismiss()  # Closes alert window by using Cancel button

#  Actual way
driver.switch_to.alert.accept()  # Closes alert window by using OK button
driver.switch_to.alert.dismiss()  # Closes alert window by using Cancel button

driver.quit()
