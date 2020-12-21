from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver.exe")
driver.get(r"C:\Users\user\OneDrive\python practice folder\Selenium\alert.html")
driver.maximize_window()

btn = driver.find_element_by_name('alert')
btn.click()

obj = driver.switch_to_alert()
msg = obj.text

print("Alert shows following messege: ", msg)
time.sleep(10)

obj.accept()
# obj.send_keys() --> for 'prompt'
print("Clicked on the 'ok' button")
time.sleep(5)

driver.refresh()

btn = driver.find_element_by_name('alert')
btn.click()

obj = driver.switch_to_alert()
msg = obj.text

print("Alert shows following messege: ", msg)
time.sleep(10)

obj.dismiss()
print("Clicked on the 'cancel' button")

driver.close()
