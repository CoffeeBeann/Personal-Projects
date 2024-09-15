import pygame
import time
import random
pygame.init()

#Window Setup
display_width = 800
display_height = 600

# Color Definition (R G B)
black = (0,0,0) 
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((display_width,display_height)) # Sets Display
pygame.display.set_caption('Race Game') # Changes Window Title
clock = pygame.time.Clock() # Frame Rate
carImg = pygame.image.load('Car.png')
global dodged
dodged = 0

def dodged_things(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))
    
car_width = 73
car_height = 73

def things(thing_x, thing_y, thing_w, thing_h, thing_c): # x1,y1,width,height,color
    pygame.draw.rect(gameDisplay, thing_c,[thing_x,thing_y,thing_w,thing_h]) # (Weere TO Display, Color, [Coordinates])
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText) # Retruns Text Surface And a Rectangle to Encase Text
    TextRect.center = ((display_width/2),(display_height/2)) # Centers Text
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    game_loop()

    
def crash():
    message_display('Game Over') # Displays This Message
    global dodged
    dodged = 0

def game_loop():
    global dodged
    dodged = 0
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0

    # Ostacle
    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    
    
    gameExit = False
    while not gameExit: # Sets Game Logic Loop
        for event in pygame.event.get(): # Gets Any Event That Happens (Left Click, Right Click, etc)
            
            if event.type == pygame.QUIT: # If User Exits Window, Program Terminates Automatically
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN: # Signals A Key Was Pressed
                if event.key == pygame.K_LEFT: # Left Arrow Key
                    x_change = -15
                    
                elif event.key == pygame.K_RIGHT: # Right Arrow Key
                    x_change = 15

                
            if event.type == pygame.KEYUP: # Nothing is Currently Being Pressed
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
                    
        x += x_change
        
        
        gameDisplay.fill(white) # Makes Background White

       # thing_x, thing_y, thing_w, thing_h, thing_c
        things(thing_start_x,thing_start_y,thing_width,thing_height,black)

       # Moves Obstacle
        thing_start_y += thing_speed

        
        car(x,y)
        dodged_things(dodged)


        if x > display_width - car_width or x < 0:
            x_change = 0

        elif thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1

            

        #Collision Detection
        elif y < thing_start_y + thing_height:
            if x > thing_start_x and x < thing_start_x + thing_width or x + car_width > thing_start_x and x + car_width < thing_start_x + thing_width:
                crash()

    
        pygame.display.update()
        clock.tick(60) # FPS : 60 FPS
        
game_loop()
pygame.quit() # Un-Initializes Pygame
quit()
    





