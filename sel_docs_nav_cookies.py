from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver.exe")
driver.get("https://www.codewithharry.com")
# cookie = {'name':'Java'}
# driver.add_cookie(cookie)
# driver.get_cookies()
print(driver.get_cookies())
driver.close()