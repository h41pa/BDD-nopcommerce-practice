Feature: Test the functionality of the Login Page
  Background: Open Login Page
    Given I am on the Login Page
    @T1
  # Scenariu 1 fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to login with an unregistered email
    When I insert an unregistered email in the mail input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "No customer account found" message
    @T3 @T1
   # Scenariu 1 cu parametru
   Scenario: Check that "No customer account found" message is displayed when the user tries to login with an unregistered email
     When I insert "email_neinregistrat@host.com" in the mail input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "No customer account found" message
   @T2 @T1
  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    When I insert " " in the email input
    When I click on the login button
    Then Email error message is displayed
    Then Email error text contains "Please enter your email"

  Scenario: Check that the login page URL is correct
    Then The login page URL is "https://demo.nopcommerce.com/login"


    # # folosim sintaxa backgroud pentru a rula Given I am on the Login Page , pentru toate scenarile
    # tagurile @ , putem rula teste cu tag - comanda
    # behave --tags=T1 -f html -o raport.html
