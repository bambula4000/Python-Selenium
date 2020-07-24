from selenium import webdriver
from Tools.Path import path_to_driver
from Tools.Urls import opensource
from Tools import ExcelUtils


driver = webdriver.Chrome(path_to_driver)
driver.get(opensource)

path = 'C://Users//Grom//Downloads//Credentials.xlsx'

rows_count = ExcelUtils.get_row_count(path, 'TemplateImportEmpl')

for row in range(1, rows_count+1):
    user_name = ExcelUtils.read_data(path, 'TemplateImportEmpl', row, 1)
    password = ExcelUtils.read_data(path, 'TemplateImportEmpl', row, 2)

    driver.find_element_by_id('txtUsername').send_keys(user_name)
    driver.find_element_by_id('txtPassword').send_keys(password)

    driver.find_element_by_id('btnLogin').click()
    if driver.page_source.__contains__('Welcome Admin'):
        ExcelUtils.write_data(path, 'TemplateImportEmpl', row, 3, 'passed')
    else:
        ExcelUtils.write_data(path, 'TemplateImportEmpl', row, 3, 'failed')

driver.quit()
