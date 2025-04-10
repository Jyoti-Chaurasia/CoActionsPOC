from selenium.webdriver.common.by import By
from utils.util import *

yaml_data= read_yaml_file()
product_page_data = yaml_data.get('web_scraping').get('ProductsPage')

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_items = (By.CLASS_NAME, product_page_data['product_items']['CLASS_NAME'])
        self.product_name = (By.CLASS_NAME, product_page_data['product_name']['CLASS_NAME'])
        self.product_price = (By.CLASS_NAME, product_page_data['product_price']['CLASS_NAME'])

    def get_products(self):
        """Extract product names and prices from the webpage."""
        products = self.driver.find_elements(*self.product_items)
        product_data = {}
        for product in products:
            name = product.find_element(*self.product_name).text
            price = product.find_element(*self.product_price).text
            product_data[name] = price
        return product_data
