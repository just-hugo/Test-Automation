from AutoGeicoTestClass import Auto_Geico_Test
from selenium import webdriver
gvt = Auto_Geico_Test()

ErrorCount = 0

#TODO REMOVE THIS
#walks through the basic process of adding a car, on hardcoded
def test():
    while True:
        try:

            # this goes through  the flow of adding a vehicle
            gvt.get_to_vehicle_page()
            gvt.select_vehicles_unlisted()
            gvt.select_specific_body_style_unlisted(1)           # doesnt always run
            gvt.select_specific_new_costs(2)            # doesnt always run
            gvt.select_antilock_brakes(0)               # doesnt always run
            gvt.select_specific_antitheft_device_unlisted(0)     # doesnt always run
            gvt.select_ownership_unlisted(1)
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()

        except Exception as err:

            ErrorCount = ErrorCount + 1
            print("Exception thrown on module:\t" + str(gvt.CurrentModule))
            print(str(err))

# this function walks through the entire unlisted flow, adds all permutations of vehicles
# other elements are hardcoded for testing purposes
# this takes a long time to run
def Test_G01():
    try:

        year_op = 1
        while year_op < gvt.MaxYearIndex:
            make_op = 1
            while make_op < gvt.MaxMakeIndex:
                model_op = 1
                while model_op < gvt.MaxModelIndex:
                    gvt.get_to_vehicle_page()
                    gvt.select_specific_vehicle(year_op, make_op, model_op)
                    gvt.select_specific_body_style(1) # replace with test case
                    gvt.select_specific_new_costs(2)  # replace with test case
                    gvt.select_antilock_brakes(0)
                    gvt.select_specific_antitheft_device(2)
                    gvt.select_ownership(1)
                    gvt.go_next()
                    gvt.select_primary_use(2)
                    gvt.go_next()
                    gvt.select_annual_mileage(2)
                    gvt.go_next()
                    model_op = model_op + 1
                make_op = make_op + 1
            year_op = year_op + 1
            print(str(gvt.MaxYearIndex))

    except Exception as err:
        gvt.error_message(err)

# adding a vehicle from before the year 1981
def Test_G02():
    try:

        gvt.get_to_vehicle_page()
        gvt.add_vehicle_pre1981("1967", "Ferrari", "Enzo")
        gvt.select_specific_body_style(1)  # replace with test case
        gvt.select_specific_new_costs(2)  # replace with test case
        gvt.select_antilock_brakes(0)
        gvt.select_specific_antitheft_device(2)
        gvt.select_ownership(1)                    # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
        gvt.go_next()
        gvt.select_primary_use(2)
        gvt.go_next()
        gvt.select_annual_mileage(2)
        gvt.go_next()
    except Exception as err:
        gvt.error_message(err)

# adding a vehicle from before the year 1981 w/ invalid year
# this is a negative test case, it is supposed to fail
def Test_G03():
    try:

        gvt.get_to_vehicle_page()
        gvt.add_vehicle_pre1981("1981", "Ferrari", "Enzo")
        gvt.select_specific_body_style(1)  # replace with test case
        gvt.select_specific_new_costs(2)  # replace with test case
        gvt.select_antilock_brakes(0)
        gvt.select_specific_antitheft_device(2)
        gvt.select_ownership(1)                    # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
        gvt.go_next()
        gvt.select_primary_use(2)
        gvt.go_next()
        gvt.select_annual_mileage(2)
        gvt.go_next()
    except Exception as err:
        gvt.error_message(err)

# adding a vehicle with different body-styles
def Test_H01():
    try:
        bodystyle_op = 1
        while bodystyle_op < gvt.MaxBodyStyleIndex:
            gvt.get_to_vehicle_page()
            gvt.add_vehicle_pre1981("1967", "Ferrari", "Enzo") # this will always bring up the body styles menu
            gvt.select_specific_body_style(bodystyle_op)
            gvt.select_specific_new_costs(2)  # replace with test case
            gvt.select_antilock_brakes(0)
            gvt.select_specific_antitheft_device(2)
            gvt.select_ownership(1)  # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
            gvt.go_next()
            gvt.select_primary_use(2)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            bodystyle_op = bodystyle_op + 1
    except Exception as err:
        gvt.error_message(err)

# "special features" - anti-theft device
def Test_H02():
    try:
        atd_op = 1
        while atd_op < gvt.MaxAntitheftDeviceIndex:
            gvt.get_to_vehicle_page()
            gvt.add_vehicle_pre1981("1967", "Ferrari",
                                             "Enzo")  # this will always bring up the body styles menu
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(2)  # replace with test case
            gvt.select_antilock_brakes(0)
            gvt.select_specific_antitheft_device(atd_op)
            gvt.select_ownership_unlisted(
                1)  # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
            gvt.go_next()
            gvt.select_primary_use(2)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            atd_op = atd_op + 1
    except Exception as err:
        gvt.error_message(err)


# "special features" - anti-lock brakes - unlisted  31 - 1990, 13 - ferrari, 3 - OTHER
def Test_H03():
    try:
        alb_op = 0
        while alb_op < 2:
            gvt.get_to_vehicle_page()
            gvt.select_specific_vehicle(31, 13, 3) # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(2)  # replace with test case
            gvt.select_specific_antitheft_device(1)
            gvt.select_antilock_brakes(alb_op)
            gvt.select_ownership(
                1)
            gvt.go_next()
            gvt.select_primary_use(2)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            alb_op = alb_op + 1
    except Exception as err:
        gvt.error_message(err)

# "special features" - new cost - unlisted  31 - 1990, 13 - ferrari, 3 - OTHER
def Test_H04():
    try:
        newcost_op = 1
        while newcost_op < gvt.MaxNewCostIndex:
            gvt.get_to_vehicle_page()
            gvt.select_specific_vehicle(31, 13, 3) # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(newcost_op)  # replace with test case
            gvt.select_specific_antitheft_device(1)
            gvt.select_antilock_brakes(0)
            gvt.select_ownership(
                1)
            gvt.go_next()
            gvt.select_primary_use(2)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            newcost_op = newcost_op + 1
    except Exception as err:
        gvt.error_message(err)

# vehicle ownership - owned
# verify that the user can select the propery ownership category
# index guide
# 0 = owned, 1 = financed, 2 = leased
# This covers Test cases I01-I03, hence the naming I0n
def Test_I0n():
    try:
        ownshp_op = 0
        while ownshp_op < 3:
            gvt.get_to_vehicle_page()
            gvt.select_specific_vehicle(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(1)  # replace with test case
            gvt.select_specific_antitheft_device(1)
            gvt.select_antilock_brakes(0)
            gvt.select_ownership(
                ownshp_op)
            gvt.go_next()
            gvt.select_primary_use(2)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            ownshp_op = ownshp_op + 1
    except Exception as err:
        gvt.error_message(err)

#TODO RANDOMIZE THE USAGE FUNCTIONS - COMMUTE AND BUSINESS

# vehicle usage
# verify that the user can select the propery ownership category
# index guide
# 0 = commute, 1 = pleasure, 2 = business
# This covers Test cases J01-J03, hence the naming J0n. Yes it is close to Jon.
def Test_J0n():
    try:
        usage_op = 0
        while usage_op < 3:
            gvt.get_to_vehicle_page()
            gvt.select_specific_vehicle(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(1)  # replace with test case
            gvt.select_specific_antitheft_device(1)
            gvt.select_antilock_brakes(0)
            gvt.select_ownership(1)
            gvt.go_next()
            gvt.select_primary_use(usage_op)
            gvt.go_next()
            gvt.select_annual_mileage(2)
            gvt.go_next()
            usage_op = usage_op + 1

    except Exception as err:
        gvt.error_message(err)

def Test_K01():
    try:
        mileage_op = 0
        while mileage_op < gvt.MaxAnnualMilesIndex:
            gvt.get_to_vehicle_page()
            gvt.select_specific_vehicle(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style(1)
            gvt.select_specific_new_costs(1)  # replace with test case
            gvt.select_specific_antitheft_device(1)
            gvt.select_antilock_brakes(0)
            gvt.select_ownership(1)
            gvt.go_next()
            gvt.select_primary_use(1)
            gvt.go_next()
            gvt.select_annual_mileage(mileage_op)
            gvt.go_next()
            mileage_op = mileage_op + 1

    except Exception as err:
        gvt.error_message(err)

# this function walks through the entire unlisted flow, adds all permutations of vehicles
# other elements are hardcoded for testing purposes
# this takes a long time to run
def Test_G01_Unlisted():
    try:

        year_op = 1
        while year_op < gvt.MaxYearIndex:
            make_op = 1
            while make_op < gvt.MaxMakeIndex:
                model_op = 1
                while model_op < gvt.MaxModelIndex:
                    gvt.get_to_vehicle_page_unlisted()
                    gvt.select_specific_vehicle_unlisted(year_op, make_op, model_op)
                    gvt.select_specific_body_style_unlisted(1) # replace with test case
                    gvt.select_specific_new_costs_unlisted(2)  # replace with test case
                    gvt.select_antilock_brakes_unlisted(0)
                    gvt.select_specific_antitheft_device_unlisted(2)
                    gvt.select_ownership_unlisted(1)
                    gvt.go_next()
                    gvt.select_primary_use_unlisted(2)
                    gvt.go_next()
                    gvt.select_annual_mileage_unlisted(2)
                    gvt.go_next()
                    model_op = model_op + 1
                make_op = make_op + 1
            year_op = year_op + 1
            print(str(gvt.MaxYearIndex))

    except Exception as err:
        gvt.error_message(err)

# adding a vehicle from before the year 1981 - unlisted
def Test_G02_Unlisted():
    try:

        gvt.get_to_vehicle_page_unlisted()
        gvt.add_vehicle_pre1981_unlisted("1967", "Ferrari", "Enzo")
        gvt.select_specific_body_style_unlisted(1)  # replace with test case
        gvt.select_specific_new_costs_unlisted(2)  # replace with test case
        gvt.select_antilock_brakes_unlisted(0)
        gvt.select_specific_antitheft_device_unlisted(2)
        gvt.select_ownership_unlisted(1)                    # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
        gvt.go_next()
        gvt.select_primary_use_unlisted(2)
        gvt.go_next()
        gvt.select_annual_mileage_unlisted(2)
        gvt.go_next()
    except Exception as err:
        gvt.error_message(err)

# adding a vehicle from before the year 1981 w/ invalid year - unlisted
# this is a negative test case, it is supposed to fail
def Test_G03_Unlisted():
    try:

        gvt.get_to_vehicle_page_unlisted()
        gvt.add_vehicle_pre1981_unlisted("1981", "Ferrari", "Enzo")
        gvt.select_specific_body_style_unlisted(1)  # replace with test case?
        gvt.select_specific_new_costs_unlisted(2)  # replace with test case?
        gvt.select_antilock_brakes_unlisted(0)
        gvt.select_specific_antitheft_device_unlisted(2)
        gvt.select_ownership_unlisted(1)                    # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
        gvt.go_next()
        gvt.select_primary_use_unlisted(2)
        gvt.go_next()
        gvt.select_annual_mileage_unlisted(2)
        gvt.go_next()
    except Exception as err:
        gvt.error_message(err)

# adding a vehicle with different body-styles - unlisted
def Test_H01_Unlisted():
    try:
        bodystyle_op = 1
        while bodystyle_op < gvt.MaxBodyStyleIndex:
            gvt.get_to_vehicle_page_unlisted()
            gvt.add_vehicle_pre1981_unlisted("1967", "Ferrari", "Enzo") # this will always bring up the body styles menu
            gvt.select_specific_body_style_unlisted(bodystyle_op)
            gvt.select_specific_new_costs_unlisted(2)  # replace with test case
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_specific_antitheft_device_unlisted(2)
            gvt.select_ownership_unlisted(1)  # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            bodystyle_op = bodystyle_op + 1
    except Exception as err:
        gvt.error_message(err)

# "special features" - anti-theft device - unlisted
def Test_H02_Unlisted():
    try:
        atd_op = 1
        while atd_op < gvt.MaxAntitheftDeviceIndex:
            gvt.get_to_vehicle_page_unlisted()
            gvt.add_vehicle_pre1981_unlisted("1967", "Ferrari",
                                             "Enzo")  # this will always bring up the body styles menu
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(2)  # replace with test case
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_specific_antitheft_device_unlisted(atd_op)
            gvt.select_ownership_unlisted(
                1)  # as far as i know this doesnt appear with pre-1981, leaving it here just in case so nothing breaks.
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            atd_op = atd_op + 1
    except Exception as err:
        gvt.error_message(err)


# "special features" - anti-lock brakes - unlisted  31 - 1990, 13 - ferrari, 3 - OTHER
def Test_H03_Unlisted():
    try:
        alb_op = 0
        while alb_op < 2:
            gvt.get_to_vehicle_page_unlisted()
            gvt.select_specific_vehicle_unlisted(31, 13, 3) # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(2)  # replace with test case
            gvt.select_specific_antitheft_device_unlisted(1)
            gvt.select_antilock_brakes_unlisted(alb_op)
            gvt.select_ownership_unlisted(
                1)
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            alb_op = alb_op + 1
    except Exception as err:
        gvt.error_message(err)

# "special features" - new cost - unlisted  31 - 1990, 13 - ferrari, 3 - OTHER
def Test_H04_Unlisted():
    try:
        newcost_op = 1
        while newcost_op < gvt.MaxNewCostIndex:
            gvt.get_to_vehicle_page_unlisted()
            gvt.select_specific_vehicle_unlisted(31, 13, 3) # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(newcost_op)  # replace with test case
            gvt.select_specific_antitheft_device_unlisted(1)
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_ownership_unlisted(
                1)
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            newcost_op = newcost_op + 1
    except Exception as err:
        gvt.error_message(err)

# vehicle ownership - owned
# verify that the user can select the propery ownership category
# index guide
# 0 = owned, 1 = financed, 2 = leased
# This covers Test cases I01-I03, hence the naming I0n
def Test_I0n_Unlisted():
    try:
        ownshp_op = 0
        while ownshp_op < 3:
            gvt.get_to_vehicle_page_unlisted()
            gvt.select_specific_vehicle_unlisted(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(1)  # replace with test case
            gvt.select_specific_antitheft_device_unlisted(1)
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_ownership_unlisted(
                ownshp_op)
            gvt.go_next()
            gvt.select_primary_use_unlisted(2)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            ownshp_op = ownshp_op + 1
    except Exception as err:
        gvt.error_message(err)

# vehicle ownership - owned
# verify that the user can select the propery ownership category
# index guide
# 0 = commute, 1 = pleasure, 2 = business
# This covers Test cases J01-J03, hence the naming J0n. Yes it is close to Jon.
def Test_J0n_Unlisted():
    try:
        usage_op = 0
        while usage_op < 3:
            gvt.get_to_vehicle_page_unlisted()
            gvt.select_specific_vehicle_unlisted(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(1)  # replace with test case
            gvt.select_specific_antitheft_device_unlisted(1)
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_ownership_unlisted(1)
            gvt.go_next()
            gvt.select_primary_use_unlisted(usage_op)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(2)
            gvt.go_next()
            usage_op = usage_op + 1

    except Exception as err:
        gvt.error_message(err)

def Test_K01_Unlisted():
    try:
        mileage_op = 0
        while mileage_op < gvt.MaxAnnualMilesIndex:
            gvt.get_to_vehicle_page_unlisted()
            gvt.select_specific_vehicle_unlisted(31, 13, 3)  # 31 - 1990, 13 - ferrari, 3 - OTHER
            gvt.select_specific_body_style_unlisted(1)
            gvt.select_specific_new_costs_unlisted(1)  # replace with test case
            gvt.select_specific_antitheft_device_unlisted(1)
            gvt.select_antilock_brakes_unlisted(0)
            gvt.select_ownership_unlisted(1)
            gvt.go_next()
            gvt.select_primary_use_unlisted(1)
            gvt.go_next()
            gvt.select_annual_mileage_unlisted(mileage_op)
            gvt.go_next()
            mileage_op = mileage_op + 1

    except Exception as err:
        gvt.error_message(err)

### execute scripts here ###
Test_K01_Unlisted()