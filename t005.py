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
time.sleep(2)
input_elements = driver.find_element(By.ID,'password').send_keys('secret_sauce')
time.sleep(2)
input_elements = driver.find_element(By.ID,'login-button').click()
time.sleep(2)

#button continue shopping 
driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
time.sleep(2.5)
driver.find_element(By.ID,'continue-shopping').click()
reference_element = driver.find_element(By.CLASS_NAME,'footer')
reference_element2 = driver.find_element(By.CLASS_NAME,'app_logo')
time.sleep(2.5)
reference_element.location_once_scrolled_into_view #scroll comand
time.sleep(2.5)
driver.find_element(By.ID,'add-to-cart-test.allthethings()-t-shirt-(red)').click()
time.sleep(2.5)
reference_element2.location_once_scrolled_into_view
time.sleep(2.5)
driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
time.sleep(2.5)
driver.find_element(By.ID,'continue-shopping').click()