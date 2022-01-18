from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://facebook.com')
time.sleep(2)
driver.find_element_by_id('email').send_keys('nguyennhat74')
time.sleep(2)
driver.find_element_by_id('pass').send_keys('nguyenphinhat2k')
time.sleep(2)
driver.find_element_by_name('login').click()