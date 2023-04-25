from selenium.common import TimeoutException
from selenium.webdriver import Keys
import random
from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first': {
                'title': self.locators.SECTION_FIRST,
                'content': self.locators.SECTION_FIRST_CONTENT
            },
            'second': {
                'title': self.locators.SECTION_SECOND,
                'content': self.locators.SECTION_SECOND_CONTENT
            },
            'third': {
                'title': self.locators.SECTION_THIRD,
                'content': self.locators.SECTION_THIRD_CONTENT
            },
        }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_multi = self.element_is_clickable(self.locators.MULTI_COMPLETE)
        input_multi.send_keys(color)
        input_multi.send_keys(Keys.ENTER)
