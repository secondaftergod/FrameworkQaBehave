from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class OverviewPage(BasePage):
    overview_title = (By.XPATH,"//*[@id='header_container']/div[2]/span")
    cancel_button = (By.XPATH,"//*[@id='cancel']")
    finish_button = (By.XPATH,"//*[@id='finish']")
    total_price_item = (By.XPATH,"//*[@class='summary_subtotal_label']")
    tax_price_item = (By.XPATH,"//*[@class='summary_tax_label']")
    total_price = (By.XPATH,"//*[@class='summary_total_label']")
    def __init__(self, driver):
        super().__init__(driver)
    def check_page(self):
        assert self.get_element_text(self.overview_title)=="CHECKOUT: OVERVIEW"