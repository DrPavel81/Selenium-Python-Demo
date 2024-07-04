from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

chrome_driver_path = 'C:/chromedriver-win64/chromedriver.exe'

chrome_options = Options()

chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://www.python.org")

print(driver.title + " DrPavel")

driver.quit()
