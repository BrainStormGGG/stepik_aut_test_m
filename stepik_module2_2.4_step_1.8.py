import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100')
)
button = browser.find_element(By.XPATH, "//button[@id='book']")
button.click()

def log(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
y = log(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)

button2 = browser.find_element(By.XPATH, "//button[@id='solve']")
button2.click()

time.sleep(10)
browser.quit()
