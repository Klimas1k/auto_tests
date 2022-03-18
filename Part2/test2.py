from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
verify = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )

button = browser.find_element(By.ID,"book")
button.click()
x_elem = browser.find_element(By.XPATH,value='//*[@id="input_value"]')
x_elem_text = x_elem.text
y = calc(x_elem_text)
form1 = browser.find_element(By.XPATH,value='//*[@id="answer"]')
form1.send_keys(y)
button = browser.find_element(By.ID,"solve")
button.click()


time.sleep(10)
browser.quit()