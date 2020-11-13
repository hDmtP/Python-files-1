from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = r"C:\Users\user\Downloads\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(url="https://selenium-python.readthedocs.io/getting-started.html")
elem = driver.find_element_by_name("q")
print(elem)
elem.clear()
elem.send_keys("send_keys")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()