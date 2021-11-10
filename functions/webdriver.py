from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import settings


def create_driver():
    """Creating driver."""
    options = Options()
    options.headless = True  # Change To False if you want to see Firefox Browser Again.
    profile = webdriver.FirefoxProfile(
        settings.webdriver_path)
    driver = webdriver.Firefox(profile, options=options, executable_path=GeckoDriverManager().install())
    return driver


driver = create_driver()
wait = WebDriverWait(driver, 5)
