from selenium.webdriver.common.by import By
import time

class TestPage():
    def test_button_presented (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        time.sleep(3)

        # проверка что кнопка есть
        button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button, 'element BUTTON not found'