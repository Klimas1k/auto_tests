from gettext import find
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))
      
    link = 'http://suninjuly.github.io/redirect_accept.html'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR,value='[type ="submit"]')
    button1.click()
    browser.switch_to.window(browser.window_handles[-1])
    elem = browser.find_element(By.ID,value='input_value')
    elem_text = elem.text
    elem_test = browser.find_element(By.ID,value='answer')
    elem_test.send_keys(calc(elem_text))
    submit = browser.find_element(By.CSS_SELECTOR,value='[type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()