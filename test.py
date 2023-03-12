import pytest
import Main

# test for household

def test_EndTurn():
    pass

def test_BeginTurn():
    TestHousehold = household(2,2)
    TestHousehold.BeginTurn()
    expected = 0
    result = TestHousehold.currentWealth
    assert(expected==result,"currentWealth is wrong.")

def test_AskForHelp():
    TestHousehold1 = household(3,4)
    TestHousehold2 = household(5,3)
    TestHousehold1.AddConnected(TestHousehold2)
    TestHousehold2.AddConnected(TestHousehold1)
    TestHousehold1.BeginTurn()
    TestHousehold2.BeginTurn()
    TestHousehold1.AskForHelp()
    expected = 0
    result = TestHousehold1.currentWealth
    assert(expected == result,"First household not updated correctly.")
    expected1 = 1
    result1 = TestHousehold2.currentWealth
    assert(expected1==result1,"Second household not updated correctly.")
     


# test for functions