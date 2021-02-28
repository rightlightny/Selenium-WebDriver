from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()

print(driver.find_element(By.XPATH, "//a[@rel='home']").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))

driver.implicitly_wait(5)
assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print(driver.title)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")

driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Alexey Sharunov")
driver.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("Alexey@mail.com")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hello world!")
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

#driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)
#driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").send_keys('\n') #находит элемент и кликает по нему даже если не видит его
#driver.find_element(By.XPATH, "//a[contains(.,'go back')]").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(driver.find_element_by_xpath("//button[contains(text(),'Submit')]").get_attribute("type"))

# quit from browser
driver.quit()

# closing browser tab
# driver.close()