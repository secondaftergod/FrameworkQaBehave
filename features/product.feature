Feature: Validate the products list

  Background:
    Given Launch the browsers
    When Open the "https://www.saucedemo.com/" website and login whith username "standard_user" and password "secret_sauce"
    Then Click on the Login button
    Then The product page open

  Scenario: Add items to basked and check
    And Add items to card
    Then Check items in basket after Add
    Then Close the browser

  Scenario: Remove items from basked and check
    And Add items to card
    Then Check items in basket after Add
    Then Remove items
    Then Check items in basket after Remove
    Then Close the browser