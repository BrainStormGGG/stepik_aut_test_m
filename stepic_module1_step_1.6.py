import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e)*10000))

    link_text = browser.find_element(By.LINK_TEXT, text)
    link_text.click()
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Alexey")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Laparevich")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Minsk')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Belarus')
    button = browser.find_element(By.XPATH, 'btn-default')
    button.click()
    browser.find_element()

finally:
    time.sleep(30)
    browser.quit()

