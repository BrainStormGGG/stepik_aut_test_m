from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://demo.guru99.com/test/login.html'
s = Service('C:\geckodriver\geckodriver.exe')
browser = webdriver.Firefox(service=s)
browser.get(link)


def login(login: str, password: str):
    try:
        user_id = browser.find_element(By.XPATH, "//input[@type='text'][@name='email'][@id='email']")
        user_id.send_keys(login)
        pas = browser.find_element(By.XPATH, "//input[@type='password'][@name='passwd'][@id='passwd']")
        pas.send_keys(password)
        button = browser.find_element(By.XPATH, "//button[@type='submit'][@id='SubmitLogin']")
        button.click()
    finally:
        time.sleep(10)
        browser.quit()

login('mngr446178', 'YzArEmu') # / Correct user data
# login('dadsadad', 'adsadacx') / Noncorrect user data
