import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)


def ln(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = ln(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)

robot = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
robot.click()

robots_rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
robots_rule.click()


button = browser.find_element(By.TAG_NAME, "button")
#Скрипт проскроливает страницу пока кнопка будет не перекрыта другим объектом.
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
browser.quit()