class Connection:
    """
    Attributes:
        Strength: int
        Type: str
        Members: Set<Households>
    Abstraction function:
        AF(strength, type, members)-> the relationship between households in members where the strength of the connection is represented by strength and the type of relationship is type
    Rep Invariant:
        Members should have two different households
        Strength should be >0
    Protection from rep:
        strength is accessed and changed using the methods

    """
    def __init__(self, strength: int, type: str, members: set["household"]) -> None:
        self.strength = strength
        self.type = type
        self.members = members
    
    def checkRep(self):
        assert self.strength > 0, ""

    def getStrength(self)-> int:
        """
        params: void
        returns: strength: int
        spec: 
        """
        return self.strength

    def setStrength(self, strength: int):
        """
        params: strength: int
        returns: void
        spec: 
        """
        self.strength = strength
        self.checkRep()

