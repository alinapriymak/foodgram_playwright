import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path
from helpers.data import TestData


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def test_user_data():
    return {
        "username": TestData.generate_unique_username(),
        "email": TestData.generate_unique_email(),
        "password": TestData.generate_valid_password(),
        "first_name": TestData.generate_first_name(),
        "last_name": TestData.generate_last_name()
    }


@pytest.fixture(scope="function")
def test_recipe_data():
    return {
        "title": TestData.generate_recipe_title(),
        "description": TestData.generate_recipe_description(),
        "ingredients": TestData.generate_ingredients(),
        "cooking_time": TestData.generate_cooking_time()
    }


@pytest.fixture(scope="function")
def test_image_path():
    project_root = Path(__file__).parent 
    image_path = project_root / "assets" / "test_img.jpg"
    return image_path