from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))
      
    link = "http://suninjuly.github.io/get_attribute.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)

    input1 = driver.find_element(By.ID,value='treasure')
    input1_attr = input1.get_attribute('valuex')
    input2 = driver.find_element(By.XPATH,value='//*[@id="answer"]')
    input2.send_keys(calc(input1_attr))
    button = driver.find_element(By.ID,value='robotCheckbox')
    button.click()
    button2 = driver.find_element(By.ID,value='robotsRule')
    button2.click()
    button3 = driver.find_element(By.CSS_SELECTOR,value = '[type="submit"]')
    button3.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()