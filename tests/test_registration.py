import allure
from pages.registration_page import RegistrationPage 
from pages.login_page import LoginPage
import pytest


@allure.feature("Создание аккаунта")
class TestRegistration:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.registration_page = RegistrationPage(page)
        self.login_page = LoginPage(page)
    
    @allure.title("Создание аккаунта")
    def test_create_account(self, test_user_data):
        with allure.step("Открыть страницу регистрации"):
            self.registration_page.open()
        
        with allure.step("Заполнить форму регистрации"):
            self.registration_page.register(
                username=test_user_data["username"],
                email=test_user_data["email"],
                password=test_user_data["password"],
                first_name=test_user_data["first_name"],
                last_name=test_user_data["last_name"]
            )
        
        with allure.step("Проверить переход на страницу авторизации"):
            assert self.registration_page.is_redirected_to_login_page()