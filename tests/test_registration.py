from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import RegistrationLocators as RL


class TestRegistration:

    def test_registration_with_unique_credentials(self, driver: WebDriver, unique_credentials: dict[str, str]):
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.BUTTON_REGISTRATION))
        driver.find_element(*RL.BUTTON_REGISTRATION).click()
        
        # Загурзка кнопки "Нет аккаунта" в форме авторизации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.BUTTON_NO_ACCOUNT))
        driver.find_element(*RL.BUTTON_NO_ACCOUNT).click()

        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.INPUT_EMAIL))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.INPUT_PASSWORD))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.INPUT_SUBMIT_PASSWORD))
        driver.find_element(*RL.INPUT_EMAIL).send_keys(unique_credentials['email'])
        driver.find_element(*RL.INPUT_PASSWORD).send_keys(unique_credentials['password'])
        driver.find_element(*RL.INPUT_SUBMIT_PASSWORD).send_keys(unique_credentials['password'])
        # Загрузка кнопки "Создать аккаунт" в форме регистрации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.BUTTON_CREATE_ACCOUNT))
        driver.find_element(*RL.BUTTON_CREATE_ACCOUNT).click()
        
        # Загрузка аватара и имени на главной странице
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.HEADER_USER_NAME))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.HEADER_USER_AVATAR))
        user_name = driver.find_element(*RL.HEADER_USER_NAME).text
        user_avatar = driver.find_elements(*RL.HEADER_USER_AVATAR)
        pop_up = driver.find_elements(*RL.FORM_POP_UP)  # Поп-апы есть?

        # Нет поп-апов, имя пользователя 'User.', есть кружок с аватаром
        assert len(pop_up) == 0 and user_name == 'User.' and len(user_avatar) != 0