from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ITEMS_LIST = (By.XPATH,"//div[@class='inventory_item_name']")
    ITEMS_TITLE = (By.XPATH,"//*[@class='title']")
    ITEM_PRICE = (By.XPATH,"//*[@id='inventory_container']/div/div/div[2]/div[2]/div")
    BUY_BUTTON = (By.XPATH,"//*[@id='shopping_cart_container']/a")
    ADD_TO_CARD = (By.XPATH,"//*[@class='pricebar']/button[text()='Add to cart']")
    REMOVE_FROM_CARD = (By.XPATH,"//button[text()='Remove']")
    ITEMS_IN_BASKET = (By.XPATH,"//*[@class='shopping_cart_badge']")
    SORT_BUTTON = (By.XPATH,"//*[@class='product_sort_container']")
    ACTIVE_OPTIONS = (By.XPATH,"//*[@class='active_option']")
    SORT_BUTTON_AZ = (By.XPATH,"//*[@class='product_sort_container']/option[1]")
    SORT_BUTTON_ZA = (By.XPATH,"//*[@class='product_sort_container']/option[2]")
    SORT_BUTTON_LOHI = (By.XPATH,"//*[@class='product_sort_container']/option[3]")
    SORT_BUTTON_HILO = (By.XPATH,"//*[@class='product_sort_container']/option[4]")

    def __init__(self, driver):
        super().__init__(driver)

    def addItemsToCard(self):
        items=self.findAll(self.ADD_TO_CARD)
        for i in range(len(items)-1):
            self.click_element(items[i])
        return items
    def checkAddItemsInBasket(self):
        assert int(self.get_element_text(self.ITEMS_IN_BASKET))==len(self.addItemsToCard())



