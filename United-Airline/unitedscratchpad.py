import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from UnitedSelectorClass import United_Flight_Booking

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-incognito')
driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=chrome_options)
wait = WebDriverWait
Test = United_Flight_Booking

driver.get('http://www.united.com')
print('United.com has been loaded in an incognito Chrome Window.')

# fareDropdown is the dropdown menu element. CLicking on it simply opens up the dropdown menu to display the 3 dropdown options: economy, premium economy, and business/first
economy = Keys.ENTER
premium = Keys.ARROW_DOWN, Keys.ENTER
business = Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER
fareTypes = [economy, premium, business]
fareDropdown = wait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'cabinType')))


fareDropdown.click()

time.sleep(5)
action(driver).send_keys(random.choice(fareTypes)).perform()
"""
"""


