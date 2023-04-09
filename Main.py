import os
import pygame
from BackEnd.Connections_Module import *
from BackEnd.Household_Module import *
from BackEnd.Economey_Module import *
import time
from FrontEnd.Button_Module import *


# setup constants

pygame.init()
red = (200,0,0)
blue = (0,0,255)

circleX = 100
circleY = 100
radius = 10

TestEconomey = Economey((400,600))

WINDOW_HEIGHT = TestEconomey.size[1]
WINDOW_WIDTH = TestEconomey.size[0]*2
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Economey Demo')

#load button images
start_img = pygame.image.load(os.path.join('FrontEnd','Next.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('FrontEnd','Info.png')).convert_alpha()

#create button instances
start_button = Button(TestEconomey.size[0]*1.5, TestEconomey.size[1]*1/4, start_img, 0.2)
exit_button = Button(TestEconomey.size[0]*1.5, TestEconomey.size[1]*2/4, exit_img, 0.2)
add_button =  Button(TestEconomey.size[0]*1.5, TestEconomey.size[1]*3/4, exit_img, 0.2)

# game speed
clock = pygame.time.Clock()

def weather(Economey):
    """
    @params: Economey
    @Returns: 
    @specs: applies a weather effect to the economey. Like a monsoon. In which case all households 
    inside circle centered at (x,y) with radius z suffer some combination of effect such as. 
    1) endowment is set to 0 for x turns. 
    2) currentWealth is reduced sharply 
    3) consumption becomes much higher for x turns, etc

    would require me to create a new class called conditions which effect households and leave after 
    a certain amount of time
    """
    pass

def guiAddHousehold(economey: Economey):
    """
    spec: add household to current economey, name randomly generted can be placed anywhere 
    on the board that doesn't violate economey specs. 
    """
    validPos = True
    newPos = pygame.mouse.get_pos()

    # position inside economey
    if newPos[0] < 0 or newPos[0] > economey.size[0]:
         validPos = False
    
    if newPos[1] < 0 or newPos[1] > economey.size[1]:
         validPos = False

    # position not to close
    for pos in economey.positions:
        if Economey.calcPosDistance(newPos, pos) < 2*economey.radius:
            validPos = False
    
    # place
    if validPos:
        print("hellow")
        print(newPos)
        newHouse = household(2,2)
        newHouse.pos = newPos
        economey.addHousehold(newHouse)



def guiAddConnnection():
    """
    spec: add connection between 2 households to the current economey
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
    # print(arrayMembers[0].pos, arrayMembers[1].pos)

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

def DisplayHouseholdInfo(nextHousehold: household, window):
    """
    displays information about the household 
    """
    # print(nextHousehold.currentWealth)
    position = nextHousehold.pos
    text_size = 15
    offset = 10
    font = pygame.font.SysFont('arial', text_size)
    text = font.render("Wealth: "+str(nextHousehold.getCurrentWealth()), True, red)
    window.blit(text, (position[0],position[1]+offset))
    text = font.render("Endowment: "+str(nextHousehold.getEndowment()), True, red)
    window.blit(text, (position[0],position[1]+text_size+offset))
    text = font.render("Consumption: "+str(nextHousehold.getConsumption()), True, red)
    window.blit(text, (position[0],position[1]+text_size*2+offset))
    text = font.render("ID: "+str(nextHousehold.id), True, red)
    window.blit(text, (position[0],position[1]+text_size*3+offset))

if __name__ == "__main__":

    # TestEconomey = Economey((400,300))    
    # window = pygame.display.set_mode(TestEconomey.size)
    
    TestHouse = household(2,3, "RothsChild")
    TestHouse1 = household(2,3, "Monroy")
    TestHouse2 = household(3,2, "Tesla")
    TestEconomey.addHousehold(TestHouse)
    TestEconomey.addHousehold(TestHouse1)
    TestEconomey.addHousehold(TestHouse2)
    TestEconomey.connectHouseholds(TestHouse,TestHouse1)
    TestEconomey.connectHouseholds(TestHouse,TestHouse2)
    TestEconomey.connectHouseholds(TestHouse1,TestHouse2)
    TestHouse2.SetCurrentWealth(6)



    add = False
    display = False
    active = True
    while active:
        clock.tick(30)
        # draw loop 
        window.fill((0,0,0))
        pygame.draw.line(window, blue, (TestEconomey.size[0]*1.1,0), (TestEconomey.size[0]*1.1,TestEconomey.size[1]))
        start_button.draw(window)
        exit_button.draw(window)
        add_button.draw(window)
        for nextHousehold in TestEconomey.adjacencyGraph:
            drawHousehold(nextHousehold,window,TestEconomey.radius)
            if display:
                DisplayHouseholdInfo(nextHousehold,window)
        for nextConnection in TestEconomey.connections:
            drawConnection(nextConnection, window)
        
        pygame.display.update()

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if add:
                    guiAddHousehold(TestEconomey)
                    add = not add
                if start_button.isClicked():
                    nextTurn()
                if exit_button.isClicked():
                    display = not display
                if add_button.isClicked():
                    add = True
                
                        

        



        
