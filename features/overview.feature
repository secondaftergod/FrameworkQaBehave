Feature: Validate the products list

  Background:
    Given Launch the browsers
    When Open the "https://www.saucedemo.com/" website and login whith username "standard_user" and password "secret_sauce"
    Then Click on the Login button
    Then The product page open
    Then Add items to card
    Then Click on buy button
    Then Click on the checkout button
    Then Provide the firstname "1" and lastname "1" and zip "1"
    Then Click on the continue button

  Scenario: Check buy page title
    Then Check overview page

  Scenario: Check price on order
    Then Check price item and total price
  Scenario:Check Eq total price
    Then Check eq prices


