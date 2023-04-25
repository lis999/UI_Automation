from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    AFTER_FIVE_SEC_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    CONFIRM_BOX_ALERT_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX_ALERT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMALL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    BIG_FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    SMALL_FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    SMALL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body'] p")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    LARGE_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")

