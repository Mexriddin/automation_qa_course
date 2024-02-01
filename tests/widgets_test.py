import random

import allure

from generator.generator import generate_colors
import time

from page_objects.pages.widgets_page import *


@allure.epic("Elements")
class TestWidgets:
    @allure.feature("Accordian")
    class TestAccordian:
        @allure.title("Check accordian")
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            section = random.choice(['first', 'second', 'third'])
            accordian_page.open_accordian_content(section)
            accordian_page.check_accordian_content(section)

    @allure.feature("AutoComplete")
    class TestAutoComplete:
        @allure.title("Check autocomplete")
        def test_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = generate_colors(2)
            autocomplete_page.fill_multi_input(colors)
            autocomplete_page.check_value_multi_input(2)
