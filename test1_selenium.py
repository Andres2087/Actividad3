from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_list_animes_en_emision(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  

        contenedor = browser.find_element(By.ID, "mCSB_12")
        animes_list = contenedor.find_elements(By.TAG_NAME, "a")  

        res = []
        for anime in animes_list:
            res.append(anime.text)

        self.assertGreater(len(res), 0, "No se encontraron animes en emisión.")

        print("Animes en emisión:")
        for anime in res:
            print(anime)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
