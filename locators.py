from selenium.webdriver.common.by import By


class RegistrationLocators:
    FORM_POP_UP = By.CLASS_NAME, "popUp_shell__LuyqR"
    BUTTON_REGISTRATION = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Вход и регистрация']"
    BUTTON_NO_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Нет аккаунта']"
    INPUT_EMAIL = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='email']"
    INPUT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='password']"
    INPUT_SUBMIT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='submitPassword']"
    BUTTON_CREATE_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Создать аккаунт']"
    HEADER_USER_NAME = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//h3[@class='profileText name']"
    HEADER_USER_AVATAR = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//button[@class='circleSmall']"