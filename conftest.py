from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Only chrome browser is currently supported")
    parser.addoption('--language', action='store', default="ru")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test...")
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language") 
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_argument("--remote-debugging-port=9222")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser

    print("\nquit browser...")
    browser.quit()
