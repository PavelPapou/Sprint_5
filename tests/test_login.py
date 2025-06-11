import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import WorkLocators
from data import URL
from helpers import generate_email, generate_password

class TestLogin:

    def test_login_profile_true(self, browser):
        browser
        browser.get(URL)
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        email = generate_email()
        browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(email)
        password = generate_password()
        browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH).send_keys(password)
        browser.find_element(*WorkLocators.REPEAT_PASSWORD_XPATH).send_keys(password)
        browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.QUIT_BUTTON))
        browser.find_element(*WorkLocators.QUIT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(email)
        browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH).send_keys(password)
        browser.find_element(*WorkLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.PROFILE_NAME_CSS))
        browser.find_element(*WorkLocators.PROFILE_IMAGE_CSS)
        profile_name = browser.find_element(*WorkLocators.PROFILE_NAME_CSS).text

        assert profile_name == 'User.'



    def test_logout_profile_true(self, browser):
        browser
        browser.get(URL)
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        email = generate_email()
        browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(email)
        password = generate_password()
        browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH).send_keys(password)
        browser.find_element(*WorkLocators.REPEAT_PASSWORD_XPATH).send_keys(password)
        browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.QUIT_BUTTON))
        browser.find_element(*WorkLocators.QUIT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        registration_text = browser.find_element(*WorkLocators.REGISTRATION_BUTTON).text

        assert registration_text == 'Вход и регистрация' 