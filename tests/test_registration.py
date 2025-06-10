import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import WorkLocators
from data import URL, PASSWORD

class TestRegistration:

    def test_register_new_profile_true(self, Browser, Email):
        Browser
        Browser.get(URL) 
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        Browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        Browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        Browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(Email)
        Browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH).send_keys(PASSWORD)
        Browser.find_element(*WorkLocators.REPEAT_PASSWORD_XPATH).send_keys(PASSWORD)
        Browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.PROFILE_NAME_CSS))
        Browser.find_element(*WorkLocators.PROFILE_IMAGE_CSS)
        profile_name = Browser.find_element(*WorkLocators.PROFILE_NAME_CSS).text

        assert profile_name == 'User.'

    def test_register_wrong_email_false(self, Browser, Email):
        Browser
        Browser.get(URL) 
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        Browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        Browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        Browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(Email[0:15])
        Browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_ERROR_XPATH))
        assert_text = Browser.find_element(*WorkLocators.EMAIL_INPUT_ERROR_XPATH).text

        assert assert_text == 'Ошибка'

    def test_register_old_profile_false(self, Browser, Email):
        Browser
        Browser.get(URL) 
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        Browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        Browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        Browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(Email)
        Browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH).send_keys(PASSWORD)
        Browser.find_element(*WorkLocators.REPEAT_PASSWORD_XPATH).send_keys(PASSWORD)
        Browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.QUIT_BUTTON))
        Browser.find_element(*WorkLocators.QUIT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.REGISTRATION_BUTTON))
        Browser.find_element(*WorkLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NO_ACCOUNT_BUTTON))
        Browser.find_element(*WorkLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        Browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH).send_keys(Email)
        Browser.find_element(*WorkLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_ERROR_XPATH))
        assert_text = Browser.find_element(*WorkLocators.EMAIL_INPUT_ERROR_XPATH).text

        assert assert_text == 'Ошибка'