from selenium import webdriver
from selenium.webdriver import ActionChains
from Tools.Path import path_to_driver
from Tools.Urls import test_auto_practice

driver = webdriver.Chrome(path_to_driver)
action = ActionChains(driver)
driver.get(test_auto_practice)

element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
action.double_click(element).perform()

driver.quit()
