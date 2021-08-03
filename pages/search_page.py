from pages.base_page import BasePage
from pages.locators import SearchPageLocators

class SearchPage(BasePage):
    """
    Contains assert methods checking if functionality is working properseaasd sdsd
    """
    
    def check_search_results_contain_keyword(self, search_item):
        assert self.find_items_from_search_results(*SearchPageLocators.SEARCH_ITEMS, search_item), "Not all search results " \
                                                                                                   "include the keyword"

    def check_search_results(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULTS), "There aren't any search results"
    
    def can_click_on_sort_asc_items(self):
        assert self.click_on_sort_asc_items(*SearchPageLocators.SORT_DROPDOWN), "There's no dropdown for sorting items"
    
    def should_be_sorted_items_by_asc(self):
        assert self.find_sorted_asc_items(*SearchPageLocators.ITEM_PRICE), "The items are not sorted by asc"