from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from functions import click, webdriver, xpaths, database
import time
import numpy as np

url = 'https://www.tradingview.com/chart/awk7Das0/'

def run_script(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    return wait

if __name__ == '__main__':
    wait = run_script(webdriver.driver)
