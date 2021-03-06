import unittest
from selenium import webdriver
import time


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')

    def test_search_no_elements(self):
        self.driver.find_element_by_id('search_query_top').send_keys('hola')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text,
                         'No results were found for your search "hola"')

    def test_search_find_dresses(self):
        self.driver.find_element_by_id('search_query_top').send_keys('dress')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertTrue('DRESS' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)

    def test_search_find_tshirts(self):
        self.driver.find_element_by_id('search_query_top').send_keys('T-SHIRTS')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath("//span[@class='lighter']").text, '"T-SHIRTS"')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
