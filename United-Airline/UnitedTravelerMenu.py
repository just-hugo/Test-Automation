from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random

class United_Traveler_Menu:
    chrome_options = webdriver.ChromeOptions

    driver = webdriver
    wait = WebDriverWait

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)

    def main_travelers_input_field(self):
        try:
            MainTravelersInputField = self.driver.find_element_by_id('bookFlightModel.passengers')
            MainTravelersInputField.click()
            print('Main Page Travelers Input Field has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_close_button(self):
        try:
            MainTravelersContextMenuCloseButton = self.driver.find_element_by_id('passengersCloseBtn')
            MainTravelersContextMenuCloseButton.click()
            print('Main Page Travelers Context Menu Close Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_clear_button(self):
        try:
            MainTravelersContextMenuClearButton = self.driver.find_element_by_id('clearPassengers')
            MainTravelersContextMenuClearButton.click()
            print('Main Page Travelers Context Menu Clear Button has been clicked successfully.')
        except Exception as err:
            print(str(err))
#TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging. Note that combined total of all travelers cannot exceed 9.
    #this method is does not work when assembled in an action chain; you must click the input field element first and then give a separate command to send_keys in order to change the input value from 1(default) to 3(or randomized)
    def main_travelers_context_menu_adults_input_field(self):
        try:
            MainTravelersContextMenuAdultsInputField = self.driver.find_element_by_id('NumOfAdults')
            MainTravelersContextMenuAdultsInputField.click()
            MainTravelersContextMenuAdultsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Adults Input Field has successfully received input to assign the number of Adult Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Adults in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Adult Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_adults_plus_button(self):
        try:
            MainTravelersContextMenuAdultsPlusButton = self.driver.find_element_by_id('NumOfAdults plusBtn')
            MainTravelersContextMenuAdultsPlusButton.click()
            print('The number of Adult Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Adults in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Adult Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_adults_minus_button(self):
        try:
            MainTravelersContextMenuAdultsMinusButton = self.driver.find_element_by_id('NumOfAdults minusBtn')
            MainTravelersContextMenuAdultsMinusButton.click()
            print('The number of Adult Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging. Note that combined total of all travelers cannot exceed 9.
    def main_travelers_context_menu_seniors_input_field(self):
        try:
            MainTravelersContextMenuSeniorsInputField = self.driver.find_element_by_id('NumOfSeniors')
            MainTravelersContextMenuSeniorsInputField.click()
            MainTravelersContextMenuSeniorsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Seniors Input Field has successfully received input to assign the number of Senior Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Seniors in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Senior Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_seniors_plus_button(self):
        try:
            MainTravelersContextMenuSeniorsPlusButton = self.driver.find_element_by_id('NumOfSeniors plusBtn')
            MainTravelersContextMenuSeniorsPlusButton.click()
            print('The number of Seniors Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Seniors in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Seniors Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_seniors_minus_button(self):
        try:
            MainTravelersContextMenuSeniorsMinusButton = self.driver.find_element_by_id('NumOfSeniors minusBtn')
            MainTravelersContextMenuSeniorsMinusButton.click()
            print('The number of Seniors Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging. Note that combined total of all travelers cannot exceed 9.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infants_input_field(self):
        try:
            MainTravelersContextMenuInfantsInputField = self.driver.find_element_by_id('NumOfInfants')
            MainTravelersContextMenuInfantsInputField.click()
            MainTravelersContextMenuInfantsInputField.send_keys('3')
            print('Main Page Travelers Context Menu Infants Under 2 Input Field has successfully received input to assign the number of Infant Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Infants Under 2 in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Infant Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infants_plus_button(self):
        try:
            MainTravelersContextMenuInfantsPlusButton = self.driver.find_element_by_id('NumOfInfants plusBtn')
            MainTravelersContextMenuInfantsPlusButton.click()
            print('The number of Infant Under 2 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Infants in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Infant Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_infants_minus_button(self):
        try:
            MainTravelersContextMenuInfantsMinusButton = self.driver.find_element_by_id('NumOfInfants minusBtn')
            MainTravelersContextMenuInfantsMinusButton.click()
            print('The number of Infant Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    # TODO randomize selection of send_keys values for all the following Traveler Context Menu elements; input field will accept 0 - 9. Should also write a negative test case to confirm it will not accept values greater than 9. Be sure the random value is also noted in the print confirmation message and error logging.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infantsonlap_input_field(self):
        try:
            MainTravelersContextMenuInfantsOnLapInputField = self.driver.find_element_by_id('NumOfLapInfants')
            MainTravelersContextMenuInfantsOnLapInputField.click()
            MainTravelersContextMenuInfantsOnLapInputField.send_keys('3')
            print('Main Page Travelers Context Menu Infants On Lap Input Field has successfully received input to assign the number of Infant On Lap Travelers to 3.')
        except Exception as err:
            print(str(err))

#this method will click the Plus Button next to Infants On Lap in the Travelers context menu. Note this method only clicks the Plus Button once; in order to select additional Infant On Lap Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    #infants must have at least 1 adult or senior traveler to be a valid selection.
    def main_travelers_context_menu_infantsonlap_plus_button(self):
        try:
            MainTravelersContextMenuInfantsOnLapPlusButton = self.driver.find_element_by_id('NumOfLapInfants plusBtn')
            MainTravelersContextMenuInfantsOnLapPlusButton.click()
            print('The number of Infant On Lap Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

#this method will click the Minus Button next to Infants On Lap in the Travelers context menu. Note this method only clicks the Minus Button once; in order to deselect additional Infants On Lap Travelers, more clicks will be needed. In other words, call this method for every single click in a test case.
    def main_travelers_context_menu_infantsonlap_minus_button(self):
        try:
            MainTravelersContextMenuInfantsOnLapMinusButton = self.driver.find_element_by_id('NumOfLapInfants minusBtn')
            MainTravelersContextMenuInfantsOnLapMinusButton.click()
            print('The number of Infant On Lap Travelers has been reduced by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children15_input_field(self):
        try:
            MainTravelersContextMenuchildren15InputField = self.driver.find_element_by_id('NumOfChildren04')
            MainTravelersContextMenuchildren15InputField.click()
            MainTravelersContextMenuchildren15InputField.send_keys('3')
            print('Main Page Travelers Context Menu Children 15-17 Input Field has successfully received input to assign the number of Children 15-17 travelers to 3.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children15_plus_button(self):
        try:
            MainTravelersContextMenuchildren15PlusButton = self.driver.find_element_by_id('NumOfChildren04 plusBtn')
            MainTravelersContextMenuchildren15PlusButton.click()
            MainTravelersContextMenuchildren15PlusButton.send_keys('3')
            print('The number of Children 15-17 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children15_minus_button(self):
        try:
            MainTravelersContextMenuchildren15MinusButton = self.driver.find_element_by_id('NumOfChildren04 minusBtn')
            MainTravelersContextMenuchildren15MinusButton.click()
            MainTravelersContextMenuchildren15MinusButton.send_keys('3')
            print('The number of Children 15-17 Travelers has been decreased by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children12_input_field(self):
        try:
            MainTravelersContextMenuchildren12InputField = self.driver.find_element_by_id('NumOfChildren03')
            MainTravelersContextMenuchildren12InputField.click()
            MainTravelersContextMenuchildren12InputField.send_keys('3')
            print('Main Page Travelers Context Menu Children 12-14 Input Field has successfully received input to assign the number of Children 12-14 travelers to 3.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children12_plus_button(self):
        try:
            MainTravelersContextMenuchildren12PlusButton = self.driver.find_element_by_id('NumOfChildren03 plusBtn')
            MainTravelersContextMenuchildren12PlusButton.click()
            MainTravelersContextMenuchildren12PlusButton.send_keys('3')
            print('The number of Children 12-14 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children12_minus_button(self):
        try:
            MainTravelersContextMenuchildren12MinusButton = self.driver.find_element_by_id('NumOfChildren03 minusBtn')
            MainTravelersContextMenuchildren12MinusButton.click()
            MainTravelersContextMenuchildren12MinusButton.send_keys('3')
            print('The number of Children 12-14 Travelers has been decreased by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children5_input_field(self):
        try:
            MainTravelersContextMenuchildren5InputField = self.driver.find_element_by_id('NumOfChildren02')
            MainTravelersContextMenuchildren5InputField.click()
            MainTravelersContextMenuchildren5InputField.send_keys('3')
            print('Main Page Travelers Context Menu Children 5-11 Input Field has successfully received input to assign the number of Children 5-11 travelers to 3.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children5_plus_button(self):
        try:
            MainTravelersContextMenuchildren5PlusButton = self.driver.find_element_by_id('NumOfChildren02 plusBtn')
            MainTravelersContextMenuchildren5PlusButton.click()
            MainTravelersContextMenuchildren5PlusButton.send_keys('3')
            print('The number of Children 5-11 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children5_minus_button(self):
        try:
            MainTravelersContextMenuchildren5MinusButton = self.driver.find_element_by_id('NumOfChildren02 minusBtn')
            MainTravelersContextMenuchildren5MinusButton.click()
            MainTravelersContextMenuchildren5MinusButton.send_keys('3')
            print('The number of Children 5-11 Travelers has been decreased by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children2_input_field(self):
        try:
            MainTravelersContextMenuchildren2InputField = self.driver.find_element_by_id('NumOfChildren01')
            MainTravelersContextMenuchildren2InputField.click()
            MainTravelersContextMenuchildren2InputField.send_keys('3')
            print('Main Page Travelers Context Menu Children 2-4 Input Field has successfully received input to assign the number of Children 2-4 travelers to 3.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children2_plus_button(self):
        try:
            MainTravelersContextMenuchildren2PlusButton = self.driver.find_element_by_id('NumOfChildren01 plusBtn')
            MainTravelersContextMenuchildren2PlusButton.click()
            MainTravelersContextMenuchildren2PlusButton.send_keys('3')
            print('The number of Children 2-4 Travelers has been increased by 1 by clicking the Plus Button on the main page.')
        except Exception as err:
            print(str(err))

    def main_travelers_context_menu_children2_minus_button(self):
        try:
            MainTravelersContextMenuchildren2MinusButton = self.driver.find_element_by_id('NumOfChildren01 minusBtn')
            MainTravelersContextMenuchildren2MinusButton.click()
            MainTravelersContextMenuchildren2MinusButton.send_keys('3')
            print('The number of Children 2-4 Travelers has been decreased by 1 by clicking the Minus Button on the main page.')
        except Exception as err:
            print(str(err))


    def traveler_randomizer(self):
        travelerOptions = [self.driver.find_element_by_id('NumOfChildren01 minusBtn')]
        numberTravelers = random.randint(1,9)


        for i in range(numberTravelers):
            travelerOptions[0].click()


