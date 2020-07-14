from selenium import webdriver
from Tools.Path import path_to_driver
import time

driver = webdriver.Chrome(path_to_driver)
driver.get("https://prom.ua/")

# time.sleep(4)
driver.find_element_by_class_name("bb-promo-panel").click()

print(driver.current_window_handle)  # CDwindow-3E5914F435ECDACD16BD78DE55A27926 parent tab

tabs = driver.window_handles  # return all the handle values of opened browser tabs

for tab in tabs:
    print(driver.title)
    time.sleep(1)

driver.switch_to.window(tabs[0])  # switch to first tab

driver.quit()
