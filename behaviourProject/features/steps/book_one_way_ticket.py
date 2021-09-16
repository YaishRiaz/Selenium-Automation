from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@when('I choose flighttype as "One Way"')
def chooseRdBtnToOneWay(context):
    context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_rbtnl_Trip_0']").click()


@when('I Enter FROM as "{input}"')
def enterFromCity(context, input):
    context.driver.find_element_by_id("ctl00_mainContent_ddl_originStation1_CTXT").send_keys(input)
    # selectFrom = Select(context.driver.find_element_by_id('ctl00_mainContent_ddl_originStation1_CTXTaction'))
    # selectFrom.select_by_visible_text("Colombo (CMB)")
    # selectFrom.select_by_value("CMB")

@when('I Enter TO as "{input}"')
def enterToCity(context, input):
    context.driver.find_element_by_id("ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys(input)


@when('I Enter DEPART DATE as "{input}"')
def chooseDepartDate(context, input):
    # context.driver.find_element_by_xpath("//body/form[@id='aspnetForm']/div[@class='maincontainer']/div[@id='wrapper']/div[@id='mainContents']/div[@id='new-homepage']/div[@id='home_banner']/div[@class='home_flight_search']/div[@id='content-change']/div[@class='book']/div[@id='flightSearchContainer']/div[@class='picker-first2']/button[1]").click()
    # context.driver.find_element_by_xpath("//a[contains(text(),'17')]").click()
    # context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_txt_Fromdate']").setAttribute("11-05-2019")
    # context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_txt_Fromdate']").send_keys(input)
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='10-05-2019']"))).send_keys(input)


@when('I Choose PASSENGERS as 2 Adults')
def choosePassengers(context):
    context.driver.find_element_by_xpath("//div[@id='divpaxinfo']").click()
    context.driver.find_element_by_xpath("//span[@id='hrefIncAdt']").click()
    context.driver.find_element_by_xpath("//input[@id='btnclosepaxoption']").click()



@when('I Choose CURRENCY as "INR"')
def chooseCurrency(context):
    context.driver.find_element_by_xpath("//select[@id='ctl00_mainContent_DropDownListCurrency']").click()
    context.driver.find_element_by_id("ctl00_mainContent_DropDownListCurrency").click()


@when('I Click Search')
def searchDetails(context):
    context.driver.find_element_by_xpath("//input[@id='ctl00_mainContent_btn_FindFlights']").click()