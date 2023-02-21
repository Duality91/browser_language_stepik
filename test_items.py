import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_browser(browser):
    browser.get(url)
    browser.maximize_window()
    scroll_vаlue = 300
    scroll_by = f'window.scrollBy(0, {scroll_vаlue});'
    browser.execute_script(scroll_by)
    assert is_element_present(browser) == True, "корзинка не найдена"
    print("Кнопка добавления в корзину найдена")
    time.sleep(5)


def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, "form button.btn-primary")
        return True
    except:
        return False