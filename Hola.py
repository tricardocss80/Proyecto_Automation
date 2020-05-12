from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_xpath("//input[@name='search_query']").send_keys("Hola")
driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Search')]").click()


time.sleep(3)
tc.assertEqual('No results were found for your search "Hola"',driver.find_element_by_xpath("//p[@class='alert alert-warning']").text)


driver.close()
driver.quit()