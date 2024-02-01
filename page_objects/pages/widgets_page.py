import time

import allure
from selenium.webdriver import Keys

from page_objects.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from page_objects.locators.widgets_page_locators import *


class AccordianPage(BasePage):
    locators = AccordianPageLocators()
    accordian = {
        'first': {
            'title': locators.SECTION_FIRST,
            'content': locators.SECTION_CONTENT_FIRST,
            'checker': locators.SECTION_FIRST_CHECKER
        },
        'second': {
            'title': locators.SECTION_SECOND,
            'content': locators.SECTION_CONTENT_SECOND,
            'checker': locators.SECTION_SECOND_CHECKER
        },
        'third': {
            'title': locators.SECTION_THIRD,
            'content': locators.SECTION_CONTENT_THIRD,
            'checker': locators.SECTION_THIRD_CHECKER
        }
    }

    def open_accordian_content(self, accordian_number):
        with allure.step(f'Open accordian: {accordian_number}'):
            self.scroll()
            section_title = self.element_is_visible(self.accordian[accordian_number]['title'])
            section_title.click()

    def check_accordian_content(self, accordian_number):
        with allure.step(f'Check accordian: {accordian_number}'):
            try:
                assert self.element_is_visible(self.accordian[accordian_number]['checker'])
                assert self.element_is_visible(self.accordian[accordian_number]['content']).text is not None
            except TimeoutException:
                self.open_accordian_content(accordian_number)


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self, colors):
        with allure.step(f'Filling with: {colors}'):
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            for color in colors.colors_list:
                input_multi.send_keys(color)
                input_multi.send_keys(Keys.ENTER)

    def check_value_multi_input(self, count):
        with allure.step(f'Check value multi input: {count}'):
            value_multi = self.elements_are_visible(self.locators.MULTI_VALUE)
            assert len(value_multi) == count
