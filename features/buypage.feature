Feature: Check buy list

  Background:
    Given Launch the browsers
    When Open the "https://www.saucedemo.com/" website and login whith username "standard_user" and password "secret_sauce"
    Then Click on the Login button
    Then The product page open
    Then Add items to card
    Then Click on buy button

  Scenario: Check buy page title and buy items
    And Check title
    Then Check items inside buy page

  Scenario: Remove items from buyPage
    Then Remove all items from buyPage


