import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

username_field.send_keys('vinayak')
password_field.send_keys('vinayak@1234')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login))
login.click()

driver.maximize_window()
time.sleep(20)
driver.quit()
