import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import WorkLocators
from data import URL
from helpers import generate_email, generate_password

class TestAdvertisement:

    def test_add_advertisement_not_authorized(self, browser):
        browser
        browser.get(URL)
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.CREATE_AD_BUTTON))
        browser.find_element(*WorkLocators.CREATE_AD_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.ADVERTISEMENT_AUTHORISATION_WINDOWS))
        ad_auth_windows = browser.find_element(*WorkLocators.ADVERTISEMENT_AUTHORISATION_WINDOWS).text

        assert ad_auth_windows == 'Чтобы разместить объявление, авторизуйтесь'


    def test_add_advertisement_authorized(self, browser):
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
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(WorkLocators.PROFILE_IMAGE_CSS))
        browser.find_element(*WorkLocators.CREATE_AD_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.NAME_AD))
        browser.find_element(*WorkLocators.NAME_AD).send_keys('Пылесос')
        browser.find_element(*WorkLocators.CATEGORIES_DROPDOWN).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.CATEGORIES_DROPDOWN_OPEN))
        browser.find_element(*WorkLocators.BOOK_CATEGORIES).click()
        browser.find_element(*WorkLocators.STATEMENT_BU).click()
        publish_buton = browser.find_element(*WorkLocators.PUBLISH_BUTTON)
        browser.execute_script("arguments[0].scrollIntoView();", publish_buton)
        browser.find_element(*WorkLocators.CITY_DROPDOWN).click()
        WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable(WorkLocators.CITY_DROPDOWN_OPEN))
        browser.find_element(*WorkLocators.CITY).click()
        browser.find_element(*WorkLocators.DISCRIPTION).send_keys("Ручной")
        browser.find_element(*WorkLocators.PRICE).send_keys(99)
        browser.find_element(*WorkLocators.PUBLISH_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(WorkLocators.ENTER_TO_PROFILE))
        browser.find_element(*WorkLocators.ENTER_TO_PROFILE).click()
        browser.get("https://qa-desk.stand.praktikum-services.ru/profile")
        WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((WorkLocators.MESSAGE_PUBLISH)))

        assert browser.find_element(*WorkLocators.MESSAGE_PUBLISH).is_displayed()
        