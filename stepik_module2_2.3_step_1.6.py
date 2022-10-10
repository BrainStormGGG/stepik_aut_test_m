import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
"""Находим и нажимаем на нужную кнопку"""
button = browser.find_element(By.XPATH, "//button[contains(@class, 'trollface')]")
button.click()

"""Переходим открывшуюся вкладку"""
new_window = browser.window_handles[-1]
browser.switch_to.window(new_window)

"""Решаем каптчу на ссайте"""
def captcha(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = captcha(x)

"""Вводим решение каптчи в поле"""
answer = browser.find_element(By.XPATH, "//input[@id='answer']")
answer.send_keys(y)

"""Отправляем форму"""
button_submit = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
button_submit.click()

time.sleep(10)
browser.quit()