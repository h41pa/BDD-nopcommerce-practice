Feature: Test the functionality of add and remove buttons
  Background: Add/Remove Elements
    Given I am on the Add/Remove Elements

  @removeradd
  Scenario: Check that Add/Remove Elements buttons works
    When I Add Element
    When I Remove Element
