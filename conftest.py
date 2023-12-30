import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": rf"{os.path.dirname(os.path.abspath(__file__))}\artifacts\download_files"}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
