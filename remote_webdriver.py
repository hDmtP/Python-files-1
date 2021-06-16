from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

chrome_options = webdriver.ChromeOptions
chrome_options.set_capability("browserVersion", "87")
chrome_options.set_capability("platformName", "Windows 10")
driver = webdriver.Remote(command_executor="https://www.codewithharry.com", options=chrome_options)

driver.get("http://www.google.com")
driver.quit()