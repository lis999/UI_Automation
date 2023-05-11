from pages.interactions_page import InteractionsPage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = (driver, "https://demoqa.com/sortable")
            sortable_page.open()
            pass
