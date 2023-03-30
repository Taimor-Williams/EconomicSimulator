from Connections_Module import *
import math
from random import randint
class Economey():
    """
    Attributes:
        adjacencyGraph: Dict<household, Set<Connections>>
        connections: set<connection>
        positions: set<tuples<int,int>>>
        size: int
        radius: int

    Abstraction Function:
        AF(adjacencyGraph, connections, size, radius) = a community of households represented by adjacencyGraph.keys(). 
        Each household i is connected to the households i !=j in adjacencyGraph[household]. Connections
        is the set of all unique connections bewteen households within the economey. 

        size is a tuple representing the 2-D board the households and connections of the economey 
        are displayed/exist in. Radius is the size of the displayed households in the economey

        positions is a set of tuples representing the positions of all households in the economey

        
    Rep Invariant:
        If Connection(HH_i, HH_J)  in adjacencyGraph[hhj], then the same Connection(HH_i, HH_j) in adjGraph[hhi]
        all connections in connection are in adjacencyGraph[household]

        size must be idk
        raidus must be > 0
        all positions must be inside of the ecomoomey and >= 2*radius apart
        

    Protection from rep:
        connections mutated through add connection
        adjacencyGraph is mutated through add household, and add connection

    """
    def __init__(self, size:tuple[int,int] = (500,500), radius:int = 10,) -> None:
        self.adjacencyGraph: dict["Household": set["Connection"]] = {}
        self.connections: set["connection"] = set()
        self.size = size
        self.radius = radius
        self.positions: set[tuple[int,int]] = set()
        

    def checkRep(self):
        # every connection is mutual
        for connection in self.connections:
            household1, household2 = connection.members
            if connection not in self.adjacencyGraph[household1]:
                raise AssertionError
            if connection not in self.adjacencyGraph[household2]:
                raise AssertionError
        
        # attribute checks size and radius
        assert self.radius > 0



    def addHousehold(self, household: "household"):
        """
        @ Params: Household
        @ Returns: void
        Spec: add household to economy, raise error if economey is already in economey
        """
        if household in self.adjacencyGraph:
            raise KeyError

        self.adjacencyGraph[household] = set()

        household.pos = self.genPosition()
        self.positions.add(household.pos)
        


    def connectHouseholds(self, household0, household1):
        """
        @ Params: (household1, household2)
        @ Returns: void
        Spec: create connection between 2 different households in the economy 
        add them to the adjacency graph values

        raises keyerror if both households not in the economey or refer to same household
        raises valueError if connection already exist
        """

        if household0 is household1:
            raise KeyError
        
        if household1 not in self.adjacencyGraph or household0 not in self.adjacencyGraph:
            raise KeyError
        

        # connection does not already exist
        for connection in self.adjacencyGraph[household0]:
            if household1 in connection.members:
                raise ValueError
        
        for connection in self.adjacencyGraph[household1]:
            if household0 in connection.members:
                raise ValueError
        

        newConnection = Connection(1, "type", set([household0,household1]))

        self.adjacencyGraph[household0].add(newConnection)
        self.adjacencyGraph[household1].add(newConnection)
        self.connections.add(newConnection)
        


    def calcWealth(self):
        """
        @ Params: void
        @ Returns: void
        Spec: all households cal wealth
        """
        for household in self.adjacencyGraph:
            household.calcCurrentWealth()

    def send(self):
        """
        @ Params: void
        @ Returns: void
        Spec: all households with -CurrentWealth send msgs to households they are connected to 
        """
        for household in self.adjacencyGraph:
            household.sendMessages(self.adjacencyGraph[household])

    def respond(self):
        """
        @ Params: void
        @ Returns: void
        Spec: households with msgs decide if they want to respond or not

        """
        for household in self.adjacencyGraph:
            household.respondMessages()

    def cleanUp(self):
        """
        @ Params: void
        @ Returns: void
        Spec: households with negative currentWEalth a
        """
        removeHouseholdSet = set()

        # removes households
        for household in self.adjacencyGraph:
            if household.getCurrentWealth() < 0:
                removeHouseholdSet.add(household)

        for key in removeHouseholdSet:
            del self.adjacencyGraph[key]
        # remove connections in economey to households that were deleted
        # we create a new set of the safe nondeleated connections and 
        # set self.adjacencyGraph[household] = safeSet
        for household in self.adjacencyGraph:
            safeSet = set()
            for i,connection in enumerate(self.adjacencyGraph[household]):
                if not removeHouseholdSet.intersection(connection.members):
                    safeSet.add(connection)

                if i == len(self.adjacencyGraph[household])-1:
                    self.adjacencyGraph[household] = safeSet
                    break

        # change connections
        self.connections = self.connections - removeHouseholdSet

        # change positions
        removePostitionsSet = set()
        for household in removeHouseholdSet:
            removePostitionsSet.add(household.pos)      
        self.positions = self.positions -removePostitionsSet
    
    def genPosition(self)-> tuple[int,int]:

        """
        @params: void
        @returns: a new position that is within the economey and at least 
        raidus distance away from all other positions
        spec:  logic for adding new pos that are at least 2* raidus distance apart from others positions
        """

        validPos = False
        while not validPos:
            validPos = True
            newPos = (randint(0, self.size[0]), randint(0, self.size[0]))
            for pos in self.positions:
                if Economey.calcPosDistance(newPos, pos) < 2*self.radius:
                    validPos = False
        
        return newPos
                    



    def calcHouseholdDistance(household0: "household", household1: "household") -> int:
        x1 = household0.pos[0]
        x2 = household1.pos[0]
        y1 = household0.pos[0]
        y2 = household1.pos[0]
        distance = math.ceil(((x1-x2)**2+(y1-y2)**2)**0.5)
        return distance

    def calcPosDistance(pos0: tuple[int,int], pos1: tuple[int,int]) -> int:
        x1 = pos0[0]
        x2 = pos1[0]
        y1 = pos0[1]
        y2 = pos1[1]
        distance = math.ceil(((x1-x2)**2+(y1-y2)**2)**0.5)
        print((x1-x2)**2)
        print((y1-y2)**2)
        return distance

                
