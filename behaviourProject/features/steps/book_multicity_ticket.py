from behave import *

@when('I choose flighttype as "MultiCity"')
def pickRadioButton(context):
    context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_rbtnl_Trip_2']").click()


@when('Accept Prompt')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Accept Prompt')


@when('I Enter FROM_2 as "{input}"')
def step_impl(context, input):
    raise NotImplementedError(u'STEP: When I Enter FROM_2 as "input"')


@when('I Enter TO_2 as "{input}"')
def step_impl(context, input):
    raise NotImplementedError(u'STEP: When I Enter TO_2 as "input"')

@when('I Enter DEPART DATE 2 as "{input}"')
def chooseDepartDate(context, input):
    raise NotImplementedError(u'STEP: When I Enter TO_3 as "input"')


@when('I Enter FROM_3 as "{input}"')
def step_impl(context, input):
    raise NotImplementedError(u'STEP: When I Enter FROM_3 as "input"')


@when('I Enter TO_3 as "{input}"')
def step_impl(context, input):
    raise NotImplementedError(u'STEP: When I Enter TO_3 as "input"')

@when('I Enter DEPART DATE 3 as "{input}"')
def chooseDepartDate(context, input):
    raise NotImplementedError(u'STEP: When I Enter TO_3 as "input"')