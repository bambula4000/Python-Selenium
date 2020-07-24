from selenium import webdriver
from Tools.Path import path_to_driver

driver = webdriver.Chrome(path_to_driver)
driver.get('https://amazon.com')

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))


# Adding new cookie to the browser
cookie = {'name': 'Alex', 'value': '31'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))

# Deleting cookie by name
driver.delete_cookie('Alex')

cookies = driver.get_cookies()
print(len(cookies))
for i in cookies:
    print(i)
