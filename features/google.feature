Feature: Googling stuff

Scenario: Search NS
  Given I go to "http://www.google.com/"
  When I search "Narrative Science"
  Then the results should contain "Narrative Science | Natural Language Generation Technology"



