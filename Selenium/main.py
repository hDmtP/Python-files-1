from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = r"C:\Users\user\Downloads\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(url="https://www.xnxx.com")