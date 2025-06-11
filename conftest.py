import random
import string
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def email():
    random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_url = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f'{random_name}@{random_url}.com'

@pytest.fixture
def password():
    return (random.choices(string.digits, k=8))