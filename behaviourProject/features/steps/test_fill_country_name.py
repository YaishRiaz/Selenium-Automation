from behave import *
from selenium import webdriver

from config.config import Config

class FillCountrySteps:
    @given('I launch Chrome browser')
    def launchBrowser(context):
        context.driver=webdriver.Chrome(r"C:\Users\yarilk\Downloads\Driver Folder\chromedriver_win32\chromedriver.exe")
        #context.driver=webdriver.Chrome()

    @when('I open rahulshettyacademy dropdowns practise homepage')
    def openHomePage(context):
        context.driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

    @when('I Enter countryname as "{countryname}"')
    def enterCountryName(context,countryname):
        # WebDriverWait(context.driver, 10).until(ExpectedConditions.presence_of_element_located("autosuggest")).send_keys(input)
        context.driver.find_element_by_id("autosuggest").send_keys(countryname)

    @then('I close browser')
    def closeBrowser(context):
        context.driver.close()