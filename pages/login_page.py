from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from helpers.urls import SIGNIN_PAGE
import allure


class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.locators = LoginPageLocators()
    
    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.page.goto(SIGNIN_PAGE)
        return self
    
    @allure.step("Выполнить авторизацию")
    def login(self, username: str, password: str):
        self.fill(self.locators.EMAIL_INPUT, username)
        self.fill(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)
        return self
    
    @allure.step("Проверить видимость формы авторизации")
    def is_login_form_visible(self):
        return self.is_visible(self.locators.LOGIN_FORM)
    
    @allure.step("Проверить видимость кнопки выхода")
    def is_logout_button_visible(self):
        return self.is_visible(self.locators.LOGOUT_BUTTON)
    
    @allure.step("Ожидать переход на страницу рецептов")
    def wait_for_redirect_after_login(self):
        self.wait_for_url("recipes")
        return "/recipes" in self.page.url
    
    @allure.step("Нажать кнопку выхода")
    def logout(self):
        if self.is_visible(self.locators.LOGOUT_BUTTON):
            self.click(self.locators.LOGOUT_BUTTON)
        return self