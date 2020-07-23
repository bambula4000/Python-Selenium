from selenium import webdriver
from Tools.Path import path_to_driver
from time import sleep

driver = webdriver.Chrome(path_to_driver)
driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.find_element_by_id('textbox').send_keys('test test test')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()

sleep(1)
driver.quit()
