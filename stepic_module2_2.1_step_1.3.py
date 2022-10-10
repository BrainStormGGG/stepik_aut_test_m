import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

first_number_str = browser.find_element(By.XPATH, "//span[@class='nowrap'][@id='num1']")
first_number = first_number_str.text

second_number_str = browser.find_element(By.XPATH, "//span[@class='nowrap'][@id='num2']")
second_number = second_number_str.text

summ = int(first_number) + int(second_number)

select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(summ))

button = browser.find_element(By.XPATH, '//button')
button.click()

time.sleep(10)
browser.quit()