Feature: Fill Country Text Field
    Scenario: Fill in country text field of rahulshettyacademy with "SriLanka"
        Given I launch Chrome browser
        When I open rahulshettyacademy dropdowns practise homepage
        And I Enter countryname as "SriLanka"
        Then I close browser
