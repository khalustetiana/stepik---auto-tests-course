from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x,y):
        return str(int(x) + int(y))
		
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = calc(x,y)
	
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z) # ищем элемент с текстом "Python
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
		
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
	

# не забываем оставить пустую строку в конце файла

