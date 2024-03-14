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


#add products in cart and go to cart
driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
time.sleep(2)
driver.find_element(By.ID,'checkout').click()
time.sleep(2)

#checkout
driver.find_element(By.ID,'first-name').send_keys('João')
time.sleep(2.5)
driver.find_element(By.ID,'last-name').send_keys('pedro')
time.sleep(2.5)
driver.find_element(By.ID,'postal-code').send_keys('65065-470')
time.sleep(2.5)
driver.find_element(By.ID,'continue').click()
time.sleep(2.5)

#finish process
driver.find_element(By.ID,'finish').click()
time.sleep(2.0)

#checks cart
driver.find_element(By.ID,'back-to-products').click()
time.sleep(2.0)
driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()