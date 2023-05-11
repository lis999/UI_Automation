from locators.interactions_page_locators import InteractionsPageLocators
from pages.base_page import BasePage


class InteractionsPage(BasePage):
    locators = InteractionsPageLocators()

    def form_result(self):
