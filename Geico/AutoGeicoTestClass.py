from selenium import webdriver
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains as action
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
import string

class Auto_Geico_Test:

    chrome_options = webdriver.ChromeOptions

    driver = webdriver
    wait = WebDriverWait
    ErrorCount = 0
    CurrentModule = ""

    # used to display the maximum index for the current select list
    MaxYearIndex = 5
    MaxMakeIndex = 5
    MaxModelIndex = 5
    MaxBodyStyleIndex = 5
    MaxNewCostIndex = 5
    MaxAnnualMilesIndex = 5
    MaxAntitheftDeviceIndex = 5
    MaxDaysDrivenIndex = 5
    MaxTypeOfBusinessUseIndex = 5
    MaxOccupationIndex = 5

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-icognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)

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

    def close_browser(self):
        self.driver.quit()

    # function for generic buttons
    def go_next(self):
        try:
            self.CurrentModule = "go_next"
            time.sleep(1)
            NextButton0 = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
            action(self.driver).move_to_element(NextButton0).click().click().perform()
            self.loadtime()
        except Exception as err:
            self.error_message(err)

    def zip_input_0(self):
        self.driver.get('http://geico.com')
        zipInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(zipInput0).click().send_keys('60629').send_keys(u'\ue007').perform()
        self.loadtime()
        print('\tZip has been found and entered. ZIP: ' + '60629')
        return

    #Testing the 1st of 5 options -- "I need insurance right away"
    def customer_intent_0(self):
        CustomerIntent0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent0']")))
        CustomerIntent0.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        print('\tCustomerIntent0 (I need insurance right away) has been selected.')
        return

    # Testing the 2nd of 5 options -- "I am buying or just bought a car"
    def customer_intent_1(self):
        CustomerIntent1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent1']")))
        CustomerIntent1.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        print('\tCustomerIntent1 (I am buying or just bought a car) has been selected.')
        return

    #Testing the 3rd of 5 options -- "I'm looking for a better price"
    def customer_intent_2(self):
        CustomerIntent2 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent2']")))
        CustomerIntent2.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        print('\tCustomerIntent2 (Im looking for a better price) has been selected.')
        return

    #Testing the 4th of 5 options -- "I'm comparing rates for different cars"
    def customer_intent_3(self):
        CustomerIntent3 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent3']")))
        CustomerIntent3.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        print('\tCustomerIntent3 (Im comparing rates for different cars) has been selected.')
        return

    #Testing the 5th of 5 options -- "I'm just shopping today"
    def customer_intent_4(self):
        CustomerIntent4 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent4']")))
        CustomerIntent4.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        print('\tCustomerIntent4 (Im just shopping today) has been selected.')
        return

#Skipping the customer intent page
    def customer_intent_5(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='button-bar']")
        #CustomerIntent5 = self.wait.until(ec.element_to_be_clickable((By.__class__, "button-bar")))
        CustomerIntent5 = self.driver.find_element_by_xpath("//*[@id='auto-customer-collect-intent-modal']/div/div/div/div[1]/div/div[2]/a")
        CustomerIntent5.click()
        #BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        #BeginQuoteButton0.click()
       # NextButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='btn.btn--primary']")))
        #NextButton0.click()
        print('\tCustomerIntent5 has been selected.')
        return

    def skip_help_page_0(self):
        try:
            time.sleep(2)
            butbar = self.driver.find_element_by_class_name("button-bar")
            SkipA0 = butbar.find_element_by_class_name("skip-collect-intent.link--primary")
            action(self.driver).move_to_element(SkipA0).click().perform()
            print('\tSkip_help_page_0 has been selected. to skip Customer Intent options.')
        except:
            self.customer_intent_0()

    #Testing the Next Button after selecting your Customer Intent
    def next_button_0(self):
        time.sleep(2)
        NextButton0 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton0.click()
        print('\tNext button has been selected to proceed from Customer Intent selection.')
        return

    #Entering first name into dialogue box
    def first_name_input_0(self):
        #Replace the string in send_keys('') to whatever you'd like.
        FirstNameInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'firstName')))
        action(self.driver).move_to_element(FirstNameInput0).click().send_keys('Abcdefghij').perform()
        print('\tFirst Name has been found and entered. First Name: ' + 'Abcdefghij')
        return

    #Entering last name into dialogue box
    def last_name_input_0(self):
        # Replace the string in send_keys('') to whatever you'd like.
        LastNameInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'lastName')))
        action(self.driver).move_to_element(LastNameInput0).click().send_keys('Ioewmaowenglweirb').perform()
        print('\tLast Name has been found and entered. Last Name: ' + 'Ioewmaowenglweirb')
        return

    #Testing the Next Button after entering First and Last Name
    def next_button_1(self):
        time.sleep(2)
        NextButton1 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton1.click()
        print('\tNext button has been selected to proceed from First and Last Name entry.')
        return

    def month_dob_0(self):
        # Replace the string in send_keys('') to a 2-digit numeric value between 01 and 12
        MonthDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-monthdob')))
        MonthDOB0.click()
        MonthDOB0.send_keys('08')
        print('\tMonth of Birth has been found and entered. Month: ' + '08')
        return

    def day_dob_0(self):
        # Replace the string in send_keys('') to a 2-digit numeric value between 01 and 31
        time.sleep(2)
        DayDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-daydob')))
        DayDOB0.click()
        DayDOB0.send_keys('08')
        print('\tDay of Birth has been found and entered. Day: ' + '08')
        return

    def year_dob_0(self):
        # Replace the string in send_keys('') to a 4-digit numeric value between 1900 and 2000
        YearDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-yeardob')))
        YearDOB0.click()
        YearDOB0.send_keys('1990')
        print('\tYear of Birth has been found and entered. Year: ' + '1990')
        return

    def month_dob_0_rand(self):
        # Replace the string in send_keys('') to a 2-digit numeric value between 01 and 12
        MonthDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-monthdob')))
        MonthDOB0.click()
        MonthDOB0.send_keys(random.randint(1, 12))
        print('Month of Birth has been found and entered. Month: ' + '08')
        return

    def day_dob_0_rand(self):
        # Replace the string in send_keys('') to a 2-digit numeric value between 01 and 31
        time.sleep(2)
        DayDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-daydob')))
        DayDOB0.click()
        DayDOB0.send_keys(random.randint(1, 30))
        print('Day of Birth has been found and entered. Day: ' + '08')
        return

    def year_dob_0_rand(self):
        # Replace the string in send_keys('') to a 4-digit numeric value between 1900 and 2000
        YearDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-yeardob')))
        YearDOB0.click()
        YearDOB0.send_keys(str(random.randint(1920, 2000)))
        print('Year of Birth has been found and entered. Year: ' + '1990')
        return

    def next_button_2(self):
        time.sleep(2)
        NextButton2 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton2.click()
        print('\tNext button has been selected to proceed from DOB entry.')
        return

#what is your address funtions
    def street_input_0(self):
        StreetInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'street')))
        action(self.driver).move_to_element(StreetInput0).click().send_keys('6609 S Karlov').perform()
        print('\tStreet Address has been found and entered. Street: ' + '6609 S Karlov')
        return

    def apt_input_0(self):
        AptInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'apt')))
        action(self.driver).move_to_element(AptInput0).click().send_keys('3').perform()
        print('\tApartment Number has been found and entered. Apartment Number: ' + '3')
        return

    def zip_input_1(self):
        ZipInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(ZipInput1).click().send_keys('60629').perform()
        print('\tZip has been found and entered. ZIP: ' + '60629')
        return

    def next_button_3(self):
        time.sleep(2)
        NextButton3 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton3.click()
        print('\tNext button has been selected to proceed from Address entry.')
        return

    def verify_address_0(self):
        OriginalAddressLabel0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='originalAddress']")))
        OriginalAddressLabel0.click()
        print('\tAddress Verification has been found and selected.')
        return

    def next_button_4(self):
        NextButton4 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton4.click()
        print('Next button has been selected to proceed from Address Verification.')
        return

    def have_you_moved(self):
        HasMovedInLast2MonthsLabel1 = self.driver.find_element_by_xpath("//label[@for='hasMovedInLast2Months1']")
        action(self.driver).move_to_element(HasMovedInLast2MonthsLabel1).click().send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        print('\tHasMovedInLast2MonthsLabel1 has been selected.')
        return

    def next_button_3(self):
        time.sleep(2)
        NextButton3 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton3.click()
        print('\tNext button has been selected to proceed from Have you moved?.')
        return

    def vehicle_not_listed_class_0(self):
        try:
            time.sleep(8)
            VehicleNotListed = self.driver.find_element_by_xpath("//label[@for='chkVehicle2']")
            VehicleNotListed.click()
            print('\tVehicle has been selected.')
        except:
            VehicleNotListed = self.driver.find_element_by_xpath("//label[@for='chkVehicle2']")
            VehicleNotListed.click()
        return

    def next_button_x(self):
        time.sleep(2)
        NextButtonx = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButtonx.click()
        print('\tNext button has been selected.')
        return

    def select_antitheft_devices(self):
        try:
            self.CurrentModule = "select_antitheft_devices"

            AntiTheftDeviceSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='antiTheftDevice']"))))

            self.MaxAntitheftDeviceIndex = len(AntiTheftDeviceSelect0.options)
            ATDOption = 0

            while ATDOption < len(AntiTheftDeviceSelect0.options):
                AntiTheftDeviceSelect0.select_by_index(ATDOption)
                ATDOption = ATDOption + 1
                print('\tAnti-theft device has been selected.')
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = no anti theft, 1 = alarm only/active disabling device, 2 = passive disabling device
    def select_specific_antitheft_device(self, index):
        try:
            self.CurrentModule = "select_specific_antitheft_device"
            AntiTheftDeviceSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='antiTheftDevice']"))))
            AntiTheftDeviceSelect0.select_by_index(index)
            self.MaxAntitheftDeviceIndex = len(AntiTheftDeviceSelect0.options)
            print('\tAnti-theft device has been selected.')
            self.go_next()
            print('\tNext button has been selected.')
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = no anti theft, 1 = alarm only/active disabling device, 2 = passive disabling device
    def select_specific_antitheft_device_unlisted(self, index):
        try:
            self.CurrentModule = "select_specific_antitheft_device"
            AntiTheftDeviceSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='antiTheftDeviceunlisted']"))))
            AntiTheftDeviceSelect0.select_by_index(index)
            self.MaxAntitheftDeviceIndex = len(AntiTheftDeviceSelect0.options)
            print('\tAnti-theft device has been selected.')
            self.go_next()
            print('\tNext button has been selected.')
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = owned, 1 = financed, 2 = leased


    def select_ownership(self, index):
        try:
            time.sleep(3)

            if index == 0:
                VehicleOwned0 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned0']")
                action(self.driver).move_to_element(VehicleOwned0).click().perform()
            if index == 1:
                VehicleOwned1 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned1']")
                action(self.driver).move_to_element(VehicleOwned1).click().perform()
            if index == 2:
                VehicleOwned2 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned2']")
                action(self.driver).move_to_element(VehicleOwned2).click().perform()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # index guide
    # 0 = owned, 1 = financed, 2 = leased

    def select_ownership_unlisted(self, index):
        try:
            time.sleep(3)

            if index == 0:
                VehicleOwned0 = self.driver.find_element_by_xpath("//label[@for='vehicleOwnedunlisted0']")
                action(self.driver).move_to_element(VehicleOwned0).click().perform()
            if index == 1:
                VehicleOwned1 = self.driver.find_element_by_xpath("//label[@for='vehicleOwnedunlisted1']")
                action(self.driver).move_to_element(VehicleOwned1).click().perform()
            if index == 2:
                VehicleOwned2 = self.driver.find_element_by_xpath("//label[@for='vehicleOwnedunlisted2']")
                action(self.driver).move_to_element(VehicleOwned2).click().perform()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # index guide
    # 0 = commute, 1 = pleasure, 2 = business


    def select_primary_use(self, index):
        try:
            time.sleep(3)

            if index == 0:
                PrimaryUse0 = self.driver.find_element_by_xpath("//label[@for='primaryUse0']")
                action(self.driver).move_to_element(PrimaryUse0).click().perform()
                self.primary_use_commute()
            if index == 1:
                PrimaryUse1 = self.driver.find_element_by_xpath("//label[@for='primaryUse1']")
                action(self.driver).move_to_element(PrimaryUse1).click().perform()
            if index == 2:
                PrimaryUse2 = self.driver.find_element_by_xpath("//label[@for='primaryUse2']")
                action(self.driver).move_to_element(PrimaryUse2).click().perform()
                self.primary_use_business()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    def select_primary_use_unlisted(self, index):
        try:
            time.sleep(3)

            if index == 0:
                PrimaryUse0 = self.driver.find_element_by_xpath("//label[@for='primaryUseunlisted0']")
                action(self.driver).move_to_element(PrimaryUse0).click().perform()
                self.primary_use_commute_unlisted()
            if index == 1:
                PrimaryUse1 = self.driver.find_element_by_xpath("//label[@for='primaryUseunlisted1']")
                action(self.driver).move_to_element(PrimaryUse1).click().perform()
            if index == 2:
                PrimaryUse2 = self.driver.find_element_by_xpath("//label[@for='primaryUseunlisted2']")
                action(self.driver).move_to_element(PrimaryUse2).click().perform()
                self.primary_use_business_unlisted()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # menu options for commuting
    def primary_use_commute(self):
        try:
            time.sleep(1)
            DaysDrivenSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='daysDriven']"))
            DaysDrivenSelect0.select_by_index(random.randint(1, len(DaysDrivenSelect0.options)))
            self.MaxDaysDrivenIndex = len(DaysDrivenSelect0.options)
            MilesDrivenInput0 = self.driver.find_element_by_xpath("//input[@id='milesDriven']")
            action(self.driver).move_to_element(MilesDrivenInput0).click().send_keys(str(miles)).perform()
            print('\tPrimary Use of Vehicle has been selected.')
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # menu options for commuting
    def primary_use_commute_unlisted(self):
        try:
            time.sleep(1)
            DaysDrivenSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='daysDrivenunlisted']"))
            DaysDrivenSelect0.select_by_index(random.randint(1, len(DaysDrivenSelect0.options)))
            self.MaxDaysDrivenIndex = len(DaysDrivenSelect0.options)
            MilesDrivenInput0 = self.driver.find_element_by_xpath("//input[@id='milesDrivenunlisted']")
            action(self.driver).move_to_element(MilesDrivenInput0).click().send_keys(str(self.random_int(3))).perform()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    def select_annual_mileage(self, index):
        try:
            time.sleep(1)
            AnnualMileageSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='annualMileage']"))
            self.MaxAnnualMilesIndex = len(AnnualMileageSelect0.options)
            AnnualMileageSelect0.select_by_index(index)
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    def select_annual_mileage_unlisted(self, index):
        try:
            time.sleep(1)
            AnnualMileageSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='annualMileageunlisted']"))
            self.MaxAnnualMilesIndex = len(AnnualMileageSelect0.options)
            AnnualMileageSelect0.select_by_index(index)
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    def primary_use_business(self):
        try:
            time.sleep(1)
            TypeOfBusinessUseSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='typeOfBusinessUse']"))
            self.MaxTypeOfBusinessUseIndex = len(TypeOfBusinessUseSelect0.options)
            TypeOfBusinessUseSelect0.select_by_index(random.randint(1, len(TypeOfBusinessUseSelect0.options) - 1))
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    def primary_use_business_unlisted(self):
        try:
            time.sleep(1)
            TypeOfBusinessUseSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='typeOfBusinessUseunlisted']"))
            self.MaxTypeOfBusinessUseIndex = len(TypeOfBusinessUseSelect0.options)
            TypeOfBusinessUseSelect0.select_by_index(random.randint(1, len(TypeOfBusinessUseSelect0.options) - 1))
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # only use this to pass through this stage, not good for testing functionality
    # indices available is reliant on the previous elements
    def select_specific_vehicle(self, year_index, make_index, model_index):
        try:
            self.CurrentModule = "select_specific_vehicle"
            VehicleYearSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
            self.MaxYearIndex = len(VehicleYearSelect0.options)
            VehicleYearSelect0.select_by_index(year_index)
            VehicleMakeSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))
            self.MaxMakeIndex = len(VehicleMakeSelect0.options)
            VehicleMakeSelect0.select_by_index(make_index)
            VehicleModelSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))
            self.MaxModelIndex = len(VehicleModelSelect0.options)
            VehicleModelSelect0.select_by_index(model_index)

            self.go_next()

        except Exception as err:
            self.error_message_vehicle(err, year_index, make_index, model_index)

    # only use this to pass through this stage, not good for testing functionality
    # indices available is reliant on the previous elements
    def select_specific_vehicle_unlisted(self, year_index, make_index, model_index):
        try:
            self.CurrentModule = "select_specific_vehicle"
            VehicleYearSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYearunlisted']"))))
            self.MaxYearIndex = len(VehicleYearSelect0.options)
            VehicleYearSelect0.select_by_index(year_index)
            VehicleMakeSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMakeunlisted']"))))
            self.MaxMakeIndex = len(VehicleMakeSelect0.options)
            VehicleMakeSelect0.select_by_index(make_index)
            VehicleModelSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModelunlisted']"))))
            self.MaxModelIndex = len(VehicleModelSelect0.options)
            VehicleModelSelect0.select_by_index(model_index)

            self.go_next()

        except Exception as err:
            self.error_message_vehicle(err, year_index, make_index, model_index)

    def select_vehicles(self):

        self.CurrentModule = "select_vehicles"

        ### NOW WE CAN TEST FOR THE ADDING OF VEHCILES ###

        VehicleYearSelect0 = Select(
            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))

        YearOption = 0

        while YearOption < len(VehicleYearSelect0.options) - 1:
            try:
                VehicleYearSelect0.select_by_index(YearOption)
            except:
                VehicleYearSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
                VehicleYearSelect0.select_by_index(YearOption)

            VehicleMakeSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))

            MakeOption = 1
            while MakeOption < len(VehicleMakeSelect0.options):
                try:
                    VehicleMakeSelect0.select_by_index(MakeOption)
                except:
                    VehicleMakeSelect0 = Select(
                        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))
                    VehicleMakeSelect0.select_by_index(MakeOption)

                VehicleModelSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))

                ModelOption = 1
                while ModelOption < len(VehicleModelSelect0.options):  # it really starts to slow down over here
                    try:
                        VehicleModelSelect0.select_by_index(ModelOption)
                    except:
                        VehicleModelSelect0 = Select(
                            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))
                        VehicleModelSelect0.select_by_index(ModelOption)

                    # time.sleep(1)
                    ModelOption = ModelOption + 1
                MakeOption = MakeOption + 1
            YearOption = YearOption + 1

    def select_vehicles_unlisted(self):

        self.CurrentModule = "select_vehicles"

        ### NOW WE CAN TEST FOR THE ADDING OF VEHCILES ###

        VehicleYearSelect0 = Select(
            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYearunlisted']"))))

        YearOption = 1

        while YearOption < len(VehicleYearSelect0.options) - 1:
            try:
                VehicleYearSelect0.select_by_index(YearOption)
            except:
                VehicleYearSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYearunlisted']"))))
                VehicleYearSelect0.select_by_index(YearOption)

            VehicleMakeSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMakeunlisted']"))))

            MakeOption = 1
            while MakeOption < len(VehicleMakeSelect0.options):
                try:
                    VehicleMakeSelect0.select_by_index(MakeOption)
                except:
                    VehicleMakeSelect0 = Select(
                        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMakeunlisted']"))))
                    VehicleMakeSelect0.select_by_index(MakeOption)

                VehicleModelSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModelunlisted']"))))

                ModelOption = 1
                while ModelOption < len(VehicleModelSelect0.options):  # it really starts to slow down over here
                    try:
                        VehicleModelSelect0.select_by_index(ModelOption)
                    except:
                        VehicleModelSelect0 = Select(
                            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModelunlisted']"))))
                        VehicleModelSelect0.select_by_index(ModelOption)

                    # time.sleep(1)
                    ModelOption = ModelOption + 1
                MakeOption = MakeOption + 1
            YearOption = YearOption + 1

    def add_vehicle_pre1981(self, year, make, model):
        try:
            self.CurrentModule = "add_vehicle_pre1981"

            VehicleYearSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
            VehicleYearSelect0.select_by_index(len(VehicleYearSelect0.options) - 1)

            ActualVehicleYearInput0 = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//input[@id='actualVehicleYear']")))
            action(self.driver).move_to_element(ActualVehicleYearInput0).click().send_keys(
                str(year)).perform()

            OtherMakeInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherMake']")))
            action(self.driver).move_to_element(OtherMakeInput0).click().send_keys(str(make)).perform()

            OtherModelInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherModel']")))
            action(self.driver).move_to_element(OtherModelInput0).click().send_keys(str(model)).perform()

            self.go_next()
        except Exception as err:
            self.error_message_vehicle(err, year, make, model)

    def add_vehicle_pre1981_unlisted(self, year, make, model):
        try:
            self.CurrentModule = "add_vehicle_pre1981"

            VehicleYearSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYearunlisted']"))))
            VehicleYearSelect0.select_by_index(len(VehicleYearSelect0.options) - 1)

            ActualVehicleYearInput0 = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//input[@id='actualVehicleYearunlisted']")))
            action(self.driver).move_to_element(ActualVehicleYearInput0).click().send_keys(
                str(year)).perform()

            OtherMakeInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherMakeunlisted']")))
            action(self.driver).move_to_element(OtherMakeInput0).click().send_keys(str(make)).perform()

            OtherModelInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherModelunlisted']")))
            action(self.driver).move_to_element(OtherModelInput0).click().send_keys(str(model)).perform()

            self.go_next()
        except Exception as err:
            self.error_message_vehicle(err, year, make, model)

    def select_body_styles(self):
        try:
            self.CurrentModule = "select_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStyles']"))))

            BSSOption = 0
            while BSSOption < len(BodyStylesSelect0.options):
                BodyStylesSelect0.select_by_index(BSSOption)
                BSSOption = BSSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_body_style(self, index):
        try:
            self.CurrentModule = "select_specific_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStyles']"))))
            self.MaxBodyStyleIndex = len(BodyStylesSelect0.options)
            BodyStylesSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_specific_body_style_unlisted(self, index):
        try:
            self.CurrentModule = "select_specific_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStylesunlisted']"))))
            self.MaxBodyStyleIndex = len(BodyStylesSelect0.options)
            BodyStylesSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_new_costs(self):

        try:
            self.CurrentModule = "select_new_costs"

            CostNewValueSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='costNewValue']"))))
            self.MaxNewCostIndex = len(CostNewValueSelect0.options)
            CNVSOption = 0
            while CNVSOption < len(CostNewValueSelect0.options):
                CostNewValueSelect0.select_by_index(CNVSOption)
                CNVSOption = CNVSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_new_costs(self, index):

        try:
            self.CurrentModule = "select_specific_new_costs"

            CostNewValueSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='costNewValue']"))))
            self.MaxNewCostIndex = len(CostNewValueSelect0.options)
            CostNewValueSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def random_int(self, len):
        return random.randint(pow(10, len-1), pow(10, len))

    def random_string(self, len):
        return ''.join([random.choice(string.ascii_letters) for n in range(len)])

    def select_specific_new_costs_unlisted(self, index):

        try:
            self.CurrentModule = "select_specific_new_costs"

            CostNewValueSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='costNewValueunlisted']"))))
            self.MaxNewCostIndex = len(CostNewValueSelect0.options)
            CostNewValueSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_antilock_brakes(self, index):
        try:

            self.CurrentModule = "select_antilock_brakes"

            if index == 0:
                AntilockBrakesLabel0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakes0']")))
                action(self.driver).move_to_element(AntilockBrakesLabel0).click().perform()
                self.go_next()
            if index == 1:
                AntilockBrakesLabel1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakes1']")))
                action(self.driver).move_to_element(AntilockBrakesLabel1).click().perform()
                self.go_next()

        except Exception as err:
            self.error_message(err)

    def select_antilock_brakes_unlisted(self, index):
        try:

            self.CurrentModule = "select_antilock_brakes"

            if index == 0:
                AntilockBrakesLabel0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakesunlisted0']")))
                action(self.driver).move_to_element(AntilockBrakesLabel0).click().perform()
                self.go_next()
            if index == 1:
                AntilockBrakesLabel1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakesunlisted1']")))
                action(self.driver).move_to_element(AntilockBrakesLabel1).click().perform()
                self.go_next()

        except Exception as err:
            self.error_message(err)

    #skipped ahead to Driver Info, missing a couple Nexts and other options; am labeling Next Buttons below according to the Excel spreadsheet, beginning on cell Q3

    def name_change_0(self):
        NameChange0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'changeName')))
        NameChange0.click()

        FirstNameInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'firstName')))
        action(self.driver).move_to_element(FirstNameInput1).click().send_keys('Abcdefghij').perform()

        LastNameInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'lastName')))
        action(self.driver).move_to_element(LastNameInput1).click().send_keys('Ioewmaowenglweirb').perform()

        return

    def gender_select_0(self):
        #index values: value "F" = female; value "M" = Male

        time.sleep(2)
        GenderSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='gender']"))
        time.sleep(2)
        GenderSelect0.select_by_index(1)
        time.sleep(4)
        #NextButton4 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        #NextButton4.click()
        return

    def marital_status_0(self):
        #Index values for dropdown: "S" = Single; "D" = Divorced; "M" = Married; "B" = Civil Union; "E" = Separated; "W" = Widowed

        MaritalStatusSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='maritalStatus']"))
        MaritalStatusSelect0.select_by_index(random.randint(1, 6))
        return

    def social_security_number_0(self):
        #negative test case to determine whether element will accept alphabet characters
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('Ioewmaowenglweirb').perform()
        return

    def social_security_number_1(self):
        #test case to determine whether element will accept 8 numeric characters (the full length of a SSN)
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('543736234').perform()
        return

    def social_security_number_2(self):
        #test case to determine whether element will accept fewer than 8 numeric characters (a partial SSN)
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('123456').perform()
        return

    # these functions get you to the page to add vehicles
    def get_to_vehicle_page(self):
        self.driver.get("https://www.geico.com/")
        self.zip_input_0()
        self.skip_help_page_0()
        self.go_next()
        self.first_name_input_0()
        self.last_name_input_0()
        self.go_next()
        self.month_dob_0()
        self.day_dob_0()
        self.year_dob_0()
        self.go_next()
        self.street_input_0()
        self.apt_input_0()
        self.zip_input_1()
        self.go_next()
        self.vehicle_not_listed_class_0()
        self.go_next()


    def error_message(self, err):
        self.ErrorCount = self.ErrorCount + 1
        print("Exception thrown on module:\t" + str(self.CurrentModule))
        print(str(err))
        print("Error Count:\t" + str(self.ErrorCount))

    def error_message_vehicle(self, err, year, make, model):
        self.error_message(err)
        print("Year:\t" + str(year) + " Make:\t" + str(make) + " Model:\t" + str(model))


    #Testing "Own" radio button on Do You Own Or Rent Your Home? page
    def home_ownership_0(self):
        OwnLabel0 = self.driver.find_element_by_xpath("//label[@for='ownOrRentHome0']")
        action(self.driver).move_to_element(OwnLabel0).click().perform()
        return

    #Testing "Rent" radio button on Do You Own Or Rent Your Home? page
    def home_ownership_1(self):
        RentLabel0 = self.driver.find_element_by_xpath("//label[@for='ownOrRentHome1']")
        action(self.driver).move_to_element(RentLabel0).click().perform()
        return

    #testing each option in the Do You Currently Have Auto Insurance? dropdown menu
    def current_insured_status_0(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(0)
        return

    def current_insured_status_1(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(1)
        return

    def current_insured_status_2(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(2)
        return

    def current_insured_status_3(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(3)
        return

    def current_insured_status_4(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(4)
        return

    #Testing each element on the Previous Insurance disclosure page (title: "Tell us more about your previous insurance").
    # 3 major element groups on this page: a dropdown menu where you can select how many years you had been continuously covered by previous insurer when your insurance ran out; 2 radio buttons for the question "Have you had insurance within the last 30 days?"; and another dropdown menu labelled "Previous Bodily Injury Limits"
    def previous_insurance_disclosure_0(self):
        #Testing 1st dropdown menu. Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index/values: index 0/value is blank; index 1/value "0" = Less than 1; index 2/value "1" = 1; index 3/value "2" = 2; index 4/value "3" = 3; index 5/value "4" = 4; index 6/value "5" = 5; index 7/value "6" = 6; index 8/value "7" = 7; index 9/value "8" = 8; index 10/value "9" = 9; index 11/value "10" = 10; index 12/value "11" = 11 or more
        PreviousInsuranceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='yearsInsured']"))
        PreviousInsuranceSelect0.select_by_index(random.randint(1, 11))
        return

    def previous_insurance_disclosure_1(self):
        #Testing radio button elements
        Last30DaysYes = self.driver.find_element_by_xpath("//label[@for='lastInsurance0']")
        action(self.driver).move_to_element(Last30DaysYes).click().perform()
        return

    def previous_insurance_disclosure_2(self):
        #Testing radio button elements
        Last30DaysNo = self.driver.find_element_by_xpath("//label[@for='lastInsurance1']")
        action(self.driver).move_to_element(Last30DaysNo).click().perform()
        return

    def previous_insurance_disclosure_3(self):
        #Testing Previous Bodily Injury Limits dropdown menu. Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index/values: index 0/value is blank; index 1/value "025" = "$25,000/$50,000"; index 2/value "051" = "$50,000/$100,000" ; index 3/value "120" = "$100,000/$200,000"; index 4/value "130" = "$100,000/$300,000"; index 5/value "330" = "$300,000/$300,000"; index 6/value "250" = "$250,000/$500,000 or higher"; index 7/value "997" = "Not Sure"
        PreviousBILimits0 = Select(self.driver.find_element_by_xpath("//select[@id='currentBILimits']"))
        PreviousBILimits0.select_by_index(random.randint(1, 7))
        return

    # Testing each element on the Current Insurance disclosure page (title: "Tell us more about your current insurance").
    # 3 major element groups on this page: a dropdown menu where you can select how many years you have been covered by your current insurance company; 2 radio buttons for the question "Have you had continuous insurance for the past 12 months?"; and another dropdown menu labelled "Current Bodily Injury Limits"
    def current_insurance_disclosure_0(self):
        # Testing 1st dropdown menu. Insert the index value you'd like to select into the parentheses in select_by_index()
        # Dropdown index/values: index 0/value is blank; index 1/value "0" = Less than 1; index 2/value "1" = 1; index 3/value "2" = 2; index 4/value "3" = 3; index 5/value "4" = 4; index 6/value "5" = 5; index 7/value "6" = 6; index 8/value "7" = 7; index 9/value "8" = 8; index 10/value "9" = 9; index 11/value "10" = 10; index 12/value "11" = 11 or more
        CurrentInsuranceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='yearsInsured']"))
        CurrentInsuranceSelect0.select_by_index(random.randint(1, 11))
        return

    def current_insurance_disclosure_1(self):
        # Testing radio button elements for "Yes" option
        Last12MonthsYes = self.driver.find_element_by_xpath("//label[@for='insuranceLapse12months0']")
        action(self.driver).move_to_element(Last12MonthsYes).click().perform()
        return

    def current_insurance_disclosure_3(self):
        # Testing radio button elements for "Yes" option
        Last12MonthsNo = self.driver.find_element_by_xpath("//label[@for='insuranceLapse12months1']")
        action(self.driver).move_to_element(Last12MonthsNo).click().perform()
        return

    def current_insurance_disclosure_4(self):
        # Testing Current Bodily Injury Limits dropdown menu. Insert the index value you'd like to select into the parentheses in select_by_index()
        # Dropdown index/values: index 0/value is blank; index 1/value "025" = "$25,000/$50,000"; index 2/value "051" = "$50,000/$100,000" ; index 3/value "120" = "$100,000/$200,000"; index 4/value "130" = "$100,000/$300,000"; index 5/value "330" = "$300,000/$300,000"; index 6/value "250" = "$250,000/$500,000 or higher"; index 7/value "997" = "Not Sure"
        CurrentBILimits0 = Select(self.driver.find_element_by_xpath("//select[@id='currentBILimits']"))
        CurrentBILimits0.select_by_index(random.randint(1, 7))
        return

    # Testing "Tell us more about your driving history" page. Contains 2 radio buttons: Yes and No. Selecting Yes will advance you to a new screen. Selecting No will add a new dialogue box to the current screen, prompting you to input your age when you became licensed.
    def driving_history_0(self):
        LicensedBefore22Yes = self.driver.find_element_by_xpath("//label[@for='licensedBeforeCertainAge0']")
        action(self.driver).move_to_element(LicensedBefore22Yes).click().perform()
        return

    def driving_history_1(self):
        LicensedBefore22No = self.driver.find_element_by_xpath("//label[@for='licensedBeforeCertainAge1']")
        action(self.driver).move_to_element(LicensedBefore22No).click().perform()
        AgeFirstLicensesInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ageFirstLicensed')))
        action(self.driver).move_to_element(AgeFirstLicensesInput0).click().send_keys('21').perform()
        return

    # Testing Driver Information - What is the highest level of education you have completed?
    def education_level_0(self):
        #Insert the index value you'd like to select into the parentheses in select_by_index()
        # Dropdown index: index 0 = blank space; index 1 = "Less than High School; index 2 = Vocational; index 3 = High School; index 4 = High school, pursuing Bachelor's degree; index 5 = Associate; index 6 = Associate, pursuing Bachelor's degree; index 7 = Bachelor's; index 8 = Bachelor's, pursuing Graduate Degree; index 9 = Master's; index 10 = Doctors; index 11 = Lawyer; index 12 = PhD
        HighestEducation0 = Select(self.driver.find_element_by_xpath("//select[@id='highestEducation']"))
        HighestEducation0.select_by_index(random.randint(1, 12))
        return

# Testing Driver Information - Employment status. Single element on page is a dropdown menu; selecting any Military or Federal Gov options will create new dropdown menus to select from.
    def employment_status_0(self):
        #Insert the index value you'd like to select into the parentheses in select_by_index()
        # Dropdown index: index 0 = blank space; index 1 = A Private Company/Self Employed; index 2 = Active Duty Military; index 3 = Federal Gov or Postal Service; index 4 = State/Local/Municipal Gov; index 5 = I am a Full Time Student; index 6 = I am currently a Homemaker; index 7 = Not Currently Employed; index 8 = Retired Private Company/Self Employed; index 9 = Retired Military; index 10 = Retired Federal Gov; index 11= Retired State/Local/Municipal Gov
        EmploymentStatus0 = Select(self.driver.find_element_by_xpath("//select[@id='employmentStatus']"))
        EmploymentStatus0.select_by_index(random.randint(1, 11))
        return

    #Secondary dropdown menu triggered by selecting Active Duty Military; you must now select which branch of the military you belong to.
    def employment_status_1(self):
        #Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index: index 0 = blank; index 1 = Air Force; index 2 = Army; index 3 = Coast Guard; index 4 = Marine Corps; index 5 = Navy; index 6 = Foreign Officer(non-US military)
        MilitaryBranchSelect0 =  Select(self.driver.find_element_by_xpath("//select[@id='branchOfMilitary']"))
        MilitaryBranchSelect0.select_by_index(random.randint(1, 6))
        return

    #Tertiary dropdown menu triggered by selecting which branch of the military you belong to; you must now select your paygrade within the military.
    def employment_status_2(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #dropdown index for Military Grade is too numerous to list out here; use index values 1 - 24
        MilitaryGradeSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='militaryGrade']"))
        MilitaryGradeSelect0.select_by_index(random.randint(1, 24))
        return

    #Secondary dropdown menu triggered by selecting Federal Goverment/Postal Service; you must now select your paygrade.
    def employment_status_3(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index for this element is too numerous to list out here.
        GovernmentGradeSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='governmentGrade']"))
        GovernmentGradeSelect0.select_by_index(random.randint(1, len(GovernmentGradeSelect0.options)))
        return

    #Secondary dropdown menu triggered by selecting Retired Military; you must now select which branch of the military you belong to.
    def employment_status_4(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index: index 0 = blank; index 1 = Air Force; index 2 = Army; index 3 = Coast Guard; index 4 = Marine Corps; index 5 = Navy; index 6 = Foreign Officer(non-US military)
        MilitaryBranchSelect1 =  Select(self.driver.find_element_by_xpath("//select[@id='branchOfMilitary']"))
        MilitaryBranchSelect1.select_by_index(random.randint(1, 6))
        return

    #Tertiary dropdown menu triggered by selecting which branch of the military you belonged to before retirement; you must now select your paygrade within the military.
    def employment_status_5(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #dropdown index for Military Grade is too numerous to list out here; use index values 1 - 24
        MilitaryGradeSelect1 = Select(self.driver.find_element_by_xpath("//select[@id='militaryGrade']"))
        MilitaryGradeSelect1.select_by_index(random.randint(1, 24))
        return

    #Secondary dropdown menu triggered by selecting Retired Federal Goverment/Postal Service; you must now select your paygrade.
    def employment_status_6(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index for this element is too numerous to list out here.
        GovernmentGradeSelect1 = Select(self.driver.find_element_by_xpath("//select[@id='governmentGrade']"))
        GovernmentGradeSelect1.select_by_index(random.randint(1, len(GovernmentGradeSelect1.options)))
        return

    def type_of_student_0(self):
        #dropdown element for the type of student; must have selected "I am a Full Time Student"
        TypeOfStudent = Select(self.driver.find_element_by_xpath("//select[@id='typeOfStudent']"))
        TypeOfStudent.select_by_index(random.randint(1, len(TypeOfStudent.options)))

#A dialogue box/search box which allows you to enter your what your occupation was before you retired; you must have previously selected Retired Private Company/Self Employed on the Employment Status page.
    def retirement_occupation_0(self):
        #Replace the string in send_keys('') with the occupation you would like to search.
        OccupationSearch0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'employmentDescription')))
        action(self.driver).move_to_element(OccupationSearch0).click().send_keys('engineer').send_keys(Keys.TAB).perform()
        return
#A second dropdown menu appears after you search for your occupation, directing you to select the closest match.
    def retirement_occupation_1(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Index values will be variable depending on how many options your search returns.
        OccupationSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='foundOccupation']"))
        OccupationSelect0.select_by_index(random.randint(1, len(OccupationSelect0.options)))

#A dialogue box/search box which allows you to enter your what your occupation is; you must have previously selected  Private Company/Self Employed on the Employment Status page.
    def current_occupation_0(self):
        #Replace the string in send_keys('') with t he occupation you would like to search.
        OccupationSearch1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'employmentDescription')))
        action(self.driver).move_to_element(OccupationSearch1).click().send_keys('engineer').perform()
        return
#A second dropdown menu appears after you search for your occupation, directing you to select the closest match.
    def current_occupation_1(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Index values will be variable depending on how many options your search returns.
        OccupationSelect1 = Select(self.driver.find_element_by_xpath("//select[@id='foundOccupation']"))

        OccupationSelect1.select_by_index(random.randint(1, len(OccupationSelect1.options)))
        return

    def military_affiliation_0(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #index for dropdown menu: index 0 = Does Not Apply; index 1 = Military Retiree; index 2 = National Guard; index 3 = Military Reserves
        MilitaryAffiliation0 = Select(self.driver.find_element_by_xpath("//select[@id='militaryAffiliation']"))
        MilitaryAffiliation0.select_by_index(random.randint(1, 3))
        return

    def military_affiliation_1(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index: index 0 = blank; index 1 = Air Force; index 2 = Army; index 3 = Coast Guard; index 4 = Marine Corps; index 5 = Navy; index 6 = Foreign Officer(non-US military)
        MilitaryAffiliationSelect1 =  Select(self.driver.find_element_by_xpath("//select[@id='militaryAffiliation']"))
        MilitaryAffiliationSelect1.select_by_index(random.randint(1, 6))

    def military_affiliation_2(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #dropdown index for Military Grade is too numerous to list out here; use index values 1 - 24
        MilitaryGradeSelect1 = Select(self.driver.find_element_by_xpath("//select[@id='militaryGrade']"))
        MilitaryGradeSelect1.select_by_index(random.randint(1, 24))
        return

    def government_affiliation_0(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #index for dropdown menu: index 0 = Does Not Apply; index 1 = Federal Gov or Postal Service; index 2 = Retired Federal Gov or Postal Service; index 3 = State/Local/Municipal Gov; index 4 = Retired State/Local/Municipal Gov
        GovernmentAffiliation0 = Select(self.driver.find_element_by_xpath("//select[@id='governmentAffiliation']"))
        GovernmentAffiliation0.select_by_index(random.randint(1, 4))
        return

    def government_affiliation_1(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index for this element is too numerous to list out here.
        GovernmentGradeSelect1 = Select(self.driver.find_element_by_xpath("//select[@id='governmentGrade']"))
        GovernmentGradeSelect1.select_by_index(random.randint(1, len(GovernmentGradeSelect1.options)))
        return

    # these functions get you to the page to add vehicles
    def get_to_vehicle_page_unlisted(self):
        self.driver.get("https://www.geico.com/")
        self.zip_input_0()
        self.skip_help_page_0()
        self.go_next()
        self.first_name_input_0()
        self.last_name_input_0()
        self.go_next()
        self.month_dob_0()
        self.day_dob_0()
        self.year_dob_0()
        self.go_next()
        self.street_input_0()
        self.apt_input_0()
        self.zip_input_1()
        self.go_next()
        self.vehicle_not_listed_class_0()
        self.go_next()

#Testing the Add Incident button; we are through the Driver Details flow and are entering the accident/suspension/conviction flow
    def add_incident(self):
        AddIncident = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Incident')]")))
        action(self.driver).move_to_element(AddIncident).click().perform()
        return

#A dropdown menu with 3 options for different types of incidents. Each option takes you through a slightly different flow.
    def incident_type(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        #Dropdown index: 0 = blank space; index 1 = Accident; index 2 = Conviction; index 3 = Suspension/Revocation
        IncidentType0 = Select(self.driver.find_element_by_xpath("//select[@id='typeOfIncidents']"))
        IncidentType0.select_by_index(random.randint(1, 3))
        return

#testing the accident flow -- must have selected Accident/index 1 from dropdown menu in incident_type. This will trigger a secondary set of radio buttons to appear beneath the Incident_type dropdown.
    def accident_flow_0(self):
        #These radio buttons ask you to select who was driving during the accident. The first radio button selects the applicant/your name as the driver. The second radio button selects "Other driver (not on policy at the time)".
        AccidentResponsibilitySelf = self.driver.find_element_by_xpath("//label[@for='involvedDriveraccident0']")
        action(self.driver).move_to_element(AccidentResponsibilitySelf).click().perform()
        return

# testing the accident flow -- must have selected Accident/index 1 from dropdown menu in incident_type. This will trigger a secondary set of radio buttons to appear beneath the Incident_type dropdown.
    def accident_flow_1(self):
        # These radio buttons ask you to select who was driving during the accident. The first radio button selects the applicant/your name as the driver. The second radio button selects "Other driver (not on policy at the time)".
        AccidentResponsibilityOther = self.driver.find_element_by_xpath("//label[@for='involvedDriveraccident1']")
        action(self.driver).move_to_element(AccidentResponsibilityOther).click().perform()
        return

        # After selecting AccidentResponsibilitySelf in accident_flow_0, you should land on a page asking "Were you primarily responsible for the accident?" and "How long ago was this accident?" Both questions have radio buttons as options.

    def accident_flow_2(self):
        ResponsibleForAccidentYes = self.driver.find_element_by_xpath("//select[@id='atFault0']")
        action(self.driver).move_to_element(ResponsibleForAccidentYes).click().perform()
        return

    def accident_flow_3(self):
        ResponsibleForAccidentNo = self.driver.find_element_by_xpath("//label[@for='involvedDriveraccident1']")
        action(self.driver).move_to_element(ResponsibleForAccidentNo).click().perform()
        return

#Each of the below radio options will take you back to the Incident landing page, without the ability to hit the back button.
    def accident_flow_4(self):
        HowLongAgoLessThan12 = self.driver.find_element_by_xpath("//label[@for='accidentDate0']")
        action(self.driver).move_to_element(HowLongAgoLessThan12).click().perform()
        return

    def accident_flow_5(self):
        HowLongAgo12to24 = self.driver.find_element_by_xpath("//label[@for='accidentDate1']")
        action(self.driver).move_to_element(HowLongAgo12to24).click().perform()
        return

    def accident_flow_6(self):
        HowLongAgo25to36 = self.driver.find_element_by_xpath("//label[@for='accidentDate2']")
        action(self.driver).move_to_element(HowLongAgo25to36).click().perform()
        return

    def accident_flow_7(self):
        HowLongAgo3to5 = self.driver.find_element_by_xpath("//label[@for='accidentDate3']")
        action(self.driver).move_to_element(HowLongAgo3to5).click().perform()
        return

#Testing Conviction flow. Must have selected Add Incident from the Incident Landing page -- index 2 on incident_type
    def conviction_flow_0(self):
    # Insert the index value you'd like to select into the parentheses in select_by_index()
    #This page has a dropdown menu has 15 options to select from, but each will take you to the same page, so there are no context dependencies. Use index 1-14 to select between the options
        ConvictionDescription = Select(self.driver.find_element_by_xpath("//select[@id='violationDescription']"))
        ConvictionDescription.select_by_index(random.randint(1, 14))
        return

    def conviction_flow_1(self):
        #This element has 4 radio buttons to respond to the question "How long ago was this ticket?"
        HowLongAgoLessThan12 = self.driver.find_element_by_xpath("//label[@for='violationDateControl0']")
        action(self.driver).move_to_element(HowLongAgoLessThan12).click().perform()
        return

    def conviction_flow_2(self):
        HowLongAgo12to24 = self.driver.find_element_by_xpath("//label[@for='violationDateControl1']")
        action(self.driver).move_to_element(HowLongAgo12to24).click().perform()
        return

    def conviction_flow_3(self):
        HowLongAgo25to36 = self.driver.find_element_by_xpath("//label[@for='violationDateControl2']")
        action(self.driver).move_to_element(HowLongAgo25to36).click().perform()
        return

    def conviction_flow_4(self):
        HowLongAgo3to5 = self.driver.find_element_by_xpath("//label[@for='violationDateControl3']")
        action(self.driver).move_to_element(HowLongAgo3to5).click().perform()
        return

#Testing Suspension flow. Must have selected Add Incident from the Incident Landing page -- index 3 on incident_type
    def suspension_flow_0(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        # This page has a dropdown menu has 5 options to select from, but each will take you to the same page, so there are no context dependencies. Use index 1-4 to select between the options
        SuspensionDetails = Select(self.driver.find_element_by_xpath("//select[@id='suspensionReason']"))
        SuspensionDetails.select_by_index(random.randint(1, 4))
        return

    def suspension_flow_1(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        # This page has a dropdown menu has 5 options to select from, but each will take you to the same page, so there are no context dependencies. Use index 1-4 to select between the options
        SuspensionStartDate = Select(self.driver.find_element_by_xpath("//select[@id='suspensionStartDate']"))
        SuspensionStartDate.select_by_index(random.randint(1, 4))
        return

    def suspension_flow_2(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        # This page has a dropdown menu has 5 options to select from, but each will take you to the same page, so there are no context dependencies. Use index 1-4 to select between the options
        SuspensionLength = Select(self.driver.find_element_by_xpath("//select[@id='lengthOfSuspensionControl']"))
        SuspensionLength.select_by_index(random.randint(1, 4))
        return

#Testing Discounts - "Is Person currently a full time student with a B average or better?"
    def discounts_0(self):
        #2 radio buttons -- "Yes" and "No"
        RadioYes = self.driver.find_element_by_xpath("//label[@for='goodStudent10']")
        action(self.driver).move_to_element(RadioYes).click().perform()
        return

# Testing Discounts - "Do you belong to any of these types of groups?" There are 8 checkbox options, and you can select as many or as few as you want before proceeding.
    def discounts_1(self):
        #8 checkboxes
        Alumni = self.driver.find_element_by_xpath("//label[@for='ALUM']")
        action(self.driver).move_to_element(Alumni).click().perform()
        return

    def discounts_2(self):
        #8 checkboxes
        Berkshire = self.driver.find_element_by_xpath("//label[@for='BERK']")
        action(self.driver).move_to_element(Berkshire).click().perform()
        return

    def discounts_3(self):
        #8 checkboxes
        BusinessOrg = self.driver.find_element_by_xpath("//label[@for='PROF']")
        action(self.driver).move_to_element(BusinessOrg).click().perform()
        return

    def discounts_4(self):
        #8 checkboxes
        CreditUnion = self.driver.find_element_by_xpath("//label[@for='CU']")
        action(self.driver).move_to_element(CreditUnion).click().perform()
        return

    def discounts_5(self):
        #8 checkboxes
        Fraternities = self.driver.find_element_by_xpath("//label[@for='FRAT']")
        action(self.driver).move_to_element(Fraternities).click().perform()
        return

    def discounts_6(self):
        #8 checkboxes
        Military = self.driver.find_element_by_xpath("//label[@for='MIL']")
        action(self.driver).move_to_element(Military).click().perform()
        return

    def discounts_7(self):
        #8 checkboxes
        EducationOrgs = self.driver.find_element_by_xpath("//label[@for='EDU']")
        action(self.driver).move_to_element(EducationOrgs).click().perform()
        return

    def discounts_8(self):
        #8 checkboxes
        Other = self.driver.find_element_by_xpath("//label[@for='OTHER']")
        action(self.driver).move_to_element(Other).click().perform()
        return

#This page brings you to Discounts - Please Select Any Group YOu Belong To. The element here is a dropdown menu with options more numerous than I can count.
    def discounts_9(self):
        # Insert the index value you'd like to select into the parentheses in select_by_index()
        DiscountGroupsSelect = Select(self.driver.find_element_by_xpath("//select[@id='sponsoredMarketingSelect']"))
        DiscountGroupsSelect.select_by_index(random.randint(1, len(DiscountGroupsSelect.options)))
        return

#This page brings you to a form where you fill out your contact information.
    def contact_information_0(self):
        #Replace the strings in send_keys('') to whatever value you'd like
        EmailAddress = self.wait.until(ec.element_to_be_clickable((By.ID, 'email')))
        action(self.driver).move_to_element(EmailAddress).click().send_keys('test@testing.com').perform()
        PhoneNumber = self.wait.until(ec.element_to_be_clickable((By.ID, 'telephoneNumber')))
        action(self.driver).move_to_element(EmailAddress).click().send_keys('5558675309').perform()
        return

    def back_button_0(self):
        time.sleep(2)
        BackButton0 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/div')
        BackButton0.click()