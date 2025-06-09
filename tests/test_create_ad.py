from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import DeskLocators as DL
from data import REGISTERED_USER


class TestCreateAd:
    # Разместить объявление без авторизации
    def test_create_ad_unauthorized(self, driver: WebDriver):
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Разместить объявление" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.HEADER_BUTTON_CREATE_AD))
        driver.find_element(*DL.HEADER_BUTTON_CREATE_AD).click()
        
        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.POP_LABEL))
        pop_label_text = driver.find_element(*DL.POP_LABEL).text

        # Предупреждение, что неавторизован
        assert pop_label_text == 'Чтобы разместить объявление, авторизуйтесь'
    
    # Авторизоваться и разместить объявление
    def test_create_ad_existing_credetials(self, driver: WebDriver):
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
        
        # Выгрузка поп-апа, загрузка кнопки "Разместить объявление" на главной странице
        WebDriverWait(driver, 5).until(ec.invisibility_of_element_located(DL.POP_UP))
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.HEADER_BUTTON_CREATE_AD))
        driver.find_element(*DL.HEADER_BUTTON_CREATE_AD).click()

        entity = {
            "name": "Ветка",
            "description": "Прекрасный образец дерева благородной породы",
            "price": 100500
        }

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_INPUT_NAME))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_INPUT_PRICE))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_TEXTAREA_DESCRIPTION))
        driver.find_element(*DL.CREATE_INPUT_NAME).send_keys(entity['name'])
        driver.find_element(*DL.CREATE_INPUT_PRICE).send_keys(str(entity['price']))
        driver.find_element(*DL.CREATE_TEXTAREA_DESCRIPTION).send_keys(entity['description'])

        assert True