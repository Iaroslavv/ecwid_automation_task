from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.form-control__ico-btn.ec-text-muted")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.grid__products")
    SEARCH_ITEMS = (By.CSS_SELECTOR, "div.grid__products>div.grid-product >div.grid-product__wrap>div.grid-product__wrap-inner>a")

    