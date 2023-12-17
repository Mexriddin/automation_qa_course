from generator.generator import generate_person
from page_objects.pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            person = generate_person()
            text_box_page.fill_all_fields(person)
            text_box_page.check_filled_form(person)