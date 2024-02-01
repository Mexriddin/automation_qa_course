from datetime import datetime
import os
import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": rf"{os.path.dirname(os.path.abspath(__file__))}\artifacts\download_files"}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs['driver']
        take_screenshot(driver, item.nodeid)


def take_screenshot(driver, nodeid: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{nodeid}_{now}.png".replace("/", "_").replace("::", "__")
    driver.save_screenshot(f"screenshots/{filename}")
    allure.attach(driver.get_screenshot_as_png(), name=filename, attachment_type=allure.attachment_type.PNG)