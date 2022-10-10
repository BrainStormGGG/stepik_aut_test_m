import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dict = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dict, 'fdfdfd.txt')

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]")
input1.send_keys('Alexey')

input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
input2.send_keys('Laparevich')

input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
input3.send_keys('Alaparevich@gmail.com')

input4 = browser.find_element(By.XPATH, "//input[@id='file']")
input4.send_keys(file_path)

button = browser.find_element(By.XPATH, "//button")
button.click()

