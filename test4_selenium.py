from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_directorio_anime_navigation(self):
        browser = self.browser
        browser.get("https://www3.animeflv.net/")  
        directorio_anime_link = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/div[2]/nav/ul/li[2]/a")
        directorio_anime_link.send_keys(Keys.ENTER)
        sleep(5)
        title_element = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/h1")
        actual_text = title_element.text.strip()
        expected_text = "Lista completa de Animes"
        self.assertEqual(actual_text, expected_text, f"El texto del título no coincide. Se encontró: '{actual_text}'")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()