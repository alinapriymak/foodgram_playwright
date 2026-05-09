from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators
from helpers.urls import RECIPES_PAGE
import allure


class RecipePage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.locators = RecipePageLocators()
    
    @allure.step("Перейти на вкладку «Создать рецепт»")
    def click_create_recipe_tab(self):
        self.click(self.locators.CREATE_RECIPE_TAB)
        return self
    
    @allure.step("Заполнить название рецепта")
    def input_title(self, title: str):
        self.fill(self.locators.TITLE_INPUT, title)
        return self
    
    @allure.step("Заполнить описание рецепта")
    def input_description(self, description: str):
        self.fill(self.locators.DESCRIPTION_TEXTAREA, description)
        return self
    
    @allure.step("Заполнить время приготовления")
    def input_cooking_time(self, cooking_time: int):
        self.fill(self.locators.COOKING_TIME_INPUT, str(cooking_time))
        return self
    
    @allure.step("Добавить ингредиент")
    def add_ingredient(self, name: str, quantity: str):
        partial_name = name[:3] if len(name) >= 3 else name
        self.fill(self.locators.INGREDIENT_INPUT, partial_name)
        
        self.page.wait_for_selector(self.locators.INGREDIENT_SUGGESTIONS_CONTAINER, state="visible")
        self.page.click(self.locators.INGREDIENT_SUGGESTION_FIRST)
        
        self.fill(self.locators.INGREDIENT_QUANTITY, quantity)
        self.click(self.locators.ADD_INGREDIENT_BUTTON)
        return self
    
    @allure.step("Загрузить изображение")
    def upload_image(self, file_path):
        self.page.set_input_files(self.locators.FILE_INPUT, str(file_path))
        return self
    
    @allure.step("Нажать кнопку «Создать рецепт»")
    def click_submit_button(self):
        with self.page.expect_navigation():
            self.page.locator(self.locators.SUBMIT_BUTTON).click()
        return self
    
    @allure.step("Перейти на страницу рецептов")
    def go_to_recipes_page(self):
        self.page.goto(RECIPES_PAGE)
        return self
    
    @allure.step("Проверить, что карточка рецепта с названием '{expected_title}' отображается")
    def is_recipe_card_visible_with_title(self, expected_title: str):
        self.page.wait_for_selector(f"text='{expected_title}'", state="visible", timeout=10000)
        return expected_title in self.page.content()