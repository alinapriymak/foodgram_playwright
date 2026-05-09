import pytest
import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage 
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestRecipe:
    
    @pytest.fixture(autouse=True)
    def setup(self, page, test_user_data, test_recipe_data, test_image_path):
        self.page = page
        self.login_page = LoginPage(page)
        self.registration_page = RegistrationPage(page)
        self.recipe_page = RecipePage(page)
        self.test_recipe_data = test_recipe_data
        self.test_image_path = test_image_path
        
        # Создание пользователя
        self.registration_page.open()
        self.registration_page.register(
            username=test_user_data["username"],
            email=test_user_data["email"],
            password=test_user_data["password"],
            first_name=test_user_data["first_name"],
            last_name=test_user_data["last_name"]
        )
       
        self.page.wait_for_timeout(2000)
        
        # Авторизация
        self.login_page.open()
        self.login_page.fill("input[name='email']", test_user_data["username"])
        self.login_page.fill("input[name='password']", test_user_data["password"])
        self.login_page.click("button:has-text('Войти')")
        self.page.wait_for_timeout(2000)
        self.login_page.wait_for_redirect_after_login()

    
    @allure.title("Создание рецепта")
    def test_create_recipe(self):
        with allure.step("Перейти на вкладку «Создать рецепт»"):
            self.recipe_page.click_create_recipe_tab()
        
        with allure.step("Заполнить поле Название рецепта"):
            self.recipe_page.input_title(self.test_recipe_data["title"])
        
        with allure.step("Заполнить поле Описание"):
            self.recipe_page.input_description(self.test_recipe_data["description"])
        
        with allure.step("Добавить ингредиенты"):
            for ingredient in self.test_recipe_data["ingredients"]:
                self.recipe_page.add_ingredient(ingredient["name"], ingredient["quantity"])
        
        with allure.step("Заполнить поле Время приготовления"):
            self.recipe_page.input_cooking_time(self.test_recipe_data["cooking_time"])
        
        with allure.step("Загрузить изображение"):
            self.recipe_page.upload_image(self.test_image_path)
        
        with allure.step("Нажать кнопку «Создать рецепт»"):
            self.recipe_page.click_submit_button()

            # Проверяем, есть ли ошибки на странице
            self.page.wait_for_timeout(3000)
            page_text = self.page.content()
            if "error" in page_text.lower() or "ошибка" in page_text.lower():
                print(f"Error on page: {page_text[:500]}")
                self.page.screenshot(path="error.png")
        
            # Ждем редиректа
            self.page.wait_for_url("**/recipes/*", timeout=15000)
            
        
        with allure.step("Перейти на страницу рецептов"):
            self.recipe_page.go_to_recipes_page()
        
        with allure.step("Проверить, что отображается карточка созданного рецепта"):
            assert self.recipe_page.is_recipe_card_visible_with_title(self.test_recipe_data["title"])