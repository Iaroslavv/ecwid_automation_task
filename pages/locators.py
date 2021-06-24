from selenium.webdriver.common.by import By

class SearchPageLocators:
    """
    Locators which are used to locate elements on the webpage in the methods in
    'base_page.py'.
    """
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.form-control__ico-btn.ec-text-muted")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.grid__products")
    SEARCH_ITEMS = (By.CSS_SELECTOR, "div.grid__products>div.grid-product >div.grid-product__wrap>div.grid-product__wrap-inner>a")
    ITEM_PRICE = (By.CSS_SELECTOR, ".grid-product__price-amount >div")
    SORT_DROPDOWN_BUTTONS = (By.XPATH, "//div[@class='ec-filter ec-filter--sortby ec-filter--section-sticky-bar']/div/div/div")
    SORT_ASC_BUTTON = (By.CSS_SELECTOR,"[for='radio-sortBy-priceAsc']")
