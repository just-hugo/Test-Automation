from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class United_Flight_Booking:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)

    def loadtime(self):
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        # Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s" % backendPerformance_calc)
        print("Front End: %s" % frontendPerformance_calc)
        return

    def airport_generator(self):
        airports = []
        codes = []

        # open() will open a file and return a corresponding file object . Refer here for information on arguments and parameters: https://www.programiz.com/python-programming/methods/built-in/open

        airportsfile = open(r'airports.txt')
        codesfile = open(r'codes.txt')
        for line in airportsfile:
            airports.append(line.strip())
        for line in codesfile:
            codes.append(line.strip())
        # print(airports)
        # print(codes)

        randomAirport = random.choice(airports)
        randomCode = random.choice(codes)

    def close_browser(self):
        self.driver.quit()

    def open_United(self):
        self.driver.get('http://www.united.com')
        print('United.com has been loaded in an incognito Chrome Window.')

#The following selectors are for all elements on the United.com main page search widget.

    #This method is to select the radio button labeled "Roundtrip" on the United.com home page.
    def roundtrip_radio_button(self):
        try:
            RoundtripRadioButton = self.driver.find_element_by_id('roundtrip')
            RoundtripRadioButton.click()
            print('Roundtrip Radio Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def oneway_radio_button(self):
        try:
            OnewayRadioButton = self.driver.find_element_by_id('oneway')
            OnewayRadioButton.click()
            print('Oneway Radio Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def book_with_miles_checkbox(self):
        try:
            BookWithMilesCheckbox = self.driver.find_element_by_xpath('//label[@for="award"]')
            BookWithMilesCheckbox.click()
            print('Book With Miles Checkbox has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def calendar_shop_checkbox(self):
        try:
            CalendarShopCheckbox = self.driver.find_element_by_id('flexDatesLabel')
            CalendarShopCheckbox.click()
            print('Calendar Shop Checkbox has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def departing_airport_input_field(self):
        airports = []
        airportsfile = open(r'airports2.txt')
        for line in airportsfile:
            airports.append(line.strip())

        try:
            DepartingAirportInputField = self.driver.find_element_by_id('bookFlightOriginInput')
            time.sleep(2)
            DepartingAirportInputField.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
            print('Departing Airport Input Field has been clicked successfully.')
            time.sleep(2)
            action(self.driver).move_to_element(DepartingAirportInputField).send_keys(random.choice(airports)).perform()
            time.sleep(2)
        except Exception as err:
            print(str(err))

    def destination_airport_input_field(self):
        airports = []
        airportsfile = open(r'airports2.txt')
        for line in airportsfile:
            airports.append(line.strip())

        try:
            DestinationAirportInputField = self.driver.find_element_by_id('bookFlightDestinationInput')
            DestinationAirportInputField.click()
            time.sleep(1)
            print('Destination Airport Input Field has been clicked successfully.')
            action(self.driver).move_to_element(DestinationAirportInputField).send_keys(random.choice(airports)).perform()
            print('The following keystrokes were entered into the Destination Airport Input Field: LAX')
        except Exception as err:
            print(str(err))

#TODO the calendarDate variable below is hardcoded using CSS Selector to select a specific date in the calendar menu. We need to randomize this selection. To do so, we must replace the ".CalendarDay:nth-child(4)" part of the CSS Selector -- the (4) points to the specific date element. Randomizing the number rather than leaving it as 4 will allow us to select any date. The randomizer must be coded such that it will only select future dates, as United will not allow searches of past dates.

    def roundtrip_departing_date(self):
        try:
            RoundtripDepartingDateField = self.driver.find_element_by_id('DepartDate')
            RoundtripDepartingDateField.click()
            print('Roundtrip Departing Date Field has been clicked successfully.')
                                                                                             # 2 - left month, 3 - right month | daytable row   } daytable column
            calendarDepartDate = self.driver.find_element(By.CSS_SELECTOR, ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(1) > .CalendarDay:nth-child(4)")
                                                                                             # even blank spaces are considered part of the table, keep this in mind.
            calendarDepartDate.click()
        except Exception as err:
            print(str(err))

    def roundtrip_return_date(self):
        try:
            RoundtripReturnDateField = self.driver.find_element_by_id('ReturnDate')
            RoundtripReturnDateField.click()
            print('Roundtrip Return Date Field has been clicked successfully.')
            calendarReturnDate = self.driver.find_element(By.CSS_SELECTOR, ".CalendarMonthGrid_month__horizontal:nth-child(3) tr:nth-child(5) > .CalendarDay:nth-child(5)")
            calendarReturnDate.click()
        except Exception as err:
            print(str(err))

    # randomly generate an october roundtrip flight
    #TODO try to see if click intercepts happen at blank spaces. can use this to select days.

    def roundtrip_random_date(self):
        try:
            calendar_list = self.calendar_format(3, 5, 5)

            RoundtripDepartingDateField = self.driver.find_element_by_id('DepartDate')
            RoundtripDepartingDateField.click()
            print('Roundtrip Departing Date Field has been clicked successfully.')

            # index 0 - month on left, index 1 - month on right
            calendar_elements = self.driver.find_elements_by_xpath("*//div//table//tbody//tr")

            print(calendar_elements)
            calendarDepartDate = self.driver.find_element(By.CSS_SELECTOR,
                                                          ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child("
                                                          + str(calendar_list[0])
                                                          + ") > .CalendarDay:nth-child("
                                                          + str(calendar_list[1])
                                                          + ")")
            calendarDepartDate.click()

            RoundtripReturnDateField = self.driver.find_element_by_id('ReturnDate')
            RoundtripReturnDateField.click()
            print('Roundtrip Return Date Field has been clicked successfully.')
            calendarReturnDate = self.driver.find_element(By.CSS_SELECTOR,
                                                          ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child("
                                                          + str(calendar_list[2])
                                                          + ") > .CalendarDay:nth-child("
                                                          + str(calendar_list[3])
                                                          + ")")
            calendarReturnDate.click()

        except Exception as err:
            print(str(err))

        # randomly generate an october roundtrip flight

    def calendar_format(self, start_col, end_col, max_row):
        try:
            # generate departure dates
            DepartCol = random.randint(1, 7)  # generate a random column int, max possible
            DepartRow = random.randint(1, max_row)  # generate a random row int, max possible

            print("DepartCol:\t" + str(DepartCol))
            print("DepartRow:\t" + str(DepartRow))
            # adjust random ints so they aren't correlated to blank spaces
            if DepartRow is 1 and DepartCol < start_col:
                print(str(DepartCol) + "<" + str(start_col))
                DepartCol = start_col  # set DepartCol to the earliest possible date

            if DepartRow is 5 and DepartCol > end_col:
                print(str(DepartCol) + ">" + str(end_col))
                DepartCol = end_col  # set DepartCol to latest possible date

            print("DepartCol:\t" + str(DepartCol))
            # declare here so it can be used outside of if-else scope
            ReturnCol = 0
            # generate return dates
            ReturnRow = random.randint(DepartRow, max_row)  # must be on the same row as depart date or later
            print("Return Row:\t" + str(ReturnRow))
            if DepartRow is ReturnRow:
                ReturnCol = random.randint(DepartCol, 7)  # must be a later date if on the same row
                print("ReturnCol:\t" + str(ReturnCol))
            elif DepartRow is not ReturnRow:
                ReturnCol = random.randint(1, 7)
                print("ReturnCol:\t" + str(ReturnCol))

            # adjust random ints so they aren't correlated to blank spaces
            if ReturnRow is 1 and ReturnCol < start_col:
                print(str(ReturnCol) + "<" + str(start_col))

                ReturnCol = start_col  # set DepartCol to the earliest possible date

            if ReturnRow is 5 and ReturnCol > end_col:
                print(str(ReturnCol) + ">" + str(start_col))
                ReturnCol = end_col  # set DepartRow to latest possible date

            cal_list = [DepartRow, DepartCol, ReturnRow, ReturnCol]

            print(cal_list)
            return cal_list
        except Exception as err:
            print(str(err))
    def roundtrip_calendar_left_scroll_button(self):
        try:
            CalendarLeftScrollButton = self.driver.find_element_by_xpath("//button[@aria-label='Move backward to switch to the previous month.']")
            CalendarLeftScrollButton.click()
            print('Calendar Left Scroll Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

    def roundtrip_calendar_right_scroll_button(self):
        try:
            CalendarRightScrollButton = self.driver.find_element_by_xpath("//button[@aria-label='Move forward to switch to the next month.']")
            CalendarRightScrollButton.click()
            print('Calendar Right Scroll Button has been clicked successfully.')
        except Exception as err:
            print(str(err))

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

#TODO randomize selection of fare options from fareTypes list.
    def main_fare_dropdown_(self):
        try:
            #fareDropdown is the dropdown menu element. CLicking on it simply opens up the dropdown menu to display the 3 dropdown options: economy, premium economy, and business/first

            #This dropdown menu is not coded like normal dropdowns, with an index. This is a graphic element that must be clicked by a mouse or manipulated using keys. There are no easy selectors for each option in the dropdown, so simulating clicks via keystrokes to navigate the dropdown are the only option.

            #If this method breaks, try adjusting the time.sleep first

            wait = WebDriverWait

            economy = Keys.ENTER
            premium = Keys.ARROW_DOWN, Keys.ENTER
            business = Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER

            fareTypes = [economy, premium, business]

            fareDropdown = wait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'cabinType')))

            fareDropdown.click()
            print('Fare/Cabin Dropdown Menu has been clicked successfully.')

            time.sleep(4)

            action(self.driver).send_keys(random.choice(fareTypes)).perform()
            print('Fare/Cabin type has been selected.')

        except Exception as err:
            print(str(err))



    def traveler_randomizer(self):
        travelerOptions = ['NumOfChildren01 plusBtn', 'NumOfAdults plusBtn', 'NumOfSeniors plusBtn', 'NumOfInfants plusBtn', 'NumOfLapInfants plusBtn', 'NumOfChildren04 plusBtn', 'NumOfChildren03 plusBtn', 'NumOfChildren02 plusBtn']
        numberTravelers = random.randint(1, 8) #the total number of travelers selected
 #
        print(str(numberTravelers))
        self.main_travelers_input_field()

        for i in range(numberTravelers):
            x = random.randint(0, 7)
            print(str(x))
            self.driver.find_element_by_id(travelerOptions[x]).click()
            print(travelerOptions[x] + ' was clicked.')


    def main_find_flights_button(self):
        findFlightsButton = self.driver.find_element_by_xpath('//button[@aria-label="Find flights"]')
        findFlightsButton.click()

    def main_advanced_search_button(self):
        advancedSearchButton = self.driver.find_element_by_xpath('//span[contains(text(), "Advanced search")]')
        advancedSearchButton.click()

    def changed_bag_rules(self):
        changedBagRulesLink = self.driver.find_element_by_xpath('//span[contains(text(), "Changed bag rules")]')
        changedBagRulesLink.click()

    def optional_services_link(self):
        optionalServicesLink = self.driver.find_element_by_xpath('//span[contains(text(), "optional services")]')
        optionalServicesLink.click()

#The following are selectors for the United Advanced Search page

    #This method allows you to click on the Recent Searches dropdown menu, which appears on the Advanced Search page.
    def recent_searches(self):
        recentSearchDropdown = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'recentSearch-text')))
        recentSearchDropdown.click()

    #This method allows you to click on the No button in the "Do you want to book a MileagePlus award ticket?" section on the Advanced Search page. The No button is selected by default when the page loads.
    def mileage_plus_no_button(self):
        mileageNoButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="RedeemMiles_noRMiles"]')))
        mileageNoButton.click()

    # This method allows you to click on the Yes button in the "Do you want to book a MileagePlus award ticket?" section on the Advanced Search page. The No button is selected by default when the page loads.
    def mileage_plus_yes_button(self):
        mileageYesButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="RedeemMiles_rMiles"]')))
        mileageYesButton.click()

    #This method will allow you to select the One-way button under the "Trip type" section on the Advanced Search page. Roundtrip is selected by default.
    def oneway_button_advanced_search(self):
        onewayButtonAdvanced = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'TripTypes_ow')))
        onewayButtonAdvanced.click()

    #This method will allow you to select the Roundtrip button under the "Trip type" section on the Advanced Search page. Roundtrip is selected by default.
    def roundtrip_button_advanced_search(self):
        roundtripButtonAdvanced = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'TripTypes_rt')))
        roundtripButtonAdvanced.click()

    #This method will allow you to select the Multi-City button under the "Trip type" section on the Advanced Search page. Roundtrip is selected by default.
    def multicity_button_advanced_search(self):
        multicityButtonAdvanced = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'TripTypes_rt')))
        multicityButtonAdvanced.click()