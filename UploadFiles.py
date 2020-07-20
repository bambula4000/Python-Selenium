from selenium import webdriver
from Tools.Path import path_to_driver
from Tools.Urls import test_auto_practice

driver = webdriver.Chrome(path_to_driver)
driver.get(test_auto_practice)

driver.switch_to.frame(0)
driver.find_element_by_id('RESULT_FileUpload-10').send_keys('C:/Users/Grom/Downloads/c09.jpg')

driver.quit()
