from selenium.webdriver.common.by import By


class DeskLocators:
    POP_UP = By.CLASS_NAME, "popUp_shell__LuyqR"
    POP_INPUTS = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input"
    POP_INPUT_ERROR = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//div[@class='input_inputError__fLUP9']"
    POP_INPUT_ERROR_MESSAGE = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//span[@class='input_span__yWPqB']"
    POP_INPUT_EMAIL = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='email']"
    POP_INPUT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='password']"
    POP_INPUT_SUBMIT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='submitPassword']"
    POP_BUTTON_NO_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Нет аккаунта']"
    POP_BUTTON_CREATE_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Создать аккаунт']"
    POP_BUTTON_ENTER = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Войти']"
    POP_LABEL = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//h1[@class='h1']"
    
    HEADER_BUTTON_REGISTRATION = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Вход и регистрация']"
    HEADER_BUTTON_CREATE_AD = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Разместить объявление']"
    HEADER_BUTTON_LOGOUT = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//button[text()='Выйти']"
    HEADER_USER_NAME = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//h3[@class='profileText name']"
    HEADER_USER_AVATAR = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//button[@class='circleSmall']"
