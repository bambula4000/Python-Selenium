from selenium import webdriver
from Tools.Path import path_to_driver

driver = webdriver.Chrome(path_to_driver)
driver.get('https://www.amazon.com/')

driver.save_screenshot('C://Users//Grom//Downloads/blabla.png')

driver.get_screenshot_as_file('C://Users//Grom//Downloads/blabla1.png')
