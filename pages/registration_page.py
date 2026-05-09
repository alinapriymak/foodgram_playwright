from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from helpers.urls import SIGNUP_PAGE
import allure


class RegistrationPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.locators = RegistrationPageLocators()
    
    @allure.step("Открыть страницу регистрации")
    def open(self):
        self.page.goto(SIGNUP_PAGE)
        return self
    
    @allure.step("Заполнить форму регистрации")
    def register(self, username: str, email: str, password: str, first_name: str = None, last_name: str = None):
        if first_name:
            self.fill(self.locators.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.fill(self.locators.LAST_NAME_INPUT, last_name)
        self.fill(self.locators.USERNAME_INPUT, username)
        self.fill(self.locators.EMAIL_INPUT, email)
        self.fill(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.REGISTER_BUTTON)
        return self
    
    @allure.step("Проверить переход на страницу авторизации")
    def is_redirected_to_login_page(self):
        self.wait_for_url("signin")
        return "/signin" in self.page.url