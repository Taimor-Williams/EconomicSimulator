import os
import pygame
from BackEnd.Connections_Module import *
from BackEnd.Household_Module import *
from BackEnd.Economey_Module import *
import time
from FrontEnd.Button_Module import *


# setup constants
red = (200,0,0)
blue = (0,0,255)

circleX = 100
circleY = 100
radius = 10

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load(os.path.join('FrontEnd','start_btn.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('FrontEnd','exit_btn.png')).convert_alpha()

#create button instances
start_button = Button(500, 200, start_img, 0.8)
exit_button = Button(500, 400, exit_img, 0.8)

# game speed
clock = pygame.time.Clock()


    
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

def nextTurn():
    """
    specs: handles the backend logic for what a new turn should look like
    """
    #Econ loop
    TestEconomey.calcWealth()
    TestEconomey.send()
    TestEconomey.respond()
    TestEconomey.cleanUp()



if __name__ == "__main__":

    TestEconomey = Economey((400,500))    
    # window = pygame.display.set_mode(TestEconomey.size)
    TestEconomey = Economey()
    TestHouse = household(2,3, "RothsChild")
    TestHouse1 = household(2,4, "Monroy")
    TestHouse2 = household(2,2, "Tesla")
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.addHousehold(TestHouse2)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse2)
    TestEconomey.connectHouseholds(TestHouse1,TestHouse2)
    TestHouse2.SetCurrentWealth(6)





    active = True
    while active:
        # draw loop 
        window.fill((0,0,0))
        start_button.draw(window)
        exit_button.draw(window)
        for nextHousehold in TestEconomey.adjacencyGraph:
            drawHousehold(nextHousehold,window,TestEconomey.radius)
        
        for nextConnection in TestEconomey.connections:
            drawConnection(nextConnection, window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isClicked():
                    nextTurn()
                if exit_button.isClicked():
                    print('EXIT')

        pygame.display.update()



        
