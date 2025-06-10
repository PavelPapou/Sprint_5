from selenium.webdriver.common.by import By

class WorkLocators:
    REGISTRATION_BUTTON = By.XPATH, "//*[text()='Вход и регистрация']"
    NO_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Нет аккаунта']"
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Создать аккаунт']"
    ENTER_BUTTON = By.XPATH, "//button[contains(@class, 'buttonPrimary') and contains(text(), 'Войти')]"
    QUIT_BUTTON = By.CSS_SELECTOR, ".spanGlobal.btnSmall"
    CREATE_AD_BUTTON = By.XPATH, "//*[text()='Разместить объявление']"

    PROFILE_NAME_CSS = By.CSS_SELECTOR, ".profileText.name"
    PROFILE_IMAGE_CSS = By.CSS_SELECTOR, ".circleSmall"
    EMAIL_INPUT_XPATH = By.XPATH, "//input[@placeholder='Введите Email']"
    EMAIL_INPUT_ERROR_XPATH = By.XPATH, "//*[text()='Ошибка']"
    PASSWORD_INPUT_XPATH = By.XPATH, "//input[@placeholder='Пароль']"
    REPEAT_PASSWORD_XPATH = By.XPATH, "//input[@placeholder='Повторите пароль']"
    ADVERTISEMENT_AUTHORISATION_WINDOWS = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']"