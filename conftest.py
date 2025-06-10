import random
import string
import pytest
from selenium import webdriver


@pytest.fixture
def Browser():
    Browser = webdriver.Chrome()
    yield Browser
    Browser.quit()

@pytest.fixture
def Email():
    random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_url = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f'{random_name}@{random_url}.com'

@pytest.fixture
def Password():
    return (random.choices(string.digits, k=8))