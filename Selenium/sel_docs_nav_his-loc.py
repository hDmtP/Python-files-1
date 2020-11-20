from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver.exe")
driver.forward()
driver.close()