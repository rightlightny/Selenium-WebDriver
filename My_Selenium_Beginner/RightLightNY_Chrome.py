import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from My_Selenium_Beginner import my_key


class RLNYChrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '78.0',
            'os': 'MAC High Sierra',
            'os_version': '10.13.6 (17G14042)',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = my_key.RLNY
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        driver.implicitly_wait(5)
        driver.find_element(By.NAME, "btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        driver.implicitly_wait(10)
        # Find el Dancing
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()
