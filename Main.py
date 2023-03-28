from Connections_Module import *
from Household_Module import *
from Economey_Module import *
from Message_Module import *


def LoopBeginTurn(economy:set):
    """
    Begin turn for all households in the economey
    """
    print("economey: ", economy)
    for household in economy:
        household.BeginTurn()

def LoopAskForHelp(economy:set):
    """
    Ask households if they want to ask for help
    Check if the currentWealth meets some criteria to ask for help.
    """
    for household in economy:
        if household.currentWealth<0:
            household.AskForHelp()

def LoopEndTurn():
    """
    Ends the turn
    Tells households the turn is over
    """
    pass

def LoopDeleteHouseholds(economey: set):
    """
    Removes households from the economey
    Removes households from other households connecthousehold
    @parama economey: set of households
    """

    # get households to be deleted
    householdsToBeDeleted = set()

    for household in economey:
        if household.currentWealth < 0:
            householdsToBeDeleted.add(household)
    
    # remove those households from household.connectedHouseholds
    for household in economey:
        if household not in householdsToBeDeleted:
            for neighbor in household.connectedHouseholds:
                if neighbor in householdsToBeDeleted:
                    household.connectedHouseholds.remove(neighbor)

    # remove thos households from economey
    print("deleted: ", householdsToBeDeleted)
    print(economey - householdsToBeDeleted)

    # assignment operater 
    # economey = economey - householdsToBeDeleted

    # mutator operator
    #-=, #difference_update
    economey -= householdsToBeDeleted
    




    # ref equality with is
    
    




if __name__ == "__main__":
    # TestHousehold1 = household(2,3)
    # TestHousehold2 = household(3,2)
    # TestHousehold3 = household (1,2)
    # TestHousehold3.SetCurrentWealth(2)
    # TestHousehold2.AddConnected(TestHousehold1)
    # TestHousehold1.AddConnected(TestHousehold2)
    # economey = {TestHousehold1,TestHousehold2,TestHousehold3}
    
    # while True:
    #     LoopBeginTurn(economey)
    #     for Household in economey:
    #         print(Household.currentWealth)
    #     LoopAskForHelp(economey)
    #     for Household in economey:
    #         print(Household.currentWealth)
    #     LoopDeleteHouseholds(economey)
    #     query = input("Next turn?")
    #     if not input:
    #         break]

    TestEconomey = Economey()
    TestHouse = household(2,2, "RothsChild")
    TestHouse1 = household(2,2, "Monroy")
    TestHouse2 = household(2,2, "Tesla")
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.addHousehold(TestHouse2)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse2)
    TestEconomey.connectHouseholds(TestHouse1,TestHouse2)
    TestHouse.SetCurrentWealth(-2)
    TestHouse1.SetCurrentWealth(1)
    TestHouse2.SetCurrentWealth(1)
    TestEconomey.send()
    TestEconomey.respond()
    print(TestHouse.getCurrentWealth()) 
    print(TestHouse1.getCurrentWealth()) 
    print(TestHouse2.getCurrentWealth())

            
