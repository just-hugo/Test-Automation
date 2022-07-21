import random
from UnitedSelectorClass import United_Flight_Booking
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium import webdriver
import time

"""chrome_options = webdriver.ChromeOptions
driver = webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-incognito')
driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=chrome_options)"""


airports = []

#open() will open a file and return a corresponding file object . Refer here for information on arguments and parameters: https://www.programiz.com/python-programming/methods/built-in/open

airportsfile = open(r'airports2.txt')

for line in airportsfile:
    airports.append(line.strip())
print(airports)



"""driver.get('http://www.united.com')
try:
    DestinationAirportInputField = driver.find_element_by_id('bookFlightDestinationInput')
    time.sleep(3)
    DestinationAirportInputField.click()
    print('Destination Airport Input Field has been clicked successfully.')
    DestinationAirportInputField.send_keys(random.choice(airports))
    print('The following keystrokes were entered into the Destination Airport Input Field: LAX')
except Exception as err:
    print(str(err))"""

