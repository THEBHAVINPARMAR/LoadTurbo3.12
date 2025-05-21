# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Updated XPaths or IDs
        self.email_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit' and contains(@class,'log_in_button')]")

    def load(self, url):
        self.driver.get(url)

    def login(self, email, password):
        # Explicit wait before interacting
        self.wait.until(EC.visibility_of_element_located(self.email_input)).clear()
        self.driver.find_element(*self.email_input).send_keys(email)

        self.wait.until(EC.visibility_of_element_located(self.password_input)).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
