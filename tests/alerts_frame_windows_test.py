import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab_result = new_tab_page.check_new_tab_opened()
            assert new_tab_result == "This is a sample page", "The new tab hasn't been opened"

        def test_new_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_window_result = new_tab_page.check_new_window_opened()
            assert new_window_result == "This is a sample page", "The new window hasn't been opened"
