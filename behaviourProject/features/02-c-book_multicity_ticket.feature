Feature: Booking a MultiCity Ticket
    Scenario: MultiCity ticket details should be filled with relevant information  and booked
        Given I launch Chrome browser
        When I open rahulshettyacademy dropdowns practise homepage
        And I choose flighttype as "MultiCity"
        And Accept Prompt
        And I Enter FROM as "Colombo (CMB)"
        And I Enter TO as "Dubai, All Airports(DWC) (DXB)"
#        And I Enter DEPART DATE as "17/09"
#        And I Choose PASSENGERS as 2 Adults
#        And I Choose CURRENCY as "INR"
#        And I Enter FROM_2 as "Colombo (CMB)"
#        And I Enter TO_2 as "Colombo (CMB)"
        And I Enter DEPART DATE 2 as "17/09"
#        And I Enter FROM_3 as "Colombo (CMB)"
#        And I Enter TO_3 as "Colombo (CMB)"
        And I Enter DEPART DATE 3 as "17/09"
        And I Click Search
        Then I close browser