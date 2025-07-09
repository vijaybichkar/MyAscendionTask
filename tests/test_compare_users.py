import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

def login_and_extract_data(page, username, password):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)
    home_page = HomePage(page)
    return home_page.extract_inventory_data()

@pytest.mark.order(6)
def test_compare_standard_vs_problem_user(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)

    context1 = browser.new_context()
    page1 = context1.new_page()
    standard_data = login_and_extract_data(page1, "standard_user", "secret_sauce")

    context2 = browser.new_context()
    page2 = context2.new_page()
    problem_data = login_and_extract_data(page2, "problem_user", "secret_sauce")

    context1.close()
    context2.close()
    browser.close()

    assert len(standard_data) == len(problem_data), "Mismatch in item count between users"

    mismatches = []
    for i in range(len(standard_data)):
        s = standard_data[i]
        p = problem_data[i]

        for key in ["name", "price", "button", "image"]:
            if s[key] != p[key]:
                mismatches.append(f"Item {i+1} [{key}] mismatch: '{s[key]}' vs '{p[key]}'")

    if mismatches:
        mismatch_report = "\n".join(mismatches)
        pytest.fail(f"Inventory data mismatch between standard_user and problem_user:\n{mismatch_report}")
