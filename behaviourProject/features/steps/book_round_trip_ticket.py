from behave import *


@when('I choose flighttype as "Round Trip"')
def pickRadioButton(context):
    # context.driver.get.find_element_by_id("ctl00_mainContent_rbtnl_Trip_1").click()
    # context.driver.get.find_element_by_xpath("//input[@id='ctl00_mainContent_rbtnl_Trip_1']").click()
    context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_rbtnl_Trip_1']").click()

@when('I Enter RETURN DATE as "{input}"')
def chooseReturnDate(context, input):
    context.driver.find_element_by_xpath()