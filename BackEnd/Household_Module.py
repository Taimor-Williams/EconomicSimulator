import copy
from .Message_Module import *
class household(): 
    '''
    household class represents a household in an economey

    Abstraction Function:
        AF(endowment, consumption, id, currentWealth, mailBox, pos) = the household named id that consumes 
        consumption units and is given endowment units, that has wealth = to currentWealth and has a mailbox, 
        its pos in the world is a tuple (x,y)

    Rep invarient:
        endowment >= 0
        consumption >= 0

    Saftey from rep exposure:
        endowment and consumption can only be changed within the functions 
        SetEndowment and SetConsumption
        This protects any client from changing endowment or consumption to a negative value

    '''

    def __init__(self, endowment: int, consumption: int, id:str = "household0"):
        self.endowment: int = endowment
        self.consumption: int = consumption
        self.currentWealth: int = 0
        self.mailBox: set["Message"] = set([])
        self.id = id
        self.pos = (0,0)
        self.CheckRepInvarient()

    def CheckRepInvarient(self):
        assert self.endowment >= 0, "can't have negative endowment"
        assert self.consumption >= 0, "can't have negative consumption" 

    def sendMessages(self, connections: set["Connection"]):
        """
        @Param: connections: Set<Connections>
        @Returns: void
        Spec: if negative currentWealth, send message to all connections 
        """
        if self.currentWealth >= 0:
            return
    
        for connection in connections:
            other = connection.members - set([self])
            other = other.pop()
            newMessage = Message(-self.currentWealth, self, other)
            other.mailBox.add(newMessage)

    def respondMessages(self):
        """
        @ Param: void
        @ Returns:void
        Spec: decide who to send money to, The calc should be based on who 
        needs help the most, keep going till you help everyone or your currentWealth reaches 0. 
        
        implemtation: prob needs a recursive solution or a while loop
        """

        while self.currentWealth >0:
            if self.mailBox:
                curMessage = self.mailBox.pop()
                if self.currentWealth - curMessage.amount >= 0:
                    givenAmount = curMessage.amount
                else:
                    givenAmount = self.currentWealth
                theircurrentAmount = curMessage.origin.currentWealth
                curMessage.origin.SetCurrentWealth(theircurrentAmount + givenAmount)
                self.SetCurrentWealth(self.currentWealth- givenAmount)
            else:
                break

    def calcCurrentWealth(self):
        """
        @ params: void
        # returns: void
        spec: First, we calculate how much is added or subtracted to the current wealth by endowment minus consumption.
        """
        self.currentWealth += self.endowment-self.consumption
        self.CheckRepInvarient()
    
    def SetEndowment(self, value: int):
        """
        @ params: value
        # returns: void
        spec: sets endowment to value
        """
        self.endowment = value
        self.CheckRepInvarient()
    
    def SetConsumption(self, value: int):
        """
        @ params: value
        # returns: void
        sets consumption to value
        """
        self.consumption = value
        self.CheckRepInvarient()
    
    def SetCurrentWealth(self, value: int):
        """
        @ params: value
        # returns: void
        sets currentWealth to value
        """
        self.currentWealth = value
        self.CheckRepInvarient()
    
    def getEndowment(self):
        return self.endowment
    
    def getConsumption(self):
        return self.consumption
    
    def getCurrentWealth(self):
        return self.currentWealth
    
    def getMailBox(self):
        return copy.deepcopy(self.mailBox)
    
    # equality operations:  =, >, >=, <, <=
    def __hash__(self):
        # print(hash(str(self)))
        return hash(str(self))
    
    def __eq__(self, other):
        """
        value equality
        """
        return self.endowment == other.endowment & self.consumption == other.consumption
    
    def __lt__(self, other):
        """
        value equality
        """
        pass


