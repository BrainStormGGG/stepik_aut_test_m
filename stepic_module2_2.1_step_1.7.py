import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)


def lg(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element(By.XPATH, "//img[@valuex]")
    x = x_element.get_attribute('valuex')
    y = lg(x)

    input1 = browser.find_element(By.XPATH, "//input[@type='text']")
    input1.send_keys(y)

    robot_check = browser.find_element(By.XPATH, "//input[@type='checkbox'][@id='robotCheckbox']")
    robot_check.click()

    robot_rule = browser.find_element(By.XPATH, "//input[@type='radio'][@id='robotsRule']")
    robot_rule.click()

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()



