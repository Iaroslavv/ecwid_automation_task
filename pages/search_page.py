from pages.base_page import BasePage
from pages.locators import SearchPageLocators

class SearchPage(BasePage):
    
    def should_be_search_field(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_TEXT_FIELD), "There's no search field"
    
    def check_search_results_contain_keyword(self, search_item):
        assert self.find_items_from_search_results(*SearchPageLocators.SEARCH_ITEMS, search_item), "Not all search results " \
                                                                                                   "with the keyword are shown"


    def check_search_results(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULTS), "There aren't any search results"
    