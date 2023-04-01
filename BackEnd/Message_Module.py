class Message:
    """
    Attributes:
        Amount: int
        Origin: Household
        Destination: Household
    Abstraction Function:
        AF(amount, origin, destination)-> the amount, negative for a request, and positive for a gift, to be sent between the origin and destination
    Rep Invariant:
        True
    Protection from rep:
        No methods to change anything
    """
    def __init__(self, amount: int, origin: "household", destination: "household") -> None:
        self.amount = amount
        self.origin = origin
        self.destination = destination
