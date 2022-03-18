from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = driver.find_element(By.XPATH , value=("/html/body/div/form/div[1]/div[1]/input"))
    input1.send_keys('Fedor')
    input2 = driver.find_element(By.XPATH , value=("/html/body/div/form/div[1]/div[2]/input"))
    input2.send_keys('Trunchov')
    input3 = driver.find_element(By.XPATH , value=("/html/body/div/form/div[1]/div[3]/input"))
    input3.send_keys('FedTrunc@gmail.com')
    input4 = driver.find_element(By.XPATH , value=("/html/body/div/form/div[2]/div[1]/input"))
    input4.send_keys('+380970970977')
    input4 = driver.find_element(By.XPATH , value=("/html/body/div/form/div[2]/div[2]/input"))
    input4.send_keys('Zmerinka')
    
    

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR,value = "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME,value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()