from pages.search_page import SearchPage
from pages.variables import search_parameters
import pytest

@pytest.mark.parametrize('domain', ["ru"])
@pytest.mark.search_field
class TestSearchField:
    """
    Checks if search field can accept multiple
    string options.
    """
    @pytest.mark.xfail(reason="not all results're relevant to the keyword")
    def test_correct_input_search_field(self, browser, domain):
        link = f"https://www.ecwid.{domain}/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dress"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
        page.check_search_results_contain_keyword(search_item)

    @pytest.mark.xfail(reason="it's impossible to click on a search icon")
    def test_empty_input(self, browser, domain):
        link = f"https://www.ecwid.{domain}/demo/search"
        page = SearchPage(browser, link)
        page.open()
        page.click_on_search_field_button()
        page.check_search_results()

    @pytest.mark.parametrize("word", search_parameters)
    def test_search_field_inputs(self, browser, domain, word):
        link = f"https://www.ecwid.{domain}/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = f"{word}"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()

@pytest.mark.sort_by_asc
class TestSortByAsc:
    """
    Checks if sorting by asc is working correctly.
    """
    def test_click_on_asc_button(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        page.can_click_on_sort_asc_items()
        page.should_be_sorted_items_by_asc()
