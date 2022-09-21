from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

load_dotenv('variables.env')

login = os.getenv('LOGIN')
pw = os.getenv('PW')

chrome = '/Users/gael/Desktop/100_days_code/*Tools/chromedriver'
driver = webdriver.Chrome(chrome)

driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
try:
    accept_cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]')
    accept_cookies.click()
    time.sleep(2)
except:
    pass

username = driver.find_element(By.NAME, 'username')
username.click()
username.send_keys(login)
time.sleep(1)

password = driver.find_element(By.NAME, 'password')
password.click()
password.send_keys(pw)
time.sleep(1)

login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login_btn.click()
time.sleep(6)

search_bar_div = driver.find_element(By.CSS_SELECTOR, '._aawf._aawg._aexm div div span')
search_bar_div.click()
time.sleep(2)
search_bar = driver.find_element(By.TAG_NAME, 'input')
time.sleep(1)
search_bar.send_keys('appbrewery')
search_bar.send_keys(Keys.RETURN)
time.sleep(1)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)
search_bar.send_keys(Keys.RETURN)
time.sleep(6)

followers_link = driver.find_element(By.CSS_SELECTOR, 'main > div > header > section > ul > li:nth-child(2) > a > div')
followers_link.click()
time.sleep(3)

follow_buttons = driver.find_elements(By.CSS_SELECTOR, 'div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm')

for follow_button in follow_buttons:
    time.sleep(5)
    follow_button.click()


