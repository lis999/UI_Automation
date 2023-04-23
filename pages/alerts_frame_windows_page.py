import random
import time

from selenium.common import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_opened(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return new_tab_text

    def check_new_window_opened(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_window_text = self.element_is_present(self.locators.NEW_WINDOW_TEXT).text
        return new_window_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.AFTER_FIVE_SEC_ALERT_BUTTON).click()
        time.sleep(5)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()         # .accept() or .dismiss()
        text_result = self.element_is_present(self.locators.CONFIRM_BOX_ALERT_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()         # .accept() or .dismiss()
        text_result = self.element_is_present(self.locators.PROMPT_BOX_ALERT_RESULT).text
        return text, text_result
