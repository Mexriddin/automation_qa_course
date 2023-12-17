import random

from page_objects.pages.base_page import BasePage
from page_objects.locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, person):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(person.full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(person.permanent_address)
        self.remove_ad()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_filled_form(self, person):
        assert person.full_name == self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1], \
            "Full Name does not match"
        assert person.email == self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1], \
            "Email does not match"
        assert person.current_address == self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[
            1], \
            "Current Address does not match"
        assert person.permanent_address == \
               self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1], \
            "Permanent Address does not match"


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 5
        while count != 0:
            item = item_list[random.randint(0, len(item_list) - 1)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM).text
            if "." in title_item:
                file_name = title_item.split(".")[0].replace(" ", "")
                data.append(file_name.lower())
            else:
                data.append(title_item.lower())
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text.replace(" ", "").lower())
        return data
