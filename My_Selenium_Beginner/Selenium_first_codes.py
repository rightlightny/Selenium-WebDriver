# THIS is ONE OF FIRST CODES

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://qasvus.wordpress.com')  # 2. Go to : https://qasvus.wordpress.com
driver.maximize_window()  # 3. Use Chrome browser
sleep(3)
pop_up = driver.find_element_by_xpath('//*[@value = "Close and accept"]')
if pop_up:
    pop_up.click()


# 7. Verify (do assert) "California Real Estate" in  website title
assert 'California Real Estate' in driver.title
print(driver.title)  # 8. Print website title

# 5. Print link(href) for header message "California Real Estate"
# 6. Print link(src) for first home image under "About us"

print(driver.find_element_by_link_text('California Real Estate').get_attribute('href'))
print(driver.find_element_by_xpath('//img[@class="wp-image-55"]').get_attribute('src'))

# 9. Find "Send Us a Message" and verify it's present on the web page
driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]")

# 10. Fill out and send the message form
driver.find_element_by_id("g2-name").send_keys('John')
driver.find_element_by_id('g2-email').send_keys('john@gmail.com')
driver.find_element_by_id('contact-form-comment-g2-message').send_keys('Some text')

body = driver.find_element_by_id('page')
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").submit()

sleep(3)
# 11. When the message will be send:
# - Find "go back" button (link) and using one of the tags above click it to go back to the Main page.
go_back = driver.find_element_by_link_text('go back')
try:
    go_back.click()
except ElementClickInterceptedException:
    body.send_keys(Keys.PAGE_DOWN)
    go_back.click()


sleep(3)
# 12. Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
print(driver.find_element_by_xpath("//button[contains(text(),'Submit')]").get_attribute('type'))
print(driver.title)

driver.quit()