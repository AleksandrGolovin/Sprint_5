from selenium.webdriver.common.by import By


class RegistrationLocators:
    POP_UP = By.CLASS_NAME, "popUp_shell__LuyqR"
    
    POP_INPUTS = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input"
    POP_INPUT_ERROR = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//div[@class='input_inputError__fLUP9']"
    POP_INPUT_ERROR_MESSAGE = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//span[@class='input_span__yWPqB']"

    POP_INPUT_EMAIL = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='email']"
    POP_INPUT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='password']"
    POP_INPUT_SUBMIT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='submitPassword']"
    
    PAGE_BUTTON_REGISTRATION = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Вход и регистрация']"
    POP_BUTTON_NO_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Нет аккаунта']"
    POP_BUTTON_CREATE_ACCOUNT = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Создать аккаунт']"
    
    HEADER_USER_NAME = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//h3[@class='profileText name']"
    HEADER_USER_AVATAR = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//button[@class='circleSmall']"

class LoginLocators:
    PAGE_BUTTON_REGISTRATION = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Вход и регистрация']"
    
    POP_UP = By.CLASS_NAME, "popUp_shell__LuyqR"
    POP_INPUTS = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input"
    POP_INPUT_EMAIL = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='email']"
    POP_INPUT_PASSWORD = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//input[@name='password']"
    POP_BUTTON_ENTER = By.XPATH, ".//form[@class='popUp_shell__LuyqR']//button[text()='Войти']"

    HEADER_USER_NAME = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//h3[@class='profileText name']"
    HEADER_USER_AVATAR = By.XPATH, ".//div[@class='header_flexRow__Xdqv1']//button[@class='circleSmall']"
