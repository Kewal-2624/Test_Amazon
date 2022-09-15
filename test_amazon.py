import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestAmazon:
    def test(self):
            self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Chair" + Keys.ENTER)
            # self.driver.find_element(By.ID,"nav-search-submit-button").click()

            self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[2]/h2/a/span").click()
            # self.driver.find_element(By.CSS_SELECTOR, "h2").click()

            #heading = self.driver.find_element(By.XPATH, "(//span[@id='productTitle'])[1]").text
            heading = self.driver.find_element(By.ID, "title").text

            print(heading)
