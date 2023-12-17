import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
