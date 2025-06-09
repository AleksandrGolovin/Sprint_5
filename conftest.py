import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Инициализация драйвера Chrome
@pytest.fixture(params=["window-size=350,800", "window-size=700,800", "window-size=1400,800"])
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(request.param)
    driver_instance = webdriver.Chrome(options=chrome_options)
    yield driver_instance
    driver_instance.quit()

# Получить уникальные логин-пароль
@pytest.fixture
def unique_credentials():
    username = ''.join(random.choices(string.ascii_lowercase, k=15))
    domain = random.choice(["example.com", "yandex.ru", "test.com", "mail.ru", "domain.org"])
    email = f"{username}@{domain}"
    password = '1111'
    credentials = {
        "email": email,
        "password": password
    }
    yield credentials

# Попробуй продать мне... ветку.
@pytest.fixture
def random_entity():
    entity = {
            "name": f"Ветка {random.randrange(20, 50)} см.",
            "description": "Прекрасный образец дерева благородной породы",
            "price": random.randrange(100, 10000)
        }
    yield entity