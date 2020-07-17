from selenium import webdriver
from Tools.Path import path_to_driver
from Tools.Urls import worlds_countries


driver = webdriver.Chrome(path_to_driver)
driver.get(worlds_countries)
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)", "")  # Scroll down by pixels

flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[93]/td[2]')
driver.execute_script("arguments[0].scrollIntoView();", flag)  # Scroll till element visible

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")  # Scroll down page toll end

driver.quit()
