from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_title_text(self):
        browser = self.browser
        browser.get("https://www3.animeflv.net/")  
        title_element = browser.find_element(By.CSS_SELECTOR, "div.Container h1")
        title_text = title_element.text.strip()
        expected_text = "AnimeFLV tu fuente de anime online gratis en HD"
        self.assertEqual(title_text, expected_text, f"El texto del título no coincide. Se encontró: '{title_text}'")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()