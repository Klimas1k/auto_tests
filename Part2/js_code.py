from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

    link = ' http://SunInJuly.github.io/execute_script.html'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    num = browser.find_element(By.ID,value='input_value')
    num_text = num.text
    input2 = browser.find_element(By.XPATH,value='//*[@id="answer"]')
    input2.send_keys(calc(num_text))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button1 = browser.find_element(By.ID,value='robotCheckbox')
    button1.click()
    button2 = browser.find_element(By.ID,value='robotsRule')
    button2.click()
    button.click()  
    
    
finally: 
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   