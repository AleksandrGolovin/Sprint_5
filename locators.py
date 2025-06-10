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
    CREATE_DROPDOWN_INPUT_CITY_ = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='city']"
    CREATE_DROPDOWN_CITY_ARROW = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='city']/..//button[contains(@class,'dropDownMenu_arrow')]"
    CREATE_DROPDOWN_CITY_BUTTONS = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='city']/../..//button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP']"
    CREATE_DROPDOWN_INPUT_CATEGORY_ = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='category']"
    CREATE_DROPDOWN_CATEGORY_ARROW = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='category']/..//button[contains(@class,'dropDownMenu_arrow')]"
    CREATE_DROPDOWN_CATEGORY_BUTTONS = By.XPATH, ".//div[@class='dropDownMenu_dropMenu__sBxhz']//input[@name='category']/../..//button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP']"
    CREATE_FIELDSET_CONDITIONS_ACTIVE = By.XPATH, ".//fieldset[contains(@class, 'createListing_inputRadio')]//div[@class='radioUnput_inputActive__eC-HY']"
    CREATE_FIELDSET_CONDITIONS_REGULAR = By.XPATH, ".//fieldset[contains(@class, 'createListing_inputRadio')]//div[@class='radioUnput_inputRegular__FbVbr']"
    CREATE_BUTTON_PUBLISH = By.XPATH, ".//button[@type='submit' and text()='Опубликовать']"

    PROFILE_CARD_DESCRIPTION_LAST = By.XPATH, "(.//div[@class='card']/div[@class='description'])[last()]"
    PROFILE_CARD_NAME = By.XPATH, ".//div[@class='about']/h2"
    PROFILE_CARD_CITY = By.XPATH, ".//div[@class='about']/h3"
    PROFILE_CARD_PRICE = By.XPATH, ".//div[@class='price']/h2"
    PROFILE_CARD_BUTTON_NEXT_ACTIVE = By.XPATH, ".//button[@class='arrowButton arrowButton--right undefined' and not(@disabled)]"
    PROFILE_CARD_BUTTON_NEXT = By.XPATH, ".//button[@class='arrowButton arrowButton--right undefined']"

    HOMEPAGE = By.XPATH, ".//div[contains(@class, 'homePage_homepageStyle')]"