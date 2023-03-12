
class household(): 
    '''
    household class represents a household in an economey
    '''

    def __init__(self, endowment: int, consumption: int):
        self.endowment = endowment
        self.consumption = consumption
        self.currentWealth = 0
        self.connectedHouseholds = []
    def AddConnected(self,newHousehold):
        """
        Adds the connected households. 
        @parameters: newHousehold cannot be in connected already.
        """
        assert(not newHousehold in self.connectedHouseholds,"newHousehold already in connected.")
        self.connectedHouseholds.append(newHousehold)
    def DeleteConnected(self,oldHousehold):
        """
        Deletes the connected households.
        @parameters: oldHousehold must be in list already.
        """
        assert(oldHousehold in self.connectedHouseholds,"newHousehold not in connected.")
        self.connectedHouseholds.delete(oldHousehold)
    def AskForHelp(self):
        """
        Ask neighbors for wealth if negative current wealth.
        In the future, might be different strategies for how/what to ask.
        """
        for neighbor in self.connectedHouseholds:
            if neighbor.currentWealth>0:
                neighbor.currentWealth-=1
                self.currentWealth+=1
            if self.currentWealth==0:
                break
                
    def EndTurn():
        """
        Get rid of households with negative current wealth.
        """
        pass
    def BeginTurn(self):
        """
        First, we calculate how much is added or subtracted to the current wealth by endowment minus consumption.
        """
        self.currentWealth = self.endowment-self.consumption




def LoopBeginTurn(economy:set):
    """
    Begin turn for all households in the economey
    """
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


if __name__ == "__main__":
    TestHousehold1 = household(2,3)
    TestHousehold2 = household(3,2)
    TestHousehold3 = household (2,2)
    TestHousehold2.AddConnected(TestHousehold1)
    TestHousehold1.AddConnected(TestHousehold2)
    economy = {TestHousehold1,TestHousehold2,TestHousehold3}
    
    while True:
        LoopBeginTurn(economy)
        print(TestHousehold1.currentWealth)
        print(TestHousehold2.currentWealth)
        print(TestHousehold3.currentWealth)
        LoopAskForHelp(economy)
        print(TestHousehold1.currentWealth)
        print(TestHousehold2.currentWealth)
        print(TestHousehold3.currentWealth)
        query = input("Next turn?")
        if not input:
            break
            
