from Connections_Module import *
class Economey():
    """
    Attributes:
        AdjacencyGraph: Dict<household, Set<Connections>>
    Abstraction Function:
        AF(adjacencyGraph) = a community of households represented by adjacencyGraph.keys(). Each household i is connected to the households i !=j in adjacencyGraph[household].
    Rep Invariant:
        If Connection(HH_i, HH_J)  in adjacencyGraph[hhj], then the same Connection(HH_i, HH_j) in adjGraph[hhi]
    Protection from rep:

    """
    def __init__(self) -> None:
        self.adjacencyGraph: dict["Household": set["Connection"]] = {}
        

    def checkRep(self):
        # every connection is mutual
        connectionSet = set()
        for household in self.adjacencyGraph:
            for connection in self.adjacencyGraph[household]:
                connectionSet.add(connection)
        
        for connection in connectionSet:
            household1, household2 = connection.members
            if connection not in self.adjacencyGraph[household1]:
                assert False
            if connection not in self.adjacencyGraph[household2]:
                assert False



    def addHousehold(self, household: "household"):
        """
        @ Params: Household
        @ Returns: void
        Spec: add household to economy, raise error if economey is already in economey
        """
        if household in self.adjacencyGraph:
            raise KeyError

        self.adjacencyGraph[household] = set()
        


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
            household.sendMessages()

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
                
