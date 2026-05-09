class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Поля ввода
    FIRST_NAME_INPUT = "input[name='first_name']"
    LAST_NAME_INPUT = "input[name='last_name']"
    USERNAME_INPUT = "input[name='username']"
    EMAIL_INPUT = "input[name='email']"
    PASSWORD_INPUT = "input[name='password']"
    
    # Кнопки
    REGISTER_BUTTON = "button:has-text('Создать аккаунт')"
    
    # Ссылки
    SIGNIN_LINK = "a:has-text('Войти')"
    
    # Форма
    LOGIN_FORM = "form"