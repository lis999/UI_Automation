import time
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertsFramesWindows:

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

    class TestAlerts:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "the alert was not displayed"

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_after_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "the alert was not displayed"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "the confirm box was not opened"

        def test_prompt_box_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_result = alert_page.check_prompt_alert()
            #assert alert_result == f"You entered {text}"\
            assert text in alert_result, "the prompt box result doesn't match with entered data"

    class TestFrames:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_big_frame = frame_page.check_frame('frame1')
            result_small_frame = frame_page.check_frame('frame2')
            assert result_big_frame == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_small_frame == ['This is a sample page', '100px', '100px'], "The frame does not exist"
