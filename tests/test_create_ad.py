import random
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
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
    def test_create_ad_existing_credentials(self, driver: WebDriver, random_entity: dict):
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

        # Загрузить тектовые поля и ввести имя, цену и описание сущности
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_INPUT_NAME))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_INPUT_PRICE))
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.CREATE_TEXTAREA_DESCRIPTION))
        driver.find_element(*DL.CREATE_INPUT_NAME).send_keys(random_entity['name'])
        driver.find_element(*DL.CREATE_INPUT_PRICE).send_keys(str(random_entity['price']))
        driver.find_element(*DL.CREATE_TEXTAREA_DESCRIPTION).send_keys(random_entity['description'])

        # Загрузить дропдаун городов, выбрать случайный
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.CREATE_DROPDOWN_CITY_ARROW))
        driver.find_element(*DL.CREATE_DROPDOWN_CITY_ARROW).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(DL.CREATE_DROPDOWN_CITY_BUTTONS))
        cities = driver.find_elements(*DL.CREATE_DROPDOWN_CITY_BUTTONS)
        city = random.choice(cities)
        city_name = city.text
        city.click()

        # Загрузить дропдаун категорий, выбрать случайную
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.CREATE_DROPDOWN_CATEGORY_ARROW))
        driver.find_element(*DL.CREATE_DROPDOWN_CATEGORY_ARROW).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(DL.CREATE_DROPDOWN_CATEGORY_BUTTONS))
        categories = driver.find_elements(*DL.CREATE_DROPDOWN_CATEGORY_BUTTONS)
        random.choice(categories).click()

        # Загрузить радио-кнопки состояния товара, выбрать случайную
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.CREATE_FIELDSET_CONDITIONS_ACTIVE))
        driver.find_element(*DL.CREATE_FIELDSET_CONDITIONS_ACTIVE).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_all_elements_located(DL.CREATE_FIELDSET_CONDITIONS_REGULAR))
        conditions = driver.find_elements(*DL.CREATE_FIELDSET_CONDITIONS_REGULAR)
        random.choice(conditions).click()

        # Загрузить кнопку "Опубликовать", нажать
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.CREATE_BUTTON_PUBLISH))
        driver.find_element(*DL.CREATE_BUTTON_PUBLISH).click()

        created_entity = random_entity['name'], random_entity['price'], city_name

        # Загрузить домашнюю страницу, аватар, нажать на аватар
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.HOMEPAGE))
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.HEADER_USER_AVATAR))
        driver.find_element(*DL.HEADER_USER_AVATAR).click()

        # Прокручиваем на последнюю страницу
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.PROFILE_CARD_BUTTON_NEXT))
        not_last_page = len(driver.find_elements(*DL.PROFILE_CARD_BUTTON_NEXT_ACTIVE)) > 0
        while not_last_page:
            driver.find_element(*DL.PROFILE_CARD_BUTTON_NEXT_ACTIVE).click()
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.PROFILE_CARD_BUTTON_NEXT))
            not_last_page = len(driver.find_elements(*DL.PROFILE_CARD_BUTTON_NEXT_ACTIVE)) > 0

        # Загружаем описания последней карточки
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.PROFILE_CARD_DESCRIPTION_LAST))
        descriptions = driver.find_element(*DL.PROFILE_CARD_DESCRIPTION_LAST)
        entity_name = descriptions.find_element(*DL.PROFILE_CARD_NAME).text
        entity_city = descriptions.find_element(*DL.PROFILE_CARD_CITY).text
        entity_price = descriptions.find_element(*DL.PROFILE_CARD_PRICE).text.replace(' ', '').replace('₽', '')
        
        # Если имя, цена и город сходятся
        assert created_entity == (entity_name, int(entity_price), entity_city)