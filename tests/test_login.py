from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import DeskLocators as DL
from data import REGISTERED_USER


class TestLogin:
    # Авторизоваться как зарегистрированный пользователь
    def test_login_existing_credentials(self, driver: WebDriver):
        email = REGISTERED_USER['email']
        password = REGISTERED_USER['password']
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.HEADER_BUTTON_REGISTRATION))
        driver.find_element(*DL.HEADER_BUTTON_REGISTRATION).click()
        
        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(DL.POP_INPUTS))
        driver.find_element(*DL.POP_INPUT_EMAIL).send_keys(email)
        driver.find_element(*DL.POP_INPUT_PASSWORD).send_keys(password)

        # Загурзка кнопки "Вход" в форме авторизации
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.POP_BUTTON_ENTER))
        driver.find_element(*DL.POP_BUTTON_ENTER).click()
        
        # Загрузка аватара и имени на главной странице
        WebDriverWait(driver, 5).until(ec.invisibility_of_element_located(DL.POP_UP))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.HEADER_USER_AVATAR))
        user_avatar = driver.find_elements(*DL.HEADER_USER_AVATAR)
        pop_up = driver.find_elements(*DL.POP_UP)  # Поп-апы есть?

        # Нет поп-апов, есть кружок с аватаром
        assert len(pop_up) == 0 and len(user_avatar) != 0