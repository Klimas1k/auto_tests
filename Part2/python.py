from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)

    input1 = driver.find_element(By.NAME, value='first_name')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME,value ='last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME,value = 'city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID,value ='country')
    input4.send_keys("Russia")
    button = driver.find_element(By.XPATH,value ="/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций= driver.quit()
    driver.quit()