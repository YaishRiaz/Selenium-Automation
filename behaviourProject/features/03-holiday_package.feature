Feature: Searching for Holiday Packages
    Scenario: Holiday Details should be filled with relevant information and Searched
        Given I launch Chrome browser
        When I open rahulshettyacademy dropdowns practise homepage
        And I Click Holiday Package
        And I Enter Destination as "Dubai"
        And I Enter Departure as "Mumbai"
#        And I Enter Return as "Delhi"
#        And I Enter Depart Date as "28-09-2021"
#        And I Click Search
        Then I close browser
