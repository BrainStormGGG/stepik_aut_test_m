import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

"""Переходит к alert"""
button1 = browser.find_element(By.XPATH, "//button")
button1.click()

"""Отвечаем на alert"""
alert = browser.switch_to.alert
alert.accept()

"""Решаем капчу и отправляем решение"""
def log(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = log(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)

button2 = browser.find_element(By.XPATH, "//button")
button2.click()

time.sleep(10)
browser.quit()