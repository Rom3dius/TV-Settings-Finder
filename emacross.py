from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from functions import click, webdriver, xpaths, database
import os
import time
import numpy as np

url = 'https://www.tradingview.com/chart/awk7Das0/'  # enter your trading view profile link here.
# range = np.arange(min_value, max_value, increment)
# combinations = np.array(np.meshgrid(x, y, z)).T.reshape(-1,3)
r1 = np.arange(3, 100, 1)
r2 = np.arange(4, 100, 1)
combinations = np.array(np.meshgrid(r1, r2)).T.reshape(-1,2)

def run_script(driver):
    """find the best stop loss value."""
    db = database.DB()
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    time.sleep(10)
    click.strategy_tester()
    time.sleep(2)
    click.overview()
    time.sleep(1)
    try:
        click.perf_sum()
        time.sleep(1)
    except NoSuchElementException:
        time.sleep(1)
        click.perf_sum()

    print("Loading script...")
    try:
        for n in combinations:
            print(n)
            pos = -1
            click.settings_button(wait)
            if n[0] == n[1]:
                continue
            click.input(n[0], 0, wait)
            click.input(n[1], 1, wait)
            click.close_settings()
            time.sleep(3)
            try:
                x = xpaths.report({'Fast': int(n[0]), 'Slow': int(n[1])})
                db.append(x)
                del x
            except Exception as e:
                print(f"Exception: {e}")

    except KeyboardInterrupt:
         print("Detected interrupt! Printing results...")

    print("Net Profit... ")
    wr = db.index("NP")[-3:]
    print(wr)
    del wr

    print("Max Drawdown... ")
    md = db.index("MD")[-3:]
    print(md)
    del md

    if not os.path.exists('databases'):
        os.makedirs('databases')

    del db
    os.rename('db.json', f'databases/db_{round(time.time())}.json')

if __name__ == '__main__':
    run_script(webdriver.driver)
