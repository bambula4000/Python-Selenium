from selenium import webdriver
from selenium.webdriver import ActionChains
from Tools.Path import path_to_driver
from Tools.Urls import demo_guru_context


driver = webdriver.Chrome(path_to_driver)
actions = ActionChains(driver)
driver.get(demo_guru_context)

element = driver.find_element_by_class_name('context-menu-one.btn.btn-neutral')

actions.context_click(element).perform()

driver.quit()
