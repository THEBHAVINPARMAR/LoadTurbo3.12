from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register_user(self, user):
        self.driver.get("http://uat-web.iwnlenergy.com/register")

        # Fill in all fields
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys(user["first_name"])
        self.driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(user["last_name"])
        self.driver.find_element(By.XPATH, "//input[@id='mobile_no']").send_keys(str(user["mobile"]))
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(user["email"])
        self.driver.find_element(By.XPATH, "//input[@id='access_code']").send_keys(user["access_code"])
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(user["password"])
        self.driver.find_element(By.XPATH, "//input[@id='password_confirmation']").send_keys(user["confirm_password"])

        # Check the checkbox if not already selected
        checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and contains(@class, 'ant-checkbox-input')]")
        if not checkbox.is_selected():
            checkbox.click()

        # Click the Sign Up button
        self.driver.find_element(By.XPATH, "//button[.//span[text()='Sign Up']]").click()
