import pytest
from pages.register_page import RegisterPage
from utils.excel_reader import get_register_data

register_users = get_register_data("test_data/register_data.xlsx")
print(f"Loaded {len(register_users)} users")  # <- ADD THIS LINE

@pytest.mark.parametrize("user", register_users)
def test_register_user(driver, user):
    register_page = RegisterPage(driver)
    register_page.register_user(user)

