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
        """
        self.browser.implicitly_wait(25)
        self.browser.find_element(*SearchPageLocators.SEARCH_TEXT_FIELD).send_keys(input_text)
    
    def click_on_search_field_button(self):
        self.browser.implicitly_wait(5)
        self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON).click()
        time.sleep(10)

    def is_not_element_present(self, how, what, timeout=4):
        """
        Checks if the element's presented on the page. If it appears, the test will fail
        and vice versa.
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_element_present(self, how, what):
        """
        Checks if element is presented on the page
        """
        try:
            self.browser.implicitly_wait(10)
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def find_items_from_search_results(self, how, what, search_item):
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
        print("NUMBER_ITEMS", number_items)
        print("NUMBER_SEARCH_ITEM", number_search_item)
        return number_items == number_search_item
