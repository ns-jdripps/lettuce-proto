Feature: Google

Scenario: Visit Google
  Given I go to "http://www.google.com/"
  The title of the page should become "Google"
