#Для того чтобы гарантировать закрытие браузера и всех вкладок/окон, даже если произошла ошибка в предыдущих строках, проще всего #использовать конструкцию try/finally: 

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()