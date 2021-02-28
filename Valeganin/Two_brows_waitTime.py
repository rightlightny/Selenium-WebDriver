# Two browsers test for Google and Wikipedia with Waiting functional
import unittest
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


# import HtmlTestRunner

class ChromeSearch ( unittest.TestCase ):

    def setUp(self):
        self.driver = webdriver.Chrome ()
        self.driver.maximize_window ()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver = self.driver
        driver.get ( "https://www.google.com" )
        print ( "Google Url has ", requests.get ( "https://www.google.com" ).status_code, " as status Code" )

        if not "Google" in driver.title:
            raise Exception ( "Unable to load google page!" )

            # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait ( driver, 2 ).until ( EC.visibility_of_element_located ( (By.NAME, "q") ) )
            print ( "First Chrome Page is ready!" )
        except TimeoutException:
            print ( "Loading took too much time!" )
            # driver.get_screenshot_as_file("google_page_loading_error.png")
            # driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn ( "Google", driver.title )
        print ( "Page has", driver.title + " as Page title" )

        # workflow over "elem" variable to better code length

        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("wikipedia")
        # driver.find_element_by_name("q").send_keys(Keys.RETURN)

        elem = driver.find_element_by_name ( "q" )
        elem.clear ()
        elem.send_keys ( "Wikipedia" )
        elem.send_keys ( Keys.RETURN )
        driver.implicitly_wait ( 5 )  # wait max 5 sec

        assert "No results found." not in driver.page_source  # True or False

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait ( driver, 10 )
        wait.until ( EC.element_to_be_clickable ( (By.PARTIAL_LINK_TEXT, 'Wikipedia') ) )
        driver.find_element_by_partial_link_text ( "Wikipedia" ).click ()
        self.assertIn ( "Wikipedia", driver.title )
        print ( "Page has", driver.title + " as Page title" )
        print ( "Wikipedia Url has ", requests.get ( "https://www.wikipedia.org" ).status_code, " as status Code" )

        if not "Wikipedia" in driver.title:
            raise Exception ( "Unable to load Wikipedia page!" )

        # assert "No results found." not in driver.page_source

        # API response Status code check
        code = requests.get ( "https://www.wikipedia.org" ).status_code
        if code == 200:
            print ( "Wikipedia Url has correct", requests.get ( "https://www.wikipedia.org" ).status_code,
                    "status Code" )
        else:
            print ( "Wikipedia Url has", requests.get ( "https://www.wikipedia.org" ).status_code, "as status Code" )

        wait = WebDriverWait ( driver, 2 )

        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until ( EC.visibility_of_element_located ( (By.CLASS_NAME, "mw-wiki-logo") ) )
        wait.until ( EC.visibility_of_element_located ( (By.ID, "searchInput") ) )
        elem2 = driver.find_element_by_id ( "searchInput" )
        elem2.send_keys ( "Bread" )
        elem2.send_keys ( Keys.RETURN )
        driver.find_element_by_partial_link_text ( "Bread" ).click ()
        wait.until ( EC.visibility_of_element_located ( (By.ID, "firstHeading") ) )
        self.assertIn ( "Bread - Wikipedia", driver.title )
        print ( "Page has", driver.title + " as Page title" )
        if not "Bread" in driver.title:
            raise Exception ( "Unable to load Wikipedia Bread page!" )

        driver.find_element_by_xpath ( "//img[@alt='Loaves of bread in a basket']" ).click ()
        delay = 10  # 10 seconds

        print ( driver.find_element_by_xpath ( "//img[@class='mw-mmv-final-image jpg']" ) )
        delay = 20  # 10 seconds

        try:
            WebDriverWait ( driver, delay ).until (
                EC.presence_of_element_located ( (
                    By.XPATH, "//img[@src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3"
                              "%B6tchen.JPG/1024px-Korb_mit_Br%C3%B6tchen.JPG']") ) )
            print ( "Wikipedia Bread Page is ready!" )
            driver.get_screenshot_as_file ( 'ScreenshotBread_page.png' )
        except TimeoutException:
            print ( "Loading took too much time!" )
            # driver.get_screenshot_as_file('gold_page_loading_error.png')
        driver.implicitly_wait ( 10 )

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print ( "Page has", driver.title + " as Page title" )
        print ( "Test for Chrome is Done! Gold forever!" )
        driver.get_screenshot_as_file ( 'gold1.png' )

        # driver.save_screenshot('./UnitTests/gold1.png')

        def tearDown(self):
            self.driver.quit ()


class FirefoxSearch ( unittest.TestCase ):
    def setUp(self):
        self.driver = webdriver.Firefox ()
        self.driver.maximize_window ()

        # As per unittest module, individual test should start with test_

    def test_search_firefox(self):
        driver = self.driver
        driver.get ( "https://www.google.com" )
        self.assertIn ( "Google", driver.title )
        print ( "Page has", driver.title + " as Page title" )
        # check API response code
        print ( "Google Url has", requests.get ( "https://www.google.com" ).status_code, " as status Code" )
        if not "Google" in driver.title:
            raise Exception ( "Unable to load google page!" )

            # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait ( driver, 2 ).until ( EC.visibility_of_element_located ( (By.NAME, "q") ) )
            print ( "First Chrome Page is ready!" )
        except TimeoutException:
            print ( "Loading took too much time!" )
            # driver.get_screenshot_as_file("google_page_loading_error.png")
            # driver.save_screenshot('google_page_loading_error.png')

            # Checking page title for "Google" then print it
        self.assertIn ( "Google", driver.title )
        print ( "Page has", driver.title + " as Page title" )

        # workflow over "elem" variable to better code length

        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("wikipedia")
        # driver.find_element_by_name("q").send_keys(Keys.RETURN)

        elem = driver.find_element_by_name ( "q" )
        elem.clear ()
        elem.send_keys ( "Wikipedia" )
        elem.send_keys ( Keys.RETURN )
        driver.implicitly_wait ( 5 )  # wait max 5 sec

        assert "No results found." not in driver.page_source  # True or False

        # Driver waits until element Wikipedia will be clickable
        wait = WebDriverWait ( driver, 10 )
        wait.until ( EC.element_to_be_clickable ( (By.PARTIAL_LINK_TEXT, 'Wikipedia') ) )
        driver.find_element_by_partial_link_text ( "Wikipedia" ).click ()
        self.assertIn ( "Wikipedia", driver.title )
        print ( "Page has", driver.title + " as Page title" )
        print ( "Wikipedia Url has ", requests.get ( "https://www.wikipedia.org" ).status_code, " as status Code" )

        if not "Wikipedia" in driver.title:
            raise Exception ( "Unable to load Wikipedia page!" )

        # assert "No results found." not in driver.page_source

        # API response Status code check
        code = requests.get ( "https://www.wikipedia.org" ).status_code
        if code == 200:
            print ( "Wikipedia Url has correct", requests.get ( "https://www.wikipedia.org" ).status_code,
                    "status Code" )
        else:
            print ( "Wikipedia Url has", requests.get ( "https://www.wikipedia.org" ).status_code, "as status Code" )

        wait = WebDriverWait ( driver, 2 )

        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until ( EC.visibility_of_element_located ( (By.CLASS_NAME, "mw-wiki-logo") ) )
        wait.until ( EC.visibility_of_element_located ( (By.ID, "searchInput") ) )
        elem2 = driver.find_element_by_id ( "searchInput" )
        elem2.send_keys ( "Bread" )
        elem2.send_keys ( Keys.RETURN )
        driver.find_element_by_partial_link_text ( "Bread" ).click ()
        wait.until ( EC.visibility_of_element_located ( (By.ID, "firstHeading") ) )
        self.assertIn ( "Bread - Wikipedia", driver.title )
        print ( "Page has", driver.title + " as Page title" )
        if not "Bread" in driver.title:
            raise Exception ( "Unable to load Wikipedia Bread page!" )

        driver.find_element_by_xpath ( "//img[@alt='Loaves of bread in a basket']" ).click ()
        delay = 10  # 10 seconds

        print ( driver.find_element_by_xpath ( "//img[@class='mw-mmv-final-image jpg']" ) )
        delay = 20  # 10 seconds

        try:
            WebDriverWait ( driver, delay ).until (
                EC.presence_of_element_located ( (
                    By.XPATH, "//img[@src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3"
                              "%B6tchen.JPG/1024px-Korb_mit_Br%C3%B6tchen.JPG']") ) )
            print ( "Wikipedia Bread Page is ready!" )
            driver.get_screenshot_as_file ( 'ScreenshotBread_page.png' )
        except TimeoutException:
            print ( "Loading took too much time!" )
            # driver.get_screenshot_as_file('gold_page_loading_error.png')
        driver.implicitly_wait ( 10 )

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print ( "Page has", driver.title + " as Page title" )
        print ( "Test for Chrome is Done! Bread forever!" )
        driver.get_screenshot_as_file ( 'bread1.png' )

        # driver.save_screenshot('./UnitTests/gold1.png')

        def tearDown(self):
            self.driver.quit ()

# if __name__ == '__main__':
#     unittest.main()