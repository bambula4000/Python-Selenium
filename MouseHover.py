from selenium import webdriver
from selenium.webdriver import ActionChains
from Tools.Path import path_to_driver
from Tools.Urls import opensource


driver = webdriver.Chrome(path_to_driver)
actions = ActionChains(driver)
driver.get(opensource)

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
user_management = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

driver.quit()
