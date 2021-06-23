from pages.search_page import SearchPage
import pytest

@pytest.mark.skip
def test_should_be_search_field(browser):
    link = "https://www.ecwid.ru/demo/search"
    page = SearchPage(browser, link)
    page.open()
    page.should_be_search_field()

def test_correct_input_search_field(browser):
    link = "https://www.ecwid.ru/demo/search"
    page = SearchPage(browser, link)
    page.open()
    search_item = "dress"
    page.input_text_into_search_field(search_item)
    page.check_search_results()
    page.check_search_results_contain_keyword(search_item)

