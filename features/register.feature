Feature: Test the functionality of the Register Page

    Background: Open Register Page
      Given I am on the Register Page

  @register_page
  Scenario: Check that success message is displayed when the user registers with a new email
    When I select the male radio button
    When I set first name as "Ion"
    When I set last name as "Pop"
    When I select day "1"
    When I select month "January"
    When I select year "1990"
    When I set a new email
    When I set company name as "IT Factory"
    When I click the newsletter checkbox
    When I set password as "123456"
    When I set confirm password as "123456"
    When I click register button
    Then Success message is displayed

    # pentru a rula doar raportul aceste folosete comanda :
    # behave --tags=register_page