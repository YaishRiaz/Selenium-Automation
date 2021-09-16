from behave import *
from selenium.webdriver.support.select import Select


@when('I Click Holiday Package')
def chooseHolidayPackageOpt(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'Holiday Packages')]").click()

@when('I Enter Destination as "Dubai"')
def enterDestinationCity(context):
    select = Select(context.driver.find_element_by_id('ctl00_mainContent_HolidayPackages_DropDownListPackage'))
    select.select_by_visible_text('Dubai')
    # context.driver.find_element_by_id("ctl00_mainContent_HolidayPackages_DropDownListPackage_CTXT").send_keys(input)


@when('I Enter Departure as "Mumbai"')
def enterDepartureCity(context):
    select = Select(context.driver.find_element_by_id('ctl00_mainContent_HolidayPackages_DropDownListFrom'))
    select.select_by_visible_text('Mumbai')
    # context.driver.find_element_by_id("ctl00_mainContent_HolidayPackages_DropDownListFrom_CTXT").send_keys(input)


@when('I Enter Return as "{input}"')
def enterReturnCity(context, input):
    context.driver.find_element_by_id("ctl00_mainContent_HolidayPackages_DropDownListTo_CTXT").send_keys(input)
