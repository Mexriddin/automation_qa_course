import allure
from selenium.webdriver import Keys
from page_objects.pages.base_page import BasePage
from page_objects.locators.forms_page_locators import *


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_form_fields(self, student, picture):
        self.remove_ad()
        self.remove_footer()
        self.go_to_element(self.element_is_present(self.locators.SUBMIT_BUTTON))
        with allure.step("Fill in all fields"):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(student.first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(student.last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(student.email)
            self.element_has_text(self.locators.GENDERS, student.gender).click()
            self.element_is_visible(self.locators.MOBILE).send_keys(student.mobile)
            self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(student.date_of_birth + Keys.ENTER)
            for subject in student.subjects:
                self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
                self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
            self.element_has_text(self.locators.HOBBIES, student.hobby).click()
            self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(picture)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(student.current_address)
            self.element_is_visible(self.locators.INPUT_STATE).send_keys("NCR")
            self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.ENTER)
            self.element_is_visible(self.locators.INPUT_CITY).send_keys("Delhi")
            self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.ENTER)
        with allure.step("Click submit button"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def check_registered_student(self, student):
        with (allure.step("Check filled_form")):
            results_data = self.elements_are_visible(self.locators.RESULT_TABLE)
            result_string = " ".join([row.text for row in results_data])
            attributes_to_check = ['first_name', 'last_name', 'email', 'gender', 'hobby', 'mobile']
            for attribute in attributes_to_check:
                with allure.step(f"Check {attribute}"):
                    assert getattr(student, attribute) in result_string, "The form has not been filled"
