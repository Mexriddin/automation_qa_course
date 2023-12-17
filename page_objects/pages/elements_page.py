from page_objects.pages.base_page import BasePage
from page_objects.locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, person):
        self.element_is_visibility(self.locators.FULL_NAME).send_keys(person.full_name)
        self.element_is_visibility(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visibility(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visibility(self.locators.PERMANENT_ADDRESS).send_keys(person.permanent_address)
        self.element_is_visibility(self.locators.SUBMIT_BUTTON).click()

    def check_filled_form(self, person):
        assert person.full_name == self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1], \
            "Full Name does not match"
        assert person.email == self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1], \
            "Email does not match"
        assert person.current_address == self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1],\
            "Current Address does not match"
        assert person.permanent_address == self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1], \
            "Permanent Address does not match"