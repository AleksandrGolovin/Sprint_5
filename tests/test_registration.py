import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import RegistrationLocators as RL
from data import INVALID_EMAILS


class TestRegistration:

    def test_registration_valid_unique_credentials(self, driver: WebDriver, unique_credentials: dict[str, str]):
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_REGISTRATION))
        driver.find_element(*RL.POP_BUTTON_REGISTRATION).click()
        
        # Загурзка кнопки "Нет аккаунта" в форме авторизации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_NO_ACCOUNT))
        driver.find_element(*RL.POP_BUTTON_NO_ACCOUNT).click()

        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(RL.POP_INPUTS))
        driver.find_element(*RL.POP_INPUT_EMAIL).send_keys(unique_credentials['email'])
        driver.find_element(*RL.POP_INPUT_PASSWORD).send_keys(unique_credentials['password'])
        driver.find_element(*RL.POP_INPUT_SUBMIT_PASSWORD).send_keys(unique_credentials['password'])
        # Загрузка кнопки "Создать аккаунт" в форме регистрации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_CREATE_ACCOUNT))
        driver.find_element(*RL.POP_BUTTON_CREATE_ACCOUNT).click()
        
        # Загрузка аватара и имени на главной странице
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.HEADER_USER_NAME))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.HEADER_USER_AVATAR))
        user_name = driver.find_element(*RL.HEADER_USER_NAME).text
        user_avatar = driver.find_elements(*RL.HEADER_USER_AVATAR)
        pop_up = driver.find_elements(*RL.POP_UP)  # Поп-апы есть?

        # Нет поп-апов, имя пользователя 'User.', есть кружок с аватаром
        assert len(pop_up) == 0 and user_name == 'User.' and len(user_avatar) != 0

    @pytest.mark.parametrize('email', INVALID_EMAILS)
    def test_registration_invalid_email(self, email, driver: WebDriver):
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_REGISTRATION))
        driver.find_element(*RL.POP_BUTTON_REGISTRATION).click()
        
        # Загурзка кнопки "Нет аккаунта" в форме авторизации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_NO_ACCOUNT))
        driver.find_element(*RL.POP_BUTTON_NO_ACCOUNT).click()

        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(RL.POP_INPUTS))
        driver.find_element(*RL.POP_INPUT_EMAIL).send_keys(email)
        # Загрузка кнопки "Создать аккаунт" в форме регистрации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(RL.POP_BUTTON_CREATE_ACCOUNT))
        driver.find_element(*RL.POP_BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(RL.POP_INPUT_ERROR))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RL.POP_INPUT_ERROR_MESSAGE))
        inputs_with_errors = driver.find_elements(*RL.POP_INPUT_ERROR)
        input_error_message = driver.find_element(*RL.POP_INPUT_ERROR_MESSAGE).text 

        # Нет поп-апов, имя пользователя 'User.', есть кружок с аватаром
        assert len(inputs_with_errors) == 3 and input_error_message == 'Ошибка'