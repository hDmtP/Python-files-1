from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver.exe")
driver.get("https://www.twitter.com")
select = Select(driver.find_element_by_name('name'))
# select.select_by_index(index)
select.select_by_visible_text("text")
# select.select_by_value(value)

      #NEEDS MORE TO CONFIRM THIS TOPIC