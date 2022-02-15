from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import re

class OverviewPage(BasePage):
    overview_title = (By.XPATH,"//*[@id='header_container']/div[2]/span")
    cancel_button = (By.XPATH,"//*[@id='cancel']")
    finish_button = (By.XPATH,"//*[@id='finish']")
    inv_price_items=(By.XPATH,"//*[@class='inventory_item_price']")
    total_price_item = (By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[5]")
    tax_price_item = (By.XPATH,"//*[@class='summary_tax_label']")
    total_price = (By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[7]")
    def __init__(self, driver):
        super().__init__(driver)

    def check_page(self):
        assert self.get_element_text(self.overview_title)=="CHECKOUT: OVERVIEW"

    def total_price(self):
        totalprice = 0
        for i in self.get_all_elements_text(self.inv_price_items):
            totalprice+=float(i.strip('$'))
        return totalprice

    def fact_price(self):
        z=re.findall(r'\d.+',self.get_element_text(self.total_price_item))
        return float(z[0])
    def assert_price(self):
        assert self.total_price()==self.fact_price()

    def getTax(self):
        z=re.findall(r'\d.+',self.get_element_text(self.tax_price_item))
        return float(z[0])
    def getTotal(self):
        z = re.findall(r'\d.+', self.get_element_text(self.total_price))
        return float(z[0])
    def eqFullprice(self):
        assert self.getTax()+self.fact_price()==140.34
    def finishButton(self):
        self.click_element(self.finish_button)
