from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by, value, timeout=10):
        """Overrides WebDriver's find_element to wait until the element is visible."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except (TimeoutException, NoSuchElementException):
            print(f"Element not found: {value}")
            return None

    def find_elements(self, by, value, timeout=10):
        """Waits for multiple elements to be visible before returning them."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((by, value))
            )
        except TimeoutException:
            print(f"Elements not found: {value}")
            return []

    def click_element(self, by, value):
        """Waits for an element to be clickable before clicking."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def enter_text(self, by, value, text):
        """Waits for an input field to be visible before entering text."""
        element = self.find_element(by, value)
        if element:
            element.clear()
            element.send_keys(text)

    def get_element_text(self, by, value):
        """Retrieves text from a visible element."""
        element = self.find_element(by, value)
        return element.text if element else ""

    def scroll_to_element(self, by, value):
        """Scrolls to the specified element on the page."""
        element = self.find_element(by, value)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_frame(self, by, value):
        """Switches to an iframe when located."""
        frame = self.find_element(by, value)
        if frame:
            self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """Switches back to the default content from an iframe."""
        self.driver.switch_to.default_content()


