import allure

from page_objects.pages.alerts_frame_windows_page import *


@allure.epic("Elements")
class TestAlertsFrameWindows:
    @allure.feature("Browser Windows")
    class TestBrowserWindows:
        @allure.title("Check new tab")
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            browser_windows_page.check_opened_new_tab()

        @allure.title("Check new windows")
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            browser_windows_page.check_opened_new_window()

    @allure.feature("Alerts")
    class TestAlerts:
        @allure.title("Check see alert")
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_page.check_alert()

        @allure.title("Check alert appear 5 sec")
        def test_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_page.check_timer_alert()

        @allure.title("Check confirm alert")
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_page.check_confirm_alert()

        @allure.title("Check prompt alert")
        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_page.check_prompt_alert()

    @allure.feature("Frames")
    class TestFrames:
        @allure.title("Check frames")
        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            frames_page.check_frame('frame1')
            frames_page.check_frame('frame2')

    @allure.feature("NestedFrames")
    class TestNestedFrames:
        @allure.title("Check nested frames")
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            nested_frames_page.check_nested_frame()

    @allure.feature("Modal dialogs")
    class TestModalDialogs:
        @allure.title("Check modal dialogs")
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            modal_dialogs_page.check_modal_dialogs()