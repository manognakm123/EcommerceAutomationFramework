# Simple code :
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def test_login():
#
#     driver = webdriver.Chrome()
#
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com")
#
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#
#     driver.find_element(By.ID, "login-button").click()
#
#     time.sleep(3)
#
#     assert "inventory" in driver.current_url
#
#     driver.quit()


# Updated code :

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
#
#
# def test_login():
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com")
#
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#
#     time.sleep(5)
#
#     assert "inventory" in driver.current_url
#
#     driver.quit()




# from selenium.webdriver.common.by import By
#
# def test_login(setup):
#
#     driver = setup
#
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#
#     assert "inventory" in driver.current_url




from pages.login_page import LoginPage
from utilities.logger import logger

def test_login(setup):

    driver = setup
    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url

    logger.info(f"Login test started")