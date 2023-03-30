import pygame
from Main import *

red = (200,0,0)
blue = (0,0,255)

circleX = 100
circleY = 100
radius = 10

    
def genPosition(self, curPositions: set, minDistance: int, boardDimensions: tuple[int,int])-> tuple[int,int]:
        """
        logic for adding new pos that are at least 2* raidus distance apart from others positions
        should return a tuple(x,y) coordinate
        1)   can obviously just make a grid an only allow for intersection points on grid like go
            but want a better solution
        
        2)   should also probably be a generator
        """

def drawConnection(connection: Connection, window):
    """
    @params:    connection, 
    @params:    window, pygame window
    @returns:   void
    specs:  draws a linesegment inside the pygame window, the linesegment had endpoints that 
            are the postions of the households in connection.members
    
    """

    arrayMembers = list(connection.members)
    print(arrayMembers[0].pos, arrayMembers[1].pos)

    pygame.draw.line(window, blue, arrayMembers[0].pos, arrayMembers[1].pos)

def drawHousehold(household: household, window, raidus):
    """
    @params:    household, houselhod we are drawing
    @params:    window, pygame window
    @returns:   void
    specs:  draws a circle inside the pygame window, the circle has center at household pos and
            radius of global radius variable
    """
    
    pygame.draw.circle(window,red,household.pos,radius) 


class node():
   """
   node on the board
   """
   def __init__(self, pos, color = red, radius = 10) -> None:
        self.pos = pos
        self.color = color
        self.radius = radius


TestEconomey = Economey()    
window = pygame.display.set_mode(TestEconomey.size)
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

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    for nextHousehold in TestEconomey.adjacencyGraph:
        drawHousehold(nextHousehold,window,TestEconomey.radius)
    
    for nextConnection in TestEconomey.connections:
        drawConnection(nextConnection, window)
    
    pygame.display.update()