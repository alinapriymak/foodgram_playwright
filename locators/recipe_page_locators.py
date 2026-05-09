class RecipePageLocators:
    """Локаторы страницы рецептов"""
    
    # Навигация
    CREATE_RECIPE_TAB = "//a[contains(text(), 'Создать рецепт')]"
    
    # Поля формы
    TITLE_INPUT = "//div[contains(text(), 'Название рецепта')]/following-sibling::input"
    DESCRIPTION_TEXTAREA = "//div[contains(text(), 'Описание')]/following-sibling::textarea"
    COOKING_TIME_INPUT = "//div[contains(text(), 'Время приготовления')]/following-sibling::input"
    
    # Ингредиенты
    INGREDIENT_INPUT = "input.styles_ingredientsInput__1zzql"
    INGREDIENT_QUANTITY = "input.styles_ingredientsAmountValue__2matT"
    ADD_INGREDIENT_BUTTON = "//div[contains(@class, 'styles_ingredientAdd__3fc32')]"
    
    # Список предложений ингредиентов
    INGREDIENT_SUGGESTIONS_CONTAINER = "div.styles_container__3ukwm"
    INGREDIENT_SUGGESTION_FIRST = "div.styles_container__3ukwm > div:first-child"
    
    # Загрузка изображения
    FILE_INPUT = "input[type='file']"
    
    # Кнопки
    SUBMIT_BUTTON = "//button[contains(text(), 'Создать рецепт')]"
    
    # Карточка рецепта
    RECIPE_CARD = "div.recipe-card"
    RECIPE_TITLE = "h2.recipe-title"