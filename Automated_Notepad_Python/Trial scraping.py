from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys
import os
#from google import search


option = Options()
option.add_experimental_option('debuggerAddress','localhost:9222')
driver = webdriver.Chrome(options=option)
driver.get('https://veeva.io/profile/detail/60c18ff90a869e0eb896c3ae')

try:
    specialties = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.CSS_SELECTOR, 'text-muted')
    )

    print(specialties.text())

except:
    print('Error')




