from selenium import webdriver
from selenium.webdriver.common.by import By
from Tools.Path import path_to_driver
from Tools.Urls import registration_form


driver = webdriver.Chrome(path_to_driver)

driver.get(registration_form)

radio_btn = driver.find_element(
    By.XPATH, "/html/body/div/div/main/form/section[3]/section[3]/div/div[1]/label[1]")

if str(radio_btn.is_selected()) == 'False':
    driver.find_element(By.XPATH, "/html/body/div/div/main/form/section[3]/section[3]/div/div[1]/label[1]").click()

driver.find_element(
    By.CLASS_NAME,
    "checkbox__imitator.checkbox__imitator_size-regular.checkbox__imitator_type-main")\
    .click()

driver.quit()
