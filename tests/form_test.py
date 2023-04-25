import time

from pages.form_page import FormsPage


class TestForms:
    class TestFormsPage:
        def test_form(self, driver):
            form_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            person_info = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [person_info.firstname + " " + person_info.lastname, person_info.email] == \
                   [result[0], result[1]], "the form hasn't been filled"
