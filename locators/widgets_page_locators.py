from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:
    MULTI_COMPLETE = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")


