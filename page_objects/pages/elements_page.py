import os
import random
import time
import requests
from selenium.common import TimeoutException

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
            assert self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text == "You have done a right click", \
                "The right click button was not clicked"
        if click_type == "click":
            assert self.element_is_visible(self.locators.SIMPLE_CLICK_MESSAGE).text == "You have done a dynamic click", \
                "The dynamic click button was not clicked"


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        simple_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert requests.get(link_href).status_code == 200
        assert self.driver.current_url == link_href, "The link is broken or url is incorrect"

    def check_broken_link(self):
        simple_link = self.element_is_visible(self.locators.BAD_REQUEST)
        link_href = simple_link.get_attribute("href")
        assert requests.get(link_href).status_code == 400, "The link works or the status code in son 400"


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self, file):
        self.element_is_visible(self.locators.UPLOAD_BUTTON).send_keys(file)

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()
        time.sleep(.5)
        return self.element_is_visible(self.locators.DOWNLOAD_BUTTON).get_attribute('download')

    def check_upload_file(self, file_name):
        file = self.element_is_visible(self.locators.UPLOADED_FILE).text.split("\\")[-1]
        assert file == file_name.split("\\")[-1], f"The file: {file_name} has not been uploaded"

    def check_download_file(self, downloaded_file):
        download_files = os.listdir(f"{os.path.dirname(os.getcwd())}\\artifacts\\download_files")
        assert downloaded_file in download_files, f"The file: {downloaded_file} has not been downloaded"


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_changed_color(self):
        before_color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        self.element_attribute_is_has_value(self.locators.COLOR_CHANGE_BUTTON,
                                            'class', 'text-danger')
        after_color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        assert before_color_button is not after_color_button, f"The button color has not been changed"

    def check_appear_button(self):
        state = True
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            state = False
        assert state, "The button has not been appeared after 5 second"

    def check_enabled_button(self):
        state = True
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            state = False
        assert state, "The button has not been enabled after 5 second"
