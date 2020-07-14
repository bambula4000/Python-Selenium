from selenium import webdriver
from Tools.Path import path_to_driver
from Tools.Urls import frames_page


driver = webdriver.Chrome(path_to_driver)
driver.get(frames_page)

driver.switch_to.frame("packageListFrame")  # first frame (left top)
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()  # !without this action we can't found other frame

driver.switch_to.frame("packageFrame")  # second frame (bottom left)
driver.find_element_by_link_text("WebDriver").click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")  # Third frame (right side)
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
