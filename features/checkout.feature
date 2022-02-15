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
    And Provide the firstname "1" and lastname "1" and zip "1"
    And Click on the continue button
    Then Check overview page
    Then Close the browser
  Scenario Outline: Checkout with invalid info
    And Provide the firstname "<first>" and lastname "<last>" and zip "<zip>"
    And Click on the continue button
    Then Error checkout
    Then Close the browser
    Examples:
      | first | last | zip |
      |NULL   |1     |1    |
      |1      |NULL  |1    |
      |1      |1     |NULL |


