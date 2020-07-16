from selenium import webdriver
from Tools.Path import path_to_driver


driver = webdriver.Chrome(path_to_driver)
driver.get('https://www.w3schools.com/html/html_tables.asp')

rows = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))  # Get count of rows
cols = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))  # Get count of columns

print('Company | ' + 'Contact | ' + 'Country')

# Parse html/web table
for r in range(2, rows+1):
    for c in range(1, cols+1):
        data = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        print(data, end=' | ')
    print()
driver.quit()
