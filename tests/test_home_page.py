from selenium import webdriver
# import pytest


def test_home_page():
    driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://cyborg.tivo.com")
    assert "TiVo | Best OTA DVRs, Cable DVRs and Streaming" in driver.title
    driver.quit()
