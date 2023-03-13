import pytest
from Main import *

# test for household

def test_SetEndowment():
    TestHousehold = household(2,2)
    TestHousehold.SetEndowment(1)
    assert(1 == TestHousehold.endowment, "set endowment")

def test_SetConsumption():
    TestHousehold = household(2,2)
    TestHousehold.SetConsumption(1)
    assert(1 == TestHousehold.consumption, "set consumption")

def test_SetCurrentWealth():
    TestHousehold = household(2,2)
    TestHousehold.SetCurrentWealth(1)
    assert(1 == TestHousehold.currentWealth, "set currentWealth")

def test_BeginTurn():
    TestHousehold = household(2,2)
    TestHousehold.BeginTurn()
    expected = 0
    result = TestHousehold.currentWealth
    assert(expected==result,"currentWealth is wrong.")

def test_AddConnected():
    TestHousehold1 = household(3,4)
    TestHousehold2 = household(5,3)
    TestHousehold1.AddConnected(TestHousehold2)
    expected = True
    result = TestHousehold2 in TestHousehold1.connectedHouseholds
    assert(result == expected, "first household present in 2nd")

def test_DeleteConnected():
    TestHousehold1 = household(3,4)
    TestHousehold2 = household(5,3)
    TestHousehold1.AddConnected(TestHousehold2)
    TestHousehold1.DeleteConnected(TestHousehold2)
    expected = False
    result = TestHousehold2 in TestHousehold1.connectedHouseholds
    assert(result == expected, "first household not present in")

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
     
# testing strategy
## Partition on number of households connected to 0,>0
def test_EndTurn_0():
    TestHousehold1 = household(3,4)
    economy = {TestHousehold1}
    TestHousehold1.SetCurrentWealth(-1)
    TestHousehold1.EndTurn()
    assert(economy.size == 0, "no household should be in the economey")

def test_EndTurn_1():
    TestHousehold1 = household(3,4)
    TestHousehold2 = household(3,4)
    TestHousehold1.AddConnected(TestHousehold2)
    economy = {TestHousehold1, TestHousehold2}
    TestHousehold2.SetCurrentWealth(-1)
    TestHousehold2.EndTurn()
    assert(economy.size == 1, "household 2 no longer in the economey")
    assert(TestHousehold2 not in TestHousehold1.connectedHouseholds, "household 2 no longer connected to anyone")

    

# test for functions