from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(num1,num2):
        sum = int(num1.text) + int(num2.text)
        
    link = 'http://suninjuly.github.io/selects2.html'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    
    num1 = driver.find_element(By.ID,value='num1')
    num1_value = int(num1.text)
    num2 = driver.find_element(By.ID,value='num2')
    num2_value = int(num2.text)
    sum = str(num1_value + num2_value)
    select = Select(driver.find_element(By.TAG_NAME,value="select"))
    select.select_by_value(sum)
    submit = driver.find_element(By.CSS_SELECTOR,value='[type="submit"]')
    submit.click()   
    
    
    
finally: 
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()   