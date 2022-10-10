from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your first name"')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[placeholder="Input your last name"')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.third[placeholder="Input your email"')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your phone:"')
    input4.send_keys("Number")
    input4 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[placeholder="Input your address:"')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()