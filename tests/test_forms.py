from generator.generator import *
from page_objects.pages.form_page import *


class TestForms:
    def test_student_registration_form(self, driver):
        practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
        practice_form_page.open()
        student = generate_student()
        picture = generate_jpeg()
        practice_form_page.fill_form_fields(student, picture)
        practice_form_page.check_registered_student(student)