import random
import time

from selenium.webdriver.support.select import Select

from page_objects.pages.base_page import BasePage
from page_objects.locators.elements_page_locators import *


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


class RadioButtonPage(BasePage):
    locators = RadioButtonsPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO_BUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
            'no': self.locators.NO_RADIO_BUTTON
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_new_person(self, person):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.AGE).send_keys(person.age)
        self.element_is_visible(self.locators.SALARY).send_keys(person.salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(person.department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_added_new_person(self, person):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        person_data = [person.first_name, person.last_name,
                       str(person.age), person.email,
                       str(person.salary), person.department]
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        for i in data:
            if person_data is i:
                continue
            else:
                AssertionError("Person is not added")

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.INPUT_SEARCH).clear()
        self.element_is_visible(self.locators.INPUT_SEARCH).send_keys(key_word)

    def check_search_person(self, search_word):
        person = self.element_is_present(self.locators.FULL_PEOPLE_LIST).text.splitlines()
        assert str(search_word) in person, "The person was not found in the table"

    def update_person_info(self, update_age):
        self.element_is_visible(self.locators.EDIT_SPAN).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(update_age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_updated_person_info(self, update_age):
        person = self.element_is_present(self.locators.FULL_PEOPLE_LIST).text.splitlines()
        assert str(update_age) in person, "The person info has not been edited"

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_SPAN).click()

    def check_deleted_person(self):
        assert self.element_is_visible(self.locators.NO_ROWS_FOUND).text == "No rows found", \
            "The deleted person should not have been found"

    def change_rows_per_page(self, count):
        count_row_select = self.element_is_visible(self.locators.SELECT_ROWS_PER_PAGE)
        self.go_to_element(count_row_select)
        select_count_rows = Select(count_row_select)
        select_count_rows.select_by_value(str(count))

    def check_rows_per_page(self, count):
        rows_list = self.elements_are_visible(self.locators.FULL_PEOPLE_LIST)
        assert len(rows_list) == count, f"There should be {count} rows in the page"


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, click_type):
        if click_type == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        if click_type == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        if click_type == "click":
            self.element_is_visible(self.locators.SIMPLE_CLICK_BUTTON).click()

    def check_clicked_button(self, click_type):
        if click_type == "double":
            assert self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text == "You have done a double click", \
                "The double click button was not clicked"
        if click_type == "right":
            assert self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text == "You have done a right click",\
                "The right click button was not clicked"
        if click_type == "click":
            assert self.element_is_visible(self.locators.SIMPLE_CLICK_MESSAGE).text == "You have done a dynamic click", \
                "The dynamic click button was not clicked"
