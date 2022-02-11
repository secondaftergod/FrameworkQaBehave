Feature: Validate the login feature

  Background:
    Given Launch the browser
    When Open the "https://www.saucedemo.com/" website
    Then The login has been opened

  @valid_login
  Scenario: Login with valid credentials
    And Provide the username "standard_user" and password "secret_sauce"
    And Click on the Login button
    Then Login is successful and productpage is opened
    Then Close the browser

  Scenario Outline: Login with invalid username and password
    And Provide the username "<username>" and password "<password> "
    And Click on the Login button
    Then Login is failed with invlid username and password
    Then Close the browser
    Examples:
      | username | password |
      | abcd     | 1234     |
      | 35473    | afsdf    |

  Scenario: Login with empty username
    And Provide the password "secret_sauce"
    And Click on the Login button
    Then Login is failed and empty username error is displayed
    Then Close the browser

  Scenario: Login with empty password
    And Provide the username "standard_user"
    And Click on the Login button
    Then Login is failed and empty password error is displayed
    Then Close the browser