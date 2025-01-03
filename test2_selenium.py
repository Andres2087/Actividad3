from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_busqueda_anime(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  
        search = browser.find_element(By.ID, "search-anim")
        search.clear()
        search.send_keys("Naruto")
        search.submit()
        sleep(2)
        results = browser.find_elements(By.CSS_SELECTOR, ".ListAnimes.AX.Rows.A03.C02.D02")  
        self.assertGreater(len(results), 0, "No se encontraron resultados para 'Naruto'.")

        print("\nResultados de búsqueda:")
        for result in results:
            print(result.text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()