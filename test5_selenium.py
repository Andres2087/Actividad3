from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
from selenium.webdriver.common.by import By

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://practicetestautomation.com/practice-test-login/")
		uname = browser.find_element(By.ID, 'username')
		uname.clear()
		uname.send_keys('student')
		passw = browser.find_element(By.ID, 'password')
		passw.clear()
		passw.send_keys('Password123')
		submitButton = browser.find_element(By.ID, 'submit')
		submitButton.send_keys(Keys.ENTER)
		sleep(2)
		res = browser.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[1]/h1')
		self.assertEqual('Logged In Successfully', res.text)

	def tearDown(self):
		self.browser.quit()


if __name__ == '__main__':
	unittest.main()