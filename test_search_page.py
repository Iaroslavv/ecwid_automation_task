import pages
from pages.search_page import SearchPage
import pytest

class TestSearchField:
    
    def test_should_be_search_field(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        page.should_be_search_field()
    
    def test_correct_input_search_field(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dress"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
        page.check_search_results_contain_keyword(search_item)

    
    def test_empty_input(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        page.click_on_search_field_button()
        page.check_search_results()
    
    def test_missing_letter_input(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "drss"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
    
    def test_search_item_with_extra_letter(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dressg"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
        
    def test_symbol_between_search_items(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "black.dress"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
    
    def test_symbol_at_the_end_search_item(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dress#"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()

    
    def test_symbol_before_search_item(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "%&dress"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()

    
    def test_letter_before_search_item(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "hdress"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
    
    def test_multiple_search_items(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dress shorts surf woven"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
    
    
    def test_plural_search_item(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "dresses"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()

    
    def test_synonym_for_search_item(self, browser):
        link = "https://www.ecwid.ru/demo/search"
        page = SearchPage(browser, link)
        page.open()
        search_item = "shirt"
        page.input_text_into_search_field(search_item)
        page.click_on_search_field_button()
        page.check_search_results()
