from AutoGeicoTestClass import Auto_Geico_Test
import sys
import time

gvt = Auto_Geico_Test()

#Precondition methods used to get initial conditions for a test case.
def preconditionA(testCaseObject):
    #these are the steps from test case(s) A in order in order to do test case B01
    testCaseObject.zip_input_0()
    testCaseObject.skip_help_page_0()
    testCaseObject.next_button_0()
    return

    #these are the steps from test cases A and B in order to do test case C01
def preconditionB(testCaseObject):
    preconditionA(testCaseObject)
    testCaseObject.first_name_input_0()
    testCaseObject.last_name_input_0()
    testCaseObject.next_button_1()
    return

    #these are the steps from test cases A, B, and C in order to do test case D01
def preconditionC(testCaseObject):
    preconditionB(testCaseObject)
    testCaseObject.month_dob_0_rand()
    testCaseObject.day_dob_0_rand()
    testCaseObject.year_dob_0_rand()
    testCaseObject.next_button_2()
    return

    #these are the steps from test cases A, B, C and D in order to do test case E01
def preconditionD(testCaseObject):
    preconditionC(testCaseObject)
    testCaseObject.street_input_0()
    testCaseObject.zip_input_1()
    testCaseObject.next_button_3()
    try:
        testCaseObject.verify_address_0()
        testCaseObject.next_button_4()
    except:
        print("unable to locate verify address")
    return

def preconditionE():
    preconditionD(gvt)
    gvt.vehicle_not_listed_class_0()
    gvt.go_next()
    gvt.select_specific_vehicle_unlisted(2, 2, 3)
    gvt.select_specific_body_style_unlisted(1)  # doesnt always run
    gvt.select_specific_new_costs(2)  # doesnt always run
    gvt.select_antilock_brakes(0)  # doesnt always run
    gvt.select_specific_antitheft_device_unlisted(0)  # doesnt always run
    gvt.select_ownership_unlisted(1)
    gvt.go_next()
    gvt.select_primary_use_unlisted(1)
    gvt.go_next()
    gvt.select_annual_mileage_unlisted(2)
    gvt.go_next()
    time.sleep(3)
    gvt.go_next()

'''NICK'S CODE'''
#TC_E01 - DRIVER INFORMATION - SELECT GENDER
try:
    preconditionE()
    time.sleep(4)
    gvt.gender_select_0()
    time.sleep(1)
    gvt.go_next()
    print("test E01 ran successfully")

except Exception as err:
    print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E01:")
    print(err.__module__)
    print(str(err))

#TC_E02 - DRIVER INFORMATION - MARITAL STATUS AND SOCIAL SECURITY NUMBER
try:

    gvt.marital_status_0()
    time.sleep(2)
    gvt.social_security_number_1()
    gvt.next_button_x()
    print("test E02 ran successfully")

except Exception as err:
    print('Test E02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E02:")
    print(err.__module__)
    print(str(err))

#TC_E03 - DRIVER INFORMATION - HOME INFORMATION
try:

    gvt.home_ownership_0()
    gvt.next_button_x()
    print("test E03 ran successfully")

except Exception as err:
    print('Test E03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E03:")
    print(err.__module__)
    print(str(err))

#TC_E04.1 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "YES"
try:
    gvt.current_insured_status_1()
    gvt.next_button_x()
    gvt.current_insurance_disclosure_0()
    gvt.current_insurance_disclosure_1()
    gvt.previous_insurance_disclosure_3()
    gvt.next_button_x()
    gvt.driving_history_1()
    gvt.next_button_x()
    print("test E04o1 ran successfully")

except Exception as err:
    print('Test E04o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o1:")
    print(err.__module__)
    print(str(err))

#TODO these need to be added to our list of test cases in the master spreadsheet, and assigned a test case id
#TC_XX01 - DRIVER INFORMATION - EDUCATION
try:
    gvt.education_level_0()
    gvt.next_button_x()
    print("test E04o4 ran successfully")

except Exception as err:
    print('Test XX01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test XX01:")
    print(err.__module__)
    print(str(err))


#TC_E05o1 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
try:
    gvt.employment_status_0()
    time.sleep(2)
    try:
        gvt.employment_status_3()
    except:
        print("nope")
    try:
        gvt.type_of_student_0()
    except:
        print("mmm nah")
    gvt.next_button_x()
    try:
        gvt.retirement_occupation_0()
    except:
        print("nah")

    try:
        time.sleep(2)
        gvt.retirement_occupation_1()
    except:
        print("nope")
    gvt.next_button_x()
    gvt.military_affiliation_0()
    try:
        time.sleep(2)
        gvt.military_affiliation_1()
    except:
        print("dgdsg")
    try:
        time.sleep(2)
        gvt.military_affiliation_2()
    except:
        print("dagd")
    gvt.next_button_x()
    try:
        gvt.employment_status_4()
    except:
        print("nada")
    try:
        gvt.employment_status_5()
    except:
        print("oh thatsa baseaball")

    gvt.next_button_x()
    try:
        gvt.government_affiliation_0()
    except:
        print("you are not a statist good for u")
    try:
        gvt.government_affiliation_1()
    except:
        print("bloop")
    gvt.next_button_x()
    print("test E05o1 ran successfully")

except Exception as err:
    print('Test E05o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o1:")
    print(err.__module__)
    print(str(err))
