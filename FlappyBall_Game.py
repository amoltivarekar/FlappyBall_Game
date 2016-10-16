# FlappyBall_Game_IN_Python.py

import pygame
from random import randint
blue=(0, 19, 77)
yellow=(255, 255, 102)
white=(255,255,255)
lightblue=(179, 236, 255)

counter = 0
x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 482
xloc = 700
yloc = 0
xwidth=70
yheight=randint(0,350)
space = 150
obspeed = 2.5
score = 0

pygame.init()

def ball(x,y):
        pygame.draw.circle(screen, yellow, [x,y], 10)

def gameover():
        font = pygame.font.SysFont("Century Gothic",35)
        text = font.render(" Game Over  :( ",True,white)
        screen.blit(text,[210,230])

def obstacle(xloc, yloc, xwidth, yheight):
        pygame.draw.rect(screen, lightblue, [xloc, yloc, xwidth, yheight])
        pygame.draw.rect(screen, lightblue, [xloc, int(yloc+yheight+space), xwidth, 500])

def Score(score):
        font = pygame.font.SysFont("Century Gothic",30)
        text = font.render("Score : "+str(score),True,white)
        screen.blit(text,[10,10]) 
        
size=700,500
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Birds")

done=False
clock=pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done=True                
                if event.type  == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                y_speed = -5
                if event.type  == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                                y_speed = 5
                
        y += y_speed
        xloc -= obspeed
                         
        screen.fill(blue)
        obstacle(xloc, yloc, xwidth, yheight)
        ball(x,y)
        Score(score)

        if y > ground :
                gameover()
                y_speed = 0
                obspeed = 0

        if((x+20) > xloc) and ((y-20) < yheight) and ((x-15) < (xwidth+xloc)):
                gameover()
                obspeed = 0
                y_speed = 0

        if((x+20) > xloc) and ((y+20) > (yheight+space)) and ((x-15) < (xwidth+xloc)):
                gameover()
                obspeed = 0
                y_speed = 0
                
        if xloc < -80 :
                xloc = 700
                yheight = randint(0, 350)
        if x > xloc and x < xloc+3:
                score = score+10
                
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
