from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C://Users//Grom//Documents//chromedriver.exe")

driver.get("https://www.w3schools.com/howto/")  # first site
print(driver.title)

driver.get("https://phptravels.com/demo")  # second site
print(driver.title)

driver.back()
print(driver.title)  # print first title

driver.forward()
print(driver.title)  # print second title

driver.quit()
