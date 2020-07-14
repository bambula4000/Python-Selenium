from selenium import webdriver
from selenium.webdriver.common.by import By
from Tools.Path import path_to_driver
from Tools.Urls import travels_demo


driver = webdriver.Chrome(path_to_driver)
driver.get(travels_demo)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    print(link.text)

#  Click on link by part of link text
driver.find_element(By.PARTIAL_LINK_TEXT, "Contact ").click()

#  Click on link by full link text
driver.find_element(By.LINK_TEXT, "Contact Us").click()

driver.quit()
