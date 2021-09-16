# from behave import *
# from selenium import webdriver
#
# @given('I launch Chrome browser')
# def launchBrowser(context):
#     context.driver=webdriver.Chrome(r"C:\Users\yarilk\Downloads\Driver Folder\chromedriver_win32\chromedriver.exe")
#     #context.driver=webdriver.Chrome()
#
# @when('I open rahulshettyacademy dropdowns practise homepage')
# def openHomePage(context):
#     context.driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
#
# @then('I verify that the flights drop down has picture present on page')
# def verifyPicture(context):
#     status=context.driver.find_element_by_xpath("//div[@class='slider has-touch']//div[1]//img[1]").is_displayed()
#     assert status is True
#
# @then('I close browser')
# def closeBrowser(context):
#     context.driver.close()