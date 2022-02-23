import pygame
import sys
import time
from pygame.locals import *
from pygame import mixer
import random


print('\nWelcome to the game...\n\n')
fname = str(input('Please Enter your name  : '))

def cl_num():
    #155 305 455
    x = random.choice([155,305,455])
    return x

def cl():
    car_lane = cl_num()
    return car_lane


f = open('players.txt','a')
f.write(fname)
f.write("\n")
f.close()


pygame.init()

mixer.init()
mixer.music.load('Arjunar-Villu.mp3')
mixer.music.play()

pygame.display.set_caption('ROAD RANGE')

screen = pygame.display.set_mode((800,800))
bike   = pygame.image.load('bike.png')
road   = pygame.image.load('road.png')
crash  = pygame.image.load('crash.png')
car    = pygame.image.load('car1.png').convert_alpha()
car    = pygame.transform.scale(car,(170,150))

FPS = 50000
fpsClock = pygame.time.Clock()

Y_UP = 0

car_index_lane  = 0
bike_lane       = 0
bike_index_lane = 0
i = 0
x = 0
y = 0
car_y = -100
lane  = 1

car_lane = cl()
#print(car_lane)

font = pygame.font.SysFont('arial', 30)
label = font.render('Game over',True,(255,255,255) , (255,0,0))
score = 0

while True:
    screen.fill((255,255,255))
    i = i + 10
    
    screen.blit(road, (350  , 0 ))
    screen.blit(road, (200  , 0 ))
    screen.blit(road, (50   , 0 ))
    
    screen.blit(road, (50   , 400))
    screen.blit(road, (350  , 400))
    screen.blit(road, (200  , 400))

    pygame.display.update()         
           
    positionx = 225 + x
    positiony = 600 + y
    screen.blit(bike,( positionx ,positiony ) )   
    
    car_y = car_y + 10
    screen.blit(car, ( car_lane , car_y  ))
    
    if car_lane == 155 :
        car_index_lane = 0 
    
    elif car_lane == 305 :
        car_index_lane = 1
    
    else:
        car_index_lane = 2
        
            
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y - 150
                Y_UP += 1
                
                if Y_UP > 4:
                    screen.blit(label,(340,350))
                    pygame.display.update()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
                    
            
            if event.key == pygame.K_DOWN:
                y = y + 150
                
            
            if event.key == pygame.K_LEFT:
                x = x - 150
                #print(x + 255 ," left \n")
                lane = lane - 1
                
                if lane < 1:
                    screen.blit(label,(340,350))
                    pygame.display.update()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
                
            if event.key == pygame.K_RIGHT:
                x = x + 150
                #print(x + 255 ," right \n")
                lane = lane + 1
                
                if lane > 3:
                    screen.blit(label,(340,350))
                    pygame.display.update()
                    time.sleep(3)
                    pygame.quit()
                    sys.exit()
      
            #if goes below the bottom line
            if  y > 100 :  
                screen.blit(label,(340,350))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()  
                            
                
    #if car goes out of range new car should comes in ...
    if car_y > 750 : 
        car_y = -100
        car_lane = cl()
        screen.blit(car, (car_lane , car_y  ))
        score += 1
        i = 0

    bike_lane = 255 + x 

    if bike_lane == 255:
        bike_index_lane = 0
        
    elif bike_lane == 405:
        bike_index_lane = 1

    else:
        bike_index_lane = 2
        
    #if get crashed : break            
    if car_y == (600 + y)-100 and bike_index_lane == car_index_lane:
        screen.blit(crash,(bike_lane - 50 ,car_y + 100))
        pygame.display.update()    
        screen.blit(label,(340,350))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()    

    score_text = font.render('Score = '+str(score), True ,(0,0,0))
    screen.blit(score_text, (10,40))
    pygame.display.flip()                       
    pygame.display.update()
    fpsClock.tick(FPS)
    
    