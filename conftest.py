import pytest
from selene import browser


@pytest.fixture
def browser_settings():
    browser.config.window_width = 1080
    browser.config.window_height = 720
    yield
    browser.quit()
