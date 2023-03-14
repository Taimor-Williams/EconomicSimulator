
class household(): 
    '''
    household class represents a household in an economey

    Abstraction Function:
        AF(endowment, consumption) = household in an economey with no connections

    Rep invarient:
        endowment >= 0
        consumption >= 0

    Saftey from rep exposure:
        endowment and consumption can only be changed within the functions 
        SetEndowment and SetConsumption
        This protects any client from changing endowment or consumption to a negative value


    '''

    def __init__(self, endowment: int, consumption: int):
        self.endowment = endowment
        self.consumption = consumption
        self.currentWealth = 0
        self.connectedHouseholds = set()

    def CheckRepInvarient(self):
        assert(self.endowment >= 0, "")
        assert(self.consumption >= 0, "")

    def AddConnected(self,newHousehold):
        """
        Adds the connected households. 
        @parameters: newHousehold cannot be in connected already.
        """
        assert(not newHousehold in self.connectedHouseholds,"newHousehold already in connected.")
        self.CheckRepInvarient()
        self.connectedHouseholds.add(newHousehold)

    def DeleteConnected(self,oldHousehold):
        """
        Deletes the connected households.
        @parameters: oldHousehold must be in list already.
        """
        assert(oldHousehold in self.connectedHouseholds,"newHousehold not in connected.")
        self.CheckRepInvarient()
        self.connectedHouseholds.remove(oldHousehold)

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
        self.CheckRepInvarient()
                
    def EndTurn():
        """
        If CurrentWealth <0: delete from economey and all households its connected to
        """
        pass

    def BeginTurn(self):
        """
        First, we calculate how much is added or subtracted to the current wealth by endowment minus consumption.
        """
        self.currentWealth += self.endowment-self.consumption
        self.CheckRepInvarient()
    
    def SetEndowment(self, value: int):
        """
        sets endowment to value
        """
        self.endowment = value
        self.CheckRepInvarient()
    
    def SetConsumption(self, value: int):
        """
        sets consumption to value
        """
        self.consumption = value
        self.CheckRepInvarient()
    
    def SetCurrentWealth(self, value: int):
        """
        sets currentWealth to value
        """
        self.currentWealth = value
        self.CheckRepInvarient()





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
    economey = economey - householdsToBeDeleted
    print(economey)
    return economey

    




if __name__ == "__main__":
    TestHousehold1 = household(2,3)
    TestHousehold2 = household(3,2)
    TestHousehold3 = household (1,2)
    TestHousehold3.SetCurrentWealth(2)
    TestHousehold2.AddConnected(TestHousehold1)
    TestHousehold1.AddConnected(TestHousehold2)
    economey = {TestHousehold1,TestHousehold2,TestHousehold3}
    
    while True:
        LoopBeginTurn(economey)
        print(TestHousehold1.currentWealth)
        print(TestHousehold2.currentWealth)
        print(TestHousehold3.currentWealth)
        LoopAskForHelp(economey)
        print(TestHousehold1.currentWealth)
        print(TestHousehold2.currentWealth)
        print(TestHousehold3.currentWealth)
        economey = LoopDeleteHouseholds(economey)
        query = input("Next turn?")
        if not input:
            break
            
