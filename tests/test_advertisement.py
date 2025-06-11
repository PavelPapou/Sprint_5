import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import WorkLocators
from data import URL

class TestAdvertisement:

    def test_add_advertisement_without_profile_true(self, browser):
        browser
        browser.get(URL)
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.CREATE_AD_BUTTON))
        browser.find_element(*WorkLocators.CREATE_AD_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.EMAIL_INPUT_XPATH))
        browser.find_element(*WorkLocators.EMAIL_INPUT_XPATH)
        browser.find_element(*WorkLocators.PASSWORD_INPUT_XPATH)
        ad_auth_windows = browser.find_element(*WorkLocators.ADVERTISEMENT_AUTHORISATION_WINDOWS).text

        assert ad_auth_windows == 'Чтобы разместить объявление, авторизуйтесь'
        