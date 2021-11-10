from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from functions import click, webdriver, xpaths, database
import os
import time
import numpy as np

url = 'https://www.tradingview.com/chart/awk7Das0/'  # enter your trading view profile link here.
# range = np.arange(min_value, max_value, increment)
# combinations = np.array(np.meshgrid(x, y, z)).T.reshape(-1,3)
r1 = np.arange(3, 10, 1)
r2 = np.arange(4, 20, 1)
r3 = np.arange(5, 40, 1)
r4 = np.arange(2, 5, 1)
r5 = np.arange(2, 5, 1)
r6 = np.arange(12, 15, 1)
r7 = np.arange(12, 15, 1)
combinations = np.array(np.meshgrid(r1, r2, r3, r4, r5, r6, r7)).T.reshape(-1,7)


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
            if n[0] == n[1] or n[1] == n[2] or n[0] == n[2]:
                continue
            for a in n:
                pos += 1
                click.input(a, pos, wait)
            click.close_settings()
            time.sleep(1.5)
            try:
                x = xpaths.report({'Fast': int(n[0]), 'Medium': int(n[1]), 'Slow': int(n[2]), 'K': int(n[3]), 'D': int(n[4]), 'RSI': int(n[5]), 'Stoch': int(n[6]),})
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
