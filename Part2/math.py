from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
   
    link = "http://suninjuly.github.io/math.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    
    x_elem = driver.find_element(By.XPATH,value='//*[@id="input_value"]')
    x_elem_text = x_elem.text
    y = calc(x_elem_text)
    print(y)
    form1 = driver.find_element(By.XPATH,value='//*[@id="answer"]')
    form1.send_keys(y)
    button = driver.find_element(By.XPATH,value='/html/body/div/form/div[2]/label')
    button.click()
    button2 = driver.find_element(By.XPATH,value='/html/body/div/form/div[4]/label')
    button2.click()
    button3 = driver.find_element(By.XPATH,value = '/html/body/div/form/button')
    button3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()