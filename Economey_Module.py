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
        pass

    def checkRep():
        pass

    def addHousehold():
        """
        @ Params: Household
        @ Returns: void
        Spec: add household to economy, raise error if economey is already in economey
        """
        pass
    def connectHouseholds(household0, household1):
        """
        @ Params: (household1, household2)
        @ Returns: void
        Spec: create connection between 2 different households in the economy 
        add them to the adjacency graph values
        """
        pass

    def calcWealth():
        """
        @ Params: void
        @ Returns: void
        Spec: all households cal wealth
        """
        pass

    def send():
        """
        @ Params: void
        @ Returns: void
        Spec: all households with -CurrentWealth send msgs to households they are connected to 
        """
        pass

    def respond():
        """
        @ Params: void
        @ Returns: void
        Spec: households with msgs decide if they want to respond or not

        """
        pass

    def cleanUp():
        """
        @ Params: void
        @ Returns: void
        Spec: households with negative currentWEalth a
        """
        pass