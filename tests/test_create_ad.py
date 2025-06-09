from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import DeskLocators as DL
from data import REGISTERED_USER


class TestCreateAd:
    def test_create_ad_unauthorized(self, driver: WebDriver):
        page_url = 'https://qa-desk.stand.praktikum-services.ru'
        driver.get(page_url)

        # Загрузка кнопки "Вход и регистрация" на главной странице
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(DL.HEADER_BUTTON_CREATE_AD))
        driver.find_element(*DL.HEADER_BUTTON_CREATE_AD).click()
        
        # Загрузка всех текстовых полей в форме регистрации
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(DL.POP_LABEL))
        pop_label_text = driver.find_element(*DL.POP_LABEL).text

        # Предупреждение, что неавторизован
        assert pop_label_text == 'Чтобы разместить объявление, авторизуйтесь'