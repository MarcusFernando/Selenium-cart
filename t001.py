from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)  # changes the behavior of chrome driver so that chrome does not close automatically

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service,options=op) #This instance of webdrive ensures that Selenium has all the necessary functions to control the browser

driver.get("https://www.saucedemo.com/")
time.sleep(2)
#login, maybe the class key could interessting in somes cases, for exemple: send_keys(keys.CONTROL + 'c', 'abc' + key.ENTER)
input_elements = driver.find_element(By.ID,'user-name').send_keys('standard_user')
time.sleep(2.5)
input_elements = driver.find_element(By.ID,'password').send_keys('secret_sauce')
time.sleep(2.5)
input_elements = driver.find_element(By.ID,'login-button').click()

#AssertionError appers when an assert fails
try:
     button_add = driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
     time.sleep(2)
     button_add = driver.find_element(By.ID,'add-to-cart-sauce-labs-bike-light').click()
     time.sleep(2)
     driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
     time.sleep(2.5)
     print("button add-cart is present in page")
except AssertionError:
     print("Error, element not finding")

#test of route
current_url = driver.current_url
expected_url = 'https://www.saucedemo.com/inventory.html'
assert current_url == expected_url, "route confirmed" #if the passed condition of the assert is false, python will raise the assertionerror automatically
