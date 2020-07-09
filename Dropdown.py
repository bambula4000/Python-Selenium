from selenium import webdriver
from selenium.webdriver.common.by import By
from Tools.Path import path_to_driver
from Tools.Urls import registration_form
from Tools.Locators import month_of_year


driver = webdriver.Chrome(path_to_driver)

driver.get(registration_form)

month_number = 3

element = driver.find_element(By.CLASS_NAME, "input-select__target").click()
driver.find_element(By.XPATH, month_of_year.format(month_number)).click()
