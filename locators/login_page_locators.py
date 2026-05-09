class LoginPageLocators:
    """Локаторы страницы авторизации"""
    
    # Поля ввода
    EMAIL_INPUT = "input[name='email']"
    PASSWORD_INPUT = "input[name='password']"
    
    # Кнопки
    LOGIN_BUTTON = "button:has-text('Войти')"
    LOGOUT_BUTTON = "a:has-text('Выход')"
    
    # Форма
    LOGIN_FORM = "form"