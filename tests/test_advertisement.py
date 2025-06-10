import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import WorkLocators
from data import URL

class TestAdvertisement:

    def test_add_advertisement_without_profile_true(self, Browser):
        Browser
        Browser.get(URL)
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.CREATE_AD_BUTTON))
        Browser.find_element(*WorkLocators.CREATE_AD_BUTTON).click()
        WebDriverWait(Browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        Browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH)
        Browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH)
        ad_auth_windows = Browser.find_element(*WorkLocators.ADVERTISEMENT_AUTHORISATION_WINDOWS).text

        assert ad_auth_windows == 'Чтобы разместить объявление, авторизуйтесь'
        