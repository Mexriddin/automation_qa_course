import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open url: {self.url}"):
            self.driver.get(self.url)

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def alert_is_visible(self):
        return self.wait.until(EC.alert_is_present())

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

    def element_attribute_is_has_value(self, locator, atr, value):
        return self.wait.until(EC.text_to_be_present_in_element_attribute(locator, atr, value))

    def element_has_text(self, locator, text):
        elements = self.elements_are_visible(locator)
        for i in elements:
            if i.text == text:
                return i

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 350);")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def remove_ad(self):
        self.driver.execute_script('document.getElementById("Ad.Plus-728x90").style.display="none"')
        self.driver.execute_script('document.getElementById("adplus-anchor").style.display="none"')

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")
