import random
import string
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome()
    yield driver_instance
    driver_instance.quit()

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