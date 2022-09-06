from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

# добавление опции language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

# создание браузера
@pytest.fixture(scope="function")
def browser(request):
    print("\nbrowser starts..")
    user_language = request.config.getoption("language")
    # настройка опций браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()