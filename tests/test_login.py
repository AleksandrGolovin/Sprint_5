from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import LoginLocators as LIL
from data import REGISTERED_USER


class TestLogin:
    def test_login_existing_credentials(self, driver: WebDriver):
        email = REGISTERED_USER['email']
        password = REGISTERED_USER['password']
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(LIL.PAGE_BUTTON_REGISTRATION))
        driver.find_element(*LIL.PAGE_BUTTON_REGISTRATION).click()
        
        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(LIL.POP_INPUTS))
        driver.find_element(*LIL.POP_INPUT_EMAIL).send_keys(email)
        driver.find_element(*LIL.POP_INPUT_PASSWORD).send_keys(password)

        # Загурзка кнопки "Вход" в форме авторизации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(LIL.POP_BUTTON_ENTER))
        driver.find_element(*LIL.POP_BUTTON_ENTER).click()
        
        # Загрузка аватара и имени на главной странице
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LIL.HEADER_USER_NAME))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LIL.HEADER_USER_AVATAR))
        user_name = driver.find_element(*LIL.HEADER_USER_NAME).text
        user_avatar = driver.find_elements(*LIL.HEADER_USER_AVATAR)
        pop_up = driver.find_elements(*LIL.POP_UP)  # Поп-апы есть?

        # Нет поп-апов, имя пользователя 'User.', есть кружок с аватаром
        assert len(pop_up) == 0 and user_name == 'User.' and len(user_avatar) != 0