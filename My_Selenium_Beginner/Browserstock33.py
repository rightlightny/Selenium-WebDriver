# coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from BrowserStack import my_key


class Search1Chrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '78.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = my_key.key
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


class Search2FF(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '74.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Frefox Test',
            'acceptSslCerts': True
        }
        url = my_key.key
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
        time.sleep(2)
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


class Search3Edge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Edge',
            'browser_version': '87.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Chrome Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        time.sleep(2)
        driver.find_element(By.NAME, "btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        time.sleep(3)
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        time.sleep(2)
        # Find el Dancing
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()


class Search4BigSurChrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': '87.0',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        time.sleep(2)
        driver.find_element(By.NAME, "btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        time.sleep(2)
        # Find el Dancing
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()


class Search4BigSurFF(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Firefox',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        time.sleep(2)
        driver.find_element(By.NAME, "btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        time.sleep(2)
        # Find el Dancing
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()


class Search4BigSurEdge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Edge',
            'browser_version': '87.0',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        time.sleep(2)
        driver.find_element(By.NAME, "btnK").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        time.sleep(2)
        # Find el Dancing
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()


class Search4BigSurSafari(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'resolution': '1920x1080',
            'browser': 'Safari',
            'browser_version': '14.0',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test'
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.maximize_window()

        driver.find_element(By.NAME, "q").send_keys("abc")
        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
        print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
        print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

        time.sleep(2)
        driver.find_element(By.NAME, "btnK").click()
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
        assert "ABC Home Page - ABC.com" in driver.title
        print(driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
        time.sleep(2)
        # Find el Dancing
        driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
        assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
        print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
