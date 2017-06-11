# file:features/sampletest.feature

Feature: Sample tests for behave

  Scenario: running a sample positive test
     Given we have a string "Hello world"
     when we get a string
     then both should be equal

  Scenario: running a sample positive test with two values
     Given we have two strings value1 value2
     when we get the strings
     then strings that we have and got are equal