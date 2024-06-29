from constants import Constants
from locators import Locators
from conftest import driver


class TestStellarBurgers:
    def test_select_sauce_tab(self,driver):
        driver.get(Constants.URL)

        driver.find_element(*Locators.SAUCE_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_TAB).text == Constants.SAUCE

    def test_select_fillings_tab(self,driver):
        driver.get(Constants.URL)

        driver.find_element(*Locators.FILLINGS_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_TAB).text == Constants.FILLINGS


    def test_select_buns_tab(self,driver):
        driver.get(Constants.URL)

        driver.find_element(*Locators.SAUCE_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        assert driver.find_element(*Locators.ACTIVE_TAB).text == Constants.BUNS

