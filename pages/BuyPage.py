from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class BuyPage(BasePage):
    buy_page_title = (By.XPATH,"//span[@class='title']")
    items_on_buy_page = (By.XPATH,"//*[@class='inventory_item_name']")
    remove_button = (By.XPATH,"//button[text()='Remove']")
    backToShopping_button = (By.XPATH,'//*[@id="continue-shopping"]')
    checkout_button = (By.XPATH,"//*[@id='checkout']")

    def __init__(self, driver):
        super().__init__(driver)

    def check_page(self):
        assert self.get_element_text(self.buy_page_title)=="YOUR CART"

    def check_itemsOnPage(self):
        assert len(self.findAll(self.items_on_buy_page))==6

    def removeItems(self):
        self.click_all_element(self.remove_button)
        assert self.verify_element_displayed(self.items_on_buy_page)

    def comebackOnProductPage(self):
        self.click_element(self.backToShopping_button)



