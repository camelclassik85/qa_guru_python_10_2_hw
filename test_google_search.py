from selene import browser, be, have
from selenium.webdriver.common.by import By


def test_should_be_text_after_search(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_should_be_empty_search_result_1(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('35145dsfgsdbgdbd34324234dhdshsdvsvs').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("\nНет результатов поиска")


def test_should_be_empty_search_result_2(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('35145dsfgsdbgdbd34324234dhdshsdvsvs').press_enter()
    result_qty = browser.driver.find_element(By.CSS_SELECTOR, '[id="result-stats"]').text
    assert "Результатов: примерно 0" in result_qty, f'\nЕсть результаты поиска - {result_qty}'
    print("\nНет результатов поиска")
