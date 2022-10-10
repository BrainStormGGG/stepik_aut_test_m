import math
import time
from selenium import webdriver
from  selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

#------Проверяем выбран ли people радио элемент по дефолту----
people_rule = browser.find_element(By.ID, 'peopleRule')
people_checked = people_rule.get_attribute('checked')
print("value of people radio: ", people_checked)
assert people_checked is not None, 'People radio is not selected by default'
#-----Конец проверки-------

#------Проверяем выбран ли robot радио элемент по дефолту----
robot_rule = browser.find_element(By.ID, 'robotsRule')
robot_checked = robot_rule.get_attribute('checked')
print("value of robot radio: ", robot_checked)
#-----Конец проверки-------

#------Проверяем выбран ли disable для кнопки по дефолту----
button_dis = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
button_disable = button_dis.get_attribute('disabled')
print("value of button: ", button_disable)
#-----Конец проверки-------

#-----Получаем видимый пользователю текст-----
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
#-----------
y = calc(x)

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)
robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
robot.click()
robot_rules = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
robot_rules.click()
button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")

button.click()

time.sleep(10)
browser.quit()




