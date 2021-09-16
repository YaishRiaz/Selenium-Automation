Feature: Booking a One Way Ticket

    Scenario: One way ticket details should be filled with relevant information and booked
        Given I launch Chrome browser
        When I open rahulshettyacademy dropdowns practise homepage
        And I choose flighttype as "One Way"
        And I Enter FROM as "Colombo (CMB)"
        And I Enter TO as "Dubai, All Airports(DWC) (DXB)"
        And I Enter DEPART DATE as "17-09-2021"
#        And I Choose PASSENGERS as 2 Adults
#        And I Choose CURRENCY as "INR"
        And I Click Search
        Then I close browser