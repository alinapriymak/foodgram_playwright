import pytest
import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@allure.feature("Авторизация")
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, page, test_user_data):
        self.page = page
        self.login_page = LoginPage(page)
        self.registration_page = RegistrationPage(page)
        self.test_user_data = test_user_data
        
        # Создание пользователя для теста
        self.registration_page.open()
        self.registration_page.register(
            username=test_user_data["username"],
            email=test_user_data["email"],
            password=test_user_data["password"],
            first_name=test_user_data["first_name"],
            last_name=test_user_data["last_name"]
        )
        self.registration_page.is_redirected_to_login_page()
        

    
    @allure.title("Авторизация")
    def test_login(self):
        with allure.step("Нажать кнопку «Войти»"):
            self.login_page.open()
        
        with allure.step("Заполнить поле Email"):
            self.login_page.fill("input[name='email']", self.test_user_data["username"])
        
        with allure.step("Заполнить поле Пароль"):
            self.login_page.fill("input[name='password']", self.test_user_data["password"])
        
        with allure.step("Нажать кнопку «Войти»"):
            self.login_page.click("button:has-text('Войти')")
        
        with allure.step("Проверить переход на страницу рецептов"):
            assert self.login_page.wait_for_redirect_after_login()
        
        with allure.step("Проверить, что отображается кнопка «Выход»"):
            assert self.login_page.is_logout_button_visible()