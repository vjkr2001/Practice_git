from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Setup
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login.php/")
driver.maximize_window()
print(driver.title)
# Test Case: Login with valid credentials
def test_login_valid_credentials():
    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "login")

    # Enter valid credentials
    username.send_keys("valid_user")
    password.send_keys("valid_password")
    login_button.click()

# Execute test
test_login_valid_credentials()
time.sleep(5)

driver.close()