from selenium.common.exceptions import NoSuchElementException,TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import SearchPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, browser: str, url: str, timeout=20):
        """Class constructor.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        self.timeout = timeout
    
    def open(self):
        """ 
        Opens the page using the method (get)
        """
        self.browser.get(self.url)
    
    def input_text_into_search_field(self, input_text):
        """
        Inputs text into the search field
        :param input_text:
        """
        self.browser.implicitly_wait(25)
        self.browser.find_element(*SearchPageLocators.SEARCH_TEXT_FIELD).send_keys(input_text)
    
    def click_on_search_field_button(self):
        self.browser.implicitly_wait(5)
        self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON).click()
        time.sleep(5)
    
    def is_element_present(self, how, what):
        """
        Checks if element is presented on the page
        :param how: the way how searching functions
        :param what: what to look for
        """
        try:
            self.browser.implicitly_wait(15)
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def find_items_from_search_results(self, how, what, search_item):
        """
        Checks if there are items appeared after clicking on search button
        :param how: the way how searching functions
        :param what: what to look for
        :param search_item: the item(s) needed to be found
        """
        try:
            self.browser.implicitly_wait(5)
            items = self.browser.find_elements(how, what)
            list_items = [item.get_attribute("title") for item in items]
            time.sleep(1)
            lower_list_items = [word.lower() for word in list_items if word.lower()]
            number_items = len(lower_list_items)
            number_search_item = sum((word.count(search_item) for word in lower_list_items))
        except (NoSuchElementException, StaleElementReferenceException):
            return False
        return number_items == number_search_item
    
    def find_sorted_asc_items(self, how, what):
        """
        Checks if the items were sorted by asc
        :param how: the way how searching functions
        :param what: what to look for
        """
        try:
            self.browser.implicitly_wait(15)
            item_price = self.browser.find_elements(how, what)
            list_items_price = [price.text for price in item_price]
            make_items_float = [float(string.strip('$')) for string in list_items_price]
        except (NoSuchElementException, StaleElementReferenceException):
            return False
        return make_items_float[0] < make_items_float[-1]

    def click_on_sort_asc_items(self, how, what):
        """
        Checks if the sorting is working 
        :param how: the way how searching functions
        :param what: what to look for
        """
        try:
            self.browser.implicitly_wait(35)
            sort_drop_down = self.browser.find_element(how, what)
            sort_drop_down.click()
            find_sort_by_asc = self.browser.find_element(*SearchPageLocators.SORT_ASC_BUTTON)
            find_sort_by_asc.click()
        except (NoSuchElementException, TimeoutException):
            return False
        return True
