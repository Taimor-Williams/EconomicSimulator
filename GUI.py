import pygame
from Main import *

red = (200,0,0)
blue = (0,0,255)

circleX = 100
circleY = 100
radius = 10

def genPosition(curPositions: set, minDistance: int, boardDimensions: tuple[int,int]):
    """
    logic for adding new pos that are a certain distance apart from others
    should return a tuple(x,y) coordinate
    1)   can obviously just make a grid an only allow for intersection points on grid like go
        but want a better solution
    
    2)   should also probably be a generator
    """
    pass



class node():
   """
   node on the board
   """
   def __init__(self, pos, color = red, radius = 10) -> None:
        self.pos = pos
        self.color = color
        self.radius = radius
        
window = pygame.display.set_mode((500,500))

household1 = node((0,100))
household2 = node((100,100))
active = True


while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False


    pygame.draw.circle(window,household1.color,household1.pos,household1.radius) # DRAW CIRCLE
    pygame.draw.circle(window,household2.color,household2.pos,household2.radius) # DRAW CIRCLE
    pygame.draw.line(window, blue, household1.pos, household2.pos)
    pygame.display.update()