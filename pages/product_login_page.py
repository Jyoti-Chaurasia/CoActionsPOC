from selenium.webdriver.common.by import By
from utils.util import *

yaml_data= read_yaml_file()
login_page_data = yaml_data.get('web_scraping').get('LoginPage')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, login_page_data.get('username_input').get('ID'))
        self.password_input = (By.ID, login_page_data.get('password_input').get('ID'))
        self.login_button = (By.ID, login_page_data.get('login_button').get('ID'))

    def login(self, username, password):
        """Perform login action."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
