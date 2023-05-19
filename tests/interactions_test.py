import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'the order of the list has not been changed'
            assert grid_before != grid_after, 'the order of the grid has not been changed'

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, 'no elements were selected'

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_f, min_f = resizable_page.change_size_resizable()
            # assert ('500px', '300px') == max_box, 'maximus size not equal to 500px, 300px'
            assert ('150px', '150px') == min_box, 'minimum size not equal to 150px, 150px'
            assert max_f != min_f, 'resizable has not been changed'
            print(max_box, min_box)
            print(max_f, min_f)

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'the element has not been dropped'

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', "the element has been accepted"
            assert accept == 'Dropped!', "the element has not been accepted"

        def test_prevent_propagation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propagation()
            assert not_greedy == 'Dropped!', 'The element text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'The element text has not been changed'
            assert greedy == 'Outer droppable', 'The element text has been changed'
            assert greedy_inner == 'Dropped!', 'The element text has not been changed'

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
