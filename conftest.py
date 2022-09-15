import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()