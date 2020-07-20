from selenium import webdriver
from selenium.webdriver import ActionChains
from Tools.Path import path_to_driver
from Tools.Urls import demo_guru_drag


driver = webdriver.Chrome(path_to_driver)
actions = ActionChains(driver)
driver.get(demo_guru_drag)

source_element = driver.find_element_by_xpath('//*[@id="credit2"]/a')
target_element = driver.find_element_by_xpath('//*[@id="bank"]/li')

actions.drag_and_drop(source_element, target_element).perform()

driver.quit()
