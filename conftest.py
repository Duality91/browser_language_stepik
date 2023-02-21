import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
# Вы импортируете два одинаковых имени, могут быть ошибки
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language", action="store", default=None, help="Choose language: ru or fr"
    )


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = chrome_options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        options = firefox_options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()