from generator.generator import *
from page_objects.pages.alerts_frame_windows_page import *


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = AlertsFrameWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            browser_windows_page.check_opened_new_tab()

        def test_new_window(self, driver):
            browser_windows_page = AlertsFrameWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            browser_windows_page.check_opened_new_window()