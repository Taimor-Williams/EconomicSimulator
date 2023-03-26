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

    """
    def __init__(self) -> None:
        pass

    def getStrength()-> int:
        """
        params: void
        returns: strength: int
        spec: 
        """
        pass

    def setStrength(strength: int):
        """
        params: strength: int
        returns: void
        spec: 
        """
        pass

