import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumDocs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io/getting-started.html")
        self.assertIn("selenium", driver.current_url)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
