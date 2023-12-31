from page_objects.pages.base_page import BasePage
from page_objects.locators.alerts_frame_windows_page_locators import *


class AlertsFrameWindowsPage(BasePage):
    locators = AlertsFrameWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        h1 = self.element_is_visible(self.locators.HEADING_IN_PAGE).text
        assert "This is a sample page" == h1, "The new tab has not opened or an incorrect tab has opened"

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        h1 = self.element_is_visible(self.locators.HEADING_IN_PAGE).text
        assert "This is a sample page" == h1, "The new window has not opened or an incorrect wi has opened"