from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located(locator))

    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def remove_ad(self):
        self.driver.execute_script('document.getElementById("Ad.Plus-728x90").style.display="none"')
        self.driver.execute_script('document.getElementById("adplus-anchor").style.display="none"')
