from selenium import webdriver
from selenium.webdriver.common.by import By
from Tools.Path import *

driver = webdriver.Chrome(path_to_driver)

driver.get("https://accounts.ukr.net/registration")

input_boxes = driver.find_elements(By.CLASS_NAME, "form__section")
print(len(input_boxes))

driver.find_element(By.ID, "id-login").send_keys('ababagalamaga')
driver.find_element(By.ID, "id-password").send_keys("123Qssww")
driver.find_element(By.ID, "id-password-repeat").send_keys("123Qssww")

driver.find_element(By.ID, "id-first-name").send_keys("Valeriy")
driver.find_element(
    By.CSS_SELECTOR,
    "/html/body/div/div/main/form/section[3]/section[1]/div/div[2]/input"
).send_keys("Leontiev")
