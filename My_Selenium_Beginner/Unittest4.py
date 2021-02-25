# Two browsers test for Google and Wikipedia with Waiting functional
from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
# import HtmlTestRunner


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        if not "Google" in driver.title:
            raise Exception("Unable to load google page!")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Chrome Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            # driver.get_screenshot_as_file("google_page_loading_error.png")
            # driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        # workflow over "elem" variable to better code length

        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("wikipedia")
        # driver.find_element_by_name("q").send_keys(Keys.RETURN)

        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)  # wait max 5 sec

        assert "No results found." not in driver.page_source  # True or False

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        driver.find_element_by_partial_link_text("Wikipedia").click()
        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")

        if not "Wikipedia" in driver.title:
            raise Exception("Unable to load Wikipedia page!")

        assert "No results found." not in driver.page_source

        # API response Status code check
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, "status Code")
        else:
            print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")

        wait = WebDriverWait(driver, 2)
        #       wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-wiki-logo")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem2 = driver.find_element_by_id("searchInput")
        elem2.send_keys("Gold")
        elem2.send_keys(Keys.RETURN)
        driver.find_element_by_partial_link_text("Gold").click()
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Gold - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if not "Gold" in driver.title:
            raise Exception("Unable to load Wikipedia GOLD page!")

        driver.find_element_by_xpath("//img[@alt='Gold nugget (Australia) 4 (16848647509).jpg']").click()
        driver.find_element_by_xpath("//img[@class='mw-mmv-final-image jpg']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@src='https://upload.wikimedia.org/wikipedia/commons/d/d7/Gold-crystals.jpg']")))
            print("Wikipedia Gold Page is ready!")
            driver.get_screenshot_as_file('ScreenshotGold_page.png')
        except TimeoutException:
            print("Loading took too much time!")
            # driver.get_screenshot_as_file('gold_page_loading_error.png')
        driver.implicitly_wait(10)

        assert "Gold_nugget_(Australia)_4_(16848647509).jpg (3531×2278)" in driver.title
        print("Page has", driver.title + " as Page title")
        print("Test for Chrome is Done! Gold forever!")
        driver.get_screenshot_as_file('gold1.png')
        # driver.save_screenshot('./UnitTests/gold1.png')

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")
        # check API response code
        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        if not "Google" in driver.title:
            raise Exception("Unable to load Google page!")

        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("wikipedia")
        elem.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source
        driver.implicitly_wait(5)

        elem2 = driver.find_element_by_partial_link_text("Wikipedia")
        elem2.click()
        self.assertIn("Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        if not "Wikipedia" in driver.title:
            raise Exception("Unable to load Wikipedia page!")

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 2)
        #       wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-wiki-logo")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem3 = driver.find_element_by_id("searchInput")
        elem3.send_keys("Gold")
        elem3.send_keys(Keys.RETURN)
        driver.find_element_by_partial_link_text("Gold").click()
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Gold - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")

        if not "Gold" in driver.title:
            raise Exception("Unable to load Wikipedia GOLD page!")

        # API response Status code check
        code = requests.get("https://www.wikipedia.org").status_code
        if code == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, "status Code")
        else:
            print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")

        driver.find_element_by_xpath("//img[@alt='Gold nugget (Australia) 4 (16848647509).jpg']").click()

        # This waits up to 10 seconds before throwing a
        # TimeoutException unless it finds the element to return within 10 seconds.
        try:
            WebDriverWait(driver, 5) \
                .until(EC.presence_of_element_located((By.XPATH, "//img[@class='shrinkToFit']")))
            print("First Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        # driver.implicitly_wait(10)
        # driver.find_element_by_xpath("//img[@class='shrinkToFit']").click()

        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//img[@class='overflowingVertical']")))
            print("Second Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            # self.assertIn("Gold-crystals.jpg (JPEG Image, 4788 × 3102 pixels)", driver.title)
            print("Page has", driver.title + " as Page title")

        print("Test for Firefox is Done! Gold forever!")

    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sefremov/PycharmProjects/Python/seleniumPy'
#                                                         '/HtmlReports'))
