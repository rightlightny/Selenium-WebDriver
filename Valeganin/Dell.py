import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_sign_in(self):
        driver_chrome = self.driver
        driver_chrome.get('https://www.dell.com/en-us')
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cf-dell-home')))
        assert 'Computers, Monitors & Technology Solutions | Dell USA' in driver_chrome.title
        driver_chrome.find_element(By.XPATH, '//span[@mh-sign-in-label="Sign In"]').click()
        driver_chrome.find_element(By.LINK_TEXT, 'Sign In').click()
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-brand-dell text-white')))
        time.sleep(2)
        assert 'Login or Register | Dell US' in driver_chrome.title
        driver_chrome.find_element(By.ID, 'EmailAddress').send_keys('smith739@gmail.com')
        driver_chrome.find_element(By.ID, 'Password').send_keys('Qwer1234')
        driver_chrome.find_element(By.XPATH, "//button[@id='sign-in-button']").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cf-dell-home')))
        assert 'Computers, Monitors & Technology Solutions | Dell USA' in driver_chrome.title
        # driver_chrome.find_element(By.XPATH, '//span[@mh-sign-in-label="Sign In"]').click()

    def test_sign_out(self):
        self.test_sign_in()
        driver_chrome = self.driver
        driver_chrome.find_element(By.XPATH, '//span[@mh-sign-in-label="Sign In"]').click()
        driver_chrome.find_element(By.LINK_TEXT, 'Sign Out').click()
        time.sleep(2)
        assert 'Computers, Monitors & Technology Solutions | Dell USA' in driver_chrome.title

    def tearDown(self):
        self.driver.quit()  # Close the browser.


if __name__ == "__main__":
    unittest.main()