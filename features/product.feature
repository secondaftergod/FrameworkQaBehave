Feature: Validate the products list

  Background:
    Given Launch the browser
    When Open the "https://www.saucedemo.com/" website and login whith username "{user}" and password "{pwd}
    Then Product list has been opened


  Scenario: Add items to basked and check
    And Add items to card
    Then Check items in basket
    Then Close the browser