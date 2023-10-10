"""
Basic test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_first():
    """
    WERT-1: Открытие деталей товара. Проверка артикула
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-Infobars")
    chrome_options.add_argument("--disable-extentions")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url="https://testqastudio.me")
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = driver.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

    