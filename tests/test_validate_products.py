import pytest
from selenium import webdriver
from conftest import driver
from pages.product_login_page import LoginPage
from pages.product_page import ProductsPage
from utils.util import *

yaml_data= read_yaml_file("url.yml")
URL= yaml_data.get('product_url')

json_data= read_json_file()
credentials = json_data.get('sauce_demo_credential')

def test_product_validation(driver):
    driver.get(URL)
    data=read_json_file()
    product_data= data['products_data']
    expected_products = {item["Product Name"]: item["Price"] for item in product_data["products"]}

    # Perform login
    login_page = LoginPage(driver)
    login_page.login(credentials["valid_user_name"], credentials["valid_user_password"])

    # Extract product details
    products_page = ProductsPage(driver)
    actual_products = products_page.get_products()

    # Validate extracted product details
    for name, price in actual_products.items():
        assert name in expected_products, f"Unexpected product found: {name}"
        assert price == expected_products[
            name], f"Price mismatch for {name}. Expected: {expected_products[name]}, Got: {price}"


    # Save extracted data to CSV
    create_csv(actual_products)
    print("✅ Product details validated and saved successfully!")



