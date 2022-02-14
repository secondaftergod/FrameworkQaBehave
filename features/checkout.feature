Feature: Validate the products list

  Background:
    Given Launch the browsers
    When Open the "https://www.saucedemo.com/" website and login whith username "standard_user" and password "secret_sauce"
    Then Click on the Login button
    Then The product page open
    Then Add items to card
    Then Click on buy button
    Then Click on the checkout button

  Scenario: Check buy page title
    Then Check title checkout page

  Scenario: Checkout with valid info
    And Provide the firstname "<firstname>" and lastname "<lastname> and zip "<zip>"
    And Click on the continue button
    Then Error checkout
    Then Close the browser
  Scenario Outline: Checkout with invalid info
    And Provide the firstname "<firstname>" and lastname "<lastname> and zip "<zip>"
    And Click on the continue button
    Then Error checkout
    Then Close the browser
    Examples:
      | firstname | lastname | zip |
      |           |1         |1    |
      |1          |          |1    |
      |1          |1         |     |


