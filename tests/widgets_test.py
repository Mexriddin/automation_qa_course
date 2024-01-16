import random

from page_objects.pages.widgets_page import *


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            section = random.choice(['first', 'second', 'third'])
            accordian_page.open_accordian_content(section)
            accordian_page.check_accordian_content(section)
