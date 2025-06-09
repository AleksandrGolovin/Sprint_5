from selenium.webdriver.common.by import By


class DeskLocators:
    POP_UP = By.XPATH, ".//form[contains(@class,'popUp_shell')]"
    POP_INPUTS = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//input"
    POP_INPUT_ERROR = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//div[@class='input_inputError__fLUP9']"
    POP_INPUT_ERROR_MESSAGE = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//span[@class='input_span__yWPqB']"
    POP_INPUT_EMAIL = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//input[@name='email']"
    POP_INPUT_PASSWORD = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//input[@name='password']"
    POP_INPUT_SUBMIT_PASSWORD = By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//input[@name='submitPassword']"
    POP_BUTTON_NO_ACCOUNT = By.XPATH, ".//div[contains(@class,'popUp_button')]//button[text()='Нет аккаунта']"
    POP_BUTTON_CREATE_ACCOUNT = By.XPATH, ".//div[contains(@class,'popUp_button')]//button[text()='Создать аккаунт']"
    POP_BUTTON_ENTER = By.XPATH, ".//div[contains(@class,'popUp_button')]//button[text()='Войти']"
    POP_LABEL = By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']//h1[@class='h1']"
    
    HEADER_BUTTON_REGISTRATION = By.XPATH, ".//div[contains(@class,'header_')]/button[text()='Вход и регистрация']"
    HEADER_BUTTON_CREATE_AD = By.XPATH, ".//div[contains(@class,'header_')]/button[text()='Разместить объявление']"
    HEADER_BUTTON_LOGOUT = By.XPATH, ".//div[contains(@class,'header_')]//button[text()='Выйти']"
    HEADER_USER_AVATAR = By.XPATH, ".//div[contains(@class,'header_')]//button[@class='circleSmall']"
    # Как тесты проводить с именем в header, если оно отображается только в широкоэкранной версии?
    HEADER_USER_NAME = By.XPATH, ".//div[contains(@class,'header_')]//h3[@class='profileText name']"

    CREATE_INPUT_NAME = By.XPATH, ".//div[@class='createListingPage_createListingPageStyle__U-MJJ']//input[@name='name']"
    CREATE_INPUT_PRICE = By.XPATH, ".//div[@class='createListingPage_createListingPageStyle__U-MJJ']//input[@name='price']"
    CREATE_TEXTAREA_DESCRIPTION = By.XPATH, ".//div[@class='createListingPage_createListingPageStyle__U-MJJ']//textarea[@name='description']"
    