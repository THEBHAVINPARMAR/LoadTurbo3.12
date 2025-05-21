# tests/test_login.py
import pytest
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--usercount", action="store", default="2", help="Number of users to login in parallel")


@pytest.mark.parametrize("user", range(100))  # Max 100, dynamically filtered
def test_login_parallel(driver, login_data, user, request):
    usercount = int(request.config.getoption("--usercount"))

    if user >= usercount or user >= len(login_data):
        pytest.skip("Skipping: Exceeds user count or data limit")

    creds = login_data[user]
    print(f"[User {user + 1}] Logging in with: {creds['email']}")

    login_page = LoginPage(driver)
    login_page.load("https://careernavigator.iwnlenergy.com/login")  # 🔁 Replace with your URL
    login_page.login(creds["email"], creds["password"])

    assert "dashboard" in driver.current_url or "Welcome" in driver.page_source
