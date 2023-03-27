import pytest
from Main import *

#######################################
# testsuite for household
########################################
"""
Testing Strategy
checkRep():
    partiton on endowment: -, +
    partiton on consumption: -, +

sendMessages():
    partition on connections.size: 0, 1, >1

openMessages():
    partition on mailbox.size: 0,1, >1

calcCurrentWealth():
    special cases

setEndowment():
    value: -, +

setConsumption():
    value: -,+
"""
def test_checkRep_endowment_negative():
    with pytest.raises(AssertionError):
        TestHousehold1 = household(-1,1)

def test_checkRep_endowment_positive():
    TestHousehold1 = household(1,1)
    assert TestHousehold1.getEnodwment() == 1

def test_checkRep_consumption_negative():
    with pytest.raises(AssertionError):
        TestHousehold1 = household(1,-1)

def test_checkRep_consumption_positive():
    TestHousehold1 = household(1,1)
    assert TestHousehold1.getEnodwment() == 1

def test_SetEndowment_positive():
    TestHousehold = household(2,2)
    TestHousehold.SetEndowment(1)
    assert 1 == TestHousehold.getEnodwment(), "set endowment"

def test_SetEndowment_negative():
    TestHousehold = household(2,2)
    with pytest.raises(AssertionError):
        TestHousehold.SetEndowment(-1)

def test_SetConsumption_positive():
    TestHousehold = household(2,2)
    TestHousehold.SetConsumption(1)
    assert TestHousehold.getConsumption() == 1, "consumpiton wrong value"

def test_SetConsumption_negative():
    TestHousehold = household(2,2)
    with pytest.raises(AssertionError):
        TestHousehold.SetConsumption(-1)


def test_sendMessage_0():
    """
    don't know what i should assert here
    """
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(household)
    TestHousehold.SetCurrentWealth = -1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    assert TestHousehold.mailBox.size == 0

def test_sendMessage_1():
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(TestHousehold)
    TestHousehold1 = household(2,2)
    TestEconomey.addHousehold(TestHousehold1)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold1)
    TestHousehold.SetCurrentWealth = -1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    assert TestHousehold1.mailBox.size == 1

def test_sendMessage_2():
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(TestHousehold)
    TestHousehold1 = household(2,2)
    TestEconomey.addHousehold(TestHousehold1)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold1)
    TestHousehold2 = household(2,2)
    TestEconomey.addHousehold(TestHousehold2)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold2)
    TestHousehold.SetCurrentWealth = -1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    assert TestHousehold1.mailBox.size == 1 & TestHousehold2.mailBox.size == 1
# OpenMessages

def test_openMessage_0():
    """
    don't know what i should assert here
    """
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(household)
    TestHousehold.SetCurrentWealth = -1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    assert TestHousehold.mailBox.size == 0

def test_openMessage_1():
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(TestHousehold)
    TestHousehold1 = household(2,2)
    TestHousehold1.SetCurrentWealth(2)
    TestEconomey.addHousehold(TestHousehold1)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold1)
    TestHousehold.SetCurrentWealth = -1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    TestHousehold1.openMessages()

    assert TestHousehold.getCurrentWealth == 0

def test_sendMessage_2():
    TestEconomey = Economey()
    TestHousehold = household(2,2)
    TestEconomey.addHousehold(TestHousehold)
    TestHousehold1 = household(2,2)
    TestEconomey.addHousehold(TestHousehold1)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold1)
    TestHousehold2 = household(2,2)
    TestEconomey.addHousehold(TestHousehold2)
    TestEconomey.connectHouseholds(TestHousehold, TestHousehold2)
    TestHousehold.SetCurrentWealth = -2
    TestHousehold1.SetCurrentWealth = 1
    TestHousehold2.SetCurrentWealth = 1
    TestHousehold.sendMessages(TestEconomey.adjacencyGraph(TestHousehold))
    assert TestHousehold.getCurrentWealth() == 0

#######################################
# testsuite for Economey
########################################
"""
Testing Strategy
checkRep():
    MutualConnection yes, no

AddHouselhold():
    HouseholdAlreadyExistInEconomey yes, no
    
ConnectHousehold():
    HouseholdsAlreadyConnected yes,no

SendMessages():
    householdsInEconomey 0, 1, >1

OpenMessages():
    householdsInEconomey 0, 1, >1

CleanUp():
    householdsInEconomey 0, 1, >1
    household.currentWealth <0, >=0
"""

def test_Economey_checkRep_0():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse, TestHouse1)
    assert TestEconomey.checkRep()

def test_Economey_checkRep_1():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse, TestHouse1)
    TestEconomey.adjacencyGraph[TestHouse1] = set()
    with pytest.raises(AssertionError):
        TestEconomey.checkRep()


def test_Economey_addHousehould_0():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    with pytest.raises(AssertionError):
        TestEconomey.addHousehold(TestHouse)

def test_Economey_addHousehould_1():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    assert TestHouse in TestEconomey.adjacencyGraph

def test_Economey_ConnectHousehold_0():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse, TestHouse1)
    with pytest.raises(AssertionError):
        TestEconomey.connectHouseholds(TestHouse, TestHouse1)

def test_Economey_ConnectHousehold_1():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse, TestHouse1)
    assert TestEconomey[TestHouse1] == TestEconomey[TestHouse], "both have same connection"

def test_sendMessages_0():
    TestEconomey = Economey()
    TestEconomey.send()
    assert TestEconomey.adjacencyGraph == {}

def test_sendMessages_1():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestHouse.SetCurrentWealth(-1)
    TestEconomey.send()
    assert TestHouse1.mailBox.size == 1

def test_sendMessages_2():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestHouse2 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.addHousehold(TestHouse2)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse2)
    TestEconomey.connectHouseholds(TestHouse1,TestHouse2)
    TestHouse.SetCurrentWealth(-1)
    TestEconomey.send()
    assert TestHouse1.mailBox.size == 1 & TestHouse2.mailBox.size == 1

# open msgs

def test_respondMessages_0():
    TestEconomey = Economey()
    TestEconomey.send()
    TestEconomey.respond()
    assert TestEconomey.adjacencyGraph == {}

def test_respondMessages_1():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestHouse.SetCurrentWealth(-1)
    TestEconomey.send()
    TestEconomey.respond()
    assert TestHouse1.mailBox.size == 1

def test_respondMessages_2():
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestHouse2 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.addHousehold(TestHouse2)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse2)
    TestEconomey.connectHouseholds(TestHouse1,TestHouse2)
    TestHouse.SetCurrentWealth(-1)
    TestEconomey.send()
    assert TestHouse1.mailBox.size == 1 & TestHouse2.mailBox.size == 1

# maybe need to revisit this test suite

def test_cleanUp_0():
    """
    2 households in economey that are connected
    both have >= 0 currentWealth
    cleanup should do nothing
    """
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.cleanUp()
    assert TestEconomey.adjacencyGraph.keys().size == 2
    assert TestEconomey.adjacencyGraph[TestHouse1] == TestEconomey.adjacencyGraph[TestHouse]

def test_cleanUp_1():
    """
    2 households in economey that are connected
    1 has negative currentWealth
    cleanup should remove that household from economeyy and break the connections
    """
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestHouse.SetCurrentWealth(-1)
    TestEconomey.cleanUp()
    assert TestEconomey.adjacencyGraph.keys().size == 1
    assert TestEconomey.adjacencyGraph[TestHouse1] == set()

def test_cleanUp_2():
    """
    2 households in economey that are connected
    2 has negative currentWealth
    cleanup should remove all housegholds from economey
    """
    TestEconomey = Economey()
    TestHouse = household(2,2)
    TestHouse1 = household(2,2)
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestHouse.SetCurrentWealth(-1)
    TestHouse1.SetCurrentWealth(-1)
    TestEconomey.cleanUp()
    assert TestEconomey.adjacencyGraph == set()








    