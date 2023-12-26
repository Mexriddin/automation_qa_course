import time

from generator.generator import generate_person, generate_count_rows
from page_objects.pages.elements_page import *


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            person = generate_person()
            text_box_page.fill_all_fields(person)
            text_box_page.check_filled_form(person)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert output_checkbox == input_checkbox, "Checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            assert "Yes" == output_yes, "'Yes' have not been selected"
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            assert "Impressive" == output_impressive, "'Impressive' have not been selected"
            radio_button_page.click_on_the_radio_button("no")
            output_no = radio_button_page.get_output_result()
            assert "No" == output_no, "'No' have not been selected'"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = generate_person()
            web_table_page.add_new_person(person)
            web_table_page.check_added_new_person(person)

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = generate_person()
            web_table_page.add_new_person(person)
            web_table_page.search_some_person(person.first_name)
            web_table_page.check_search_person(person.last_name)

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = generate_person()
            web_table_page.add_new_person(person)
            person.age = random.randint(18, 60)
            web_table_page.search_some_person(person.first_name)
            web_table_page.update_person_info(person.age)
            web_table_page.check_updated_person_info(person.age)

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = generate_person()
            web_table_page.add_new_person(person)
            web_table_page.search_some_person(person.first_name)
            web_table_page.delete_person()
            web_table_page.check_deleted_person()

        def test_web_table_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = generate_person()
            web_table_page.change_rows_per_page(count)
            web_table_page.check_rows_per_page(count)

