import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.excel_reader import get_login_data

@pytest.fixture(scope="function")
def driver():
    chrome_driver_path = r"C:\DRIVERS\chromedriver-win64\chromedriver.exe"

    if not os.path.exists(chrome_driver_path):
        raise FileNotFoundError(f"❌ ChromeDriver not found at: {chrome_driver_path}")

    print(f"✅ ChromeDriver found at: {chrome_driver_path}")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login_data():
    return get_login_data("test_data/login_data.xlsx")

def pytest_addoption(parser):
    parser.addoption(
        "--usercount",
        action="store",
        default="1",
        help="Number of users to run in parallel"
    )

@pytest.fixture(scope="session")
def user_count(request):
    return int(request.config.getoption("--usercount"))
