#khai bao thu vien
import pygame
import math
from datetime import datetime

def getTime():
    now = datetime.now()
    timeString = str(now).split()[1]
    return timeString.split(".")[0].split(":")

def drawLine(inTime : int, color: tuple ,lengthLine: int = 200, width : int = 10):
    x = 300 + lengthLine * math.sin(6 * inTime * math.pi / 180)
    y = 300 - lengthLine * math.cos(6 * inTime * math.pi / 180)
    pygame.draw.line(screen , color , (300, 300) , (x , y) , width)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600,600)) # Create display

    # Picture
    image = pygame.image.load('additionalFolder\Clock.png') # Clock

    pygame.display.set_caption("Clock") # Set title
    pygame.display.set_icon(pygame.image.load("additionalFolder\IconClock.ico")) # Set icon

    #color
    red = (225, 74, 74)
    orange = (255, 146, 81)
    blue = (185, 255, 248)
    lightOrange = (253, 238, 220)

    running = True
    # Clock Run
    while running:
        h,m,s = map(int,getTime())
        screen.fill(lightOrange)
        screen.blit(image, (50, 50))
        drawLine(s, red , 200, 2)
        drawLine(m, blue , 170 , 4)
        drawLine(h*5 + m//12, orange , 120, 6)

        #Exit Clock
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        
        pygame.display.flip()
    pygame.quit()	