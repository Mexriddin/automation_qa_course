import random

import allure

from page_objects.pages.base_page import BasePage
from page_objects.locators.alerts_frame_windows_page_locators import *


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        with allure.step("Check opened new tab"):
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            h1 = self.element_is_visible(self.locators.HEADING_IN_PAGE).text
            assert "This is a sample page" == h1, "The new tab has not opened or an incorrect tab has opened"

    def check_opened_new_window(self):
        with allure.step("Check opened new window"):
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            h1 = self.element_is_visible(self.locators.HEADING_IN_PAGE).text
            assert "This is a sample page" == h1, "The new window has not opened or an incorrect wi has opened"


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert(self):
        with allure.step("Check alert"):
            self.element_is_visible(self.locators.ALERT_BUTTON).click()
            alert = self.driver.switch_to.alert
            assert "You clicked a button" == alert.text, "The alert has not opened or an incorrect alert has opened"

    def check_timer_alert(self):
        with allure.step("Check appear alert"):
            self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
            alert = self.alert_is_visible()
            assert "This alert appeared after 5 seconds" == alert.text, "This alert appeared after 5 seconds has not been"

    def check_confirm_alert(self):
        with allure.step("Check confirm alert"):
            self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
            assert "You selected Ok" == result, "You selected Ok"

    def check_prompt_alert(self):
        with allure.step("Check prompt alert"):
            text = f"autotest{random.randint(1, 100000)}"
            self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()
            result = self.element_is_visible(self.locators.PROMPT_RESULT).text
            assert text in result, f"You entered {text}"


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_number):
        with allure.step(f"Check frame {frame_number}"):
            if frame_number == 'frame1':
                frame = self.element_is_present(self.locators.FIRST_FRAME)
                assert frame.size['width'] == 500
                assert frame.size['height'] == 350
                self.driver.switch_to.frame(frame)
            if frame_number == 'frame2':
                frame = self.element_is_present(self.locators.SECOND_FRAME)
                assert frame.size['width'] == 100
                assert frame.size['height'] == 100
                self.driver.switch_to.frame(frame)
            heading_in_iframe = self.element_is_present(self.locators.HEADING_IN_IFRAME).text
            self.driver.switch_to.default_content()
            assert heading_in_iframe == "This is a sample page", "The frame does not exist"


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        with allure.step("Checking nested frame"):
            with allure.step("Checking parent frame"):
                parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
                self.driver.switch_to.frame(parent_frame)
                assert self.element_is_present(self.locators.PARENT_FRAME_TEXT).text == 'Parent frame', \
                    'The parent frame does not exist'
            with allure.step("Checking child frame"):
                child_frame = self.element_is_present(self.locators.CHILD_FRAME)
                self.driver.switch_to.frame(child_frame)
                assert self.element_is_present(self.locators.CHILD_FRAME_TEXT).text == 'Child Iframe', \
                    "The child frame does not exist"


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self):
        with allure.step("Checking modal dialogs"):
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
            small_title = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
            small_body = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
            self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()

            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
            large_title = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
            large_body = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
            self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()

            assert len(small_body) < len(large_body), 'Text from small dialog is less than text from large dialog'
            assert small_title == 'Small Modal', 'The header is not "Small Modal"!'
            assert large_title == 'Large Modal', 'The header is not "Large Modal"!'
