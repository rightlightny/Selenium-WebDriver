import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_qasvus_wordpress_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
        time.sleep(1)  # simulate long running test

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        name = driver_chrome.find_element_by_name("g2-name")
        name.clear()
        name.send_keys("Alexey")
        email = driver_chrome.find_element_by_name("g2-email")
        email.clear()
        email.send_keys("lexus330rx@mail.ru")
        message = driver_chrome.find_element_by_name("g2-message")
        message.clear()
        message.send_keys("Hello, my friends!")
        time.sleep(1)
        driver_chrome.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')
        try:
            WebDriverWait(driver_chrome, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                              "back')]")))
            driver_chrome.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
        except TimeoutException:
            print("Loading took too much time!")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30"]')))
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

    def test_qasvus_wordpress_chrome_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
        time.sleep(1)

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        name = driver_chrome.find_element_by_name("g2-name")
        name.clear()
        name.send_keys("Alexey")
        email = driver_chrome.find_element_by_name("g2-email")
        email.clear()
        email.send_keys("lexus330rx@mail.ru")
        message = driver_chrome.find_element_by_name("g2-message")
        message.clear()
        message.send_keys("Hello, my friends!")
        time.sleep(1)
        driver_chrome.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')
        try:
            WebDriverWait(driver_chrome, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                              "back')]")))
            driver_chrome.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
        except TimeoutException:
            print("Loading took too much time!")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30"]')))
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser.


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_qasvus_wordpress_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))
        time.sleep(1)

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        name = driver_firefox.find_element_by_name("g2-name")
        name.clear()
        name.send_keys("Alexey")
        email = driver_firefox.find_element_by_name("g2-email")
        email.clear()
        email.send_keys("lexus330rx@mail.ru")
        message = driver_firefox.find_element_by_name("g2-message")
        message.clear()
        message.send_keys("Hello, my friends!")
        time.sleep(1)
        driver_firefox.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')
        try:
            WebDriverWait(driver_firefox, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                              "back')]")))
            driver_firefox.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
        except TimeoutException:
            print("Loading took too much time!")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30"]')))
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

    def test_qasvus_wordpress_firefox_1120x850(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 850)
        driver_firefox.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))
        time.sleep(1)

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        name = driver_firefox.find_element_by_name("g2-name")
        name.clear()
        name.send_keys("Alexey")
        email = driver_firefox.find_element_by_name("g2-email")
        email.clear()
        email.send_keys("lexus330rx@mail.ru")
        message = driver_firefox.find_element_by_name("g2-message")
        message.clear()
        message.send_keys("Hello, my friends!")
        time.sleep(1)
        driver_firefox.find_element(By.XPATH, "//button[@type='submit']").send_keys('\n')
        try:
            WebDriverWait(driver_firefox, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                               "back')]")))
            driver_firefox.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
        except TimeoutException:
            print("Loading took too much time!")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30"]')))
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()