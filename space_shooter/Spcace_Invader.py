import time
import os
import pygame
import random

pygame.font.init()
WIDTH,HEIGHT=680,580
WIN=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("SPACE INVADER")
RED_SPACE_SHIP=pygame.image.load(os.path.join("images","red_ship.png"))
GREEN_SPACE_SHIP=pygame.image.load(os.path.join("images","green_ship.png"))
BLUE_SPACE_SHIP=pygame.image.load(os.path.join("images","blue_ship.png"))
YELLOW_SPACE_SHIP=pygame.image.load(os.path.join("images","yellow_ship.png"))

RED_LASER=pygame.image.load(os.path.join("images","red_laser.png"))
GREEN_LASER=pygame.image.load(os.path.join("images","green_laser.png"))
BLUE_LASER=pygame.image.load(os.path.join("images","blue_laser.png"))
YELLOw_LASER=pygame.image.load(os.path.join("images","yellow_laser.png"))

BG=pygame.transform.scale(pygame.image.load(os.path.join("images","background.png")),(WIDTH,HEIGHT))

class Ship:
	def __init__(self,x,y,health=100):
		self.x,self.y,self.health=x,y,health
		self.ship_image=None
		self.laser_image=None
		self.lasers=[]
		self.cool_down_counter=[]
	def draw_ship(self,window):
		pygame.draw.rect(window,(255,0,0),(self.x,self.y,50,50),0)

def main():
	run=True
	FPS=60
	level=1
	live=5
	moving_speed=5
	clock=pygame.time.Clock()
	main_font=pygame.font.SysFont("comicsans",50)
	ship=Ship(50,500)
	def redraw_window():
		WIN.blit(BG,(0,0))
		lable_lives=main_font.render(f"Lives:{live}",1,(255,255,255))
		lable_level=main_font.render(f"Level:{level}",1,(255,255,255))	
		
		WIN.blit(lable_lives,(10,10))
		WIN.blit(lable_level,(WIDTH-lable_level.get_width()-10,10))
		ship.draw_ship(WIN)
		pygame.display.update()
		
	while run:
		clock.tick(FPS)
		redraw_window()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
		keys=pygame.key.get_pressed()
		if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ship.x+moving_speed>: 
			ship.x-=moving_speed
		if (keys[pygame.K_d]or keys[pygame.K_RIGHT]) and ship.x+moving_speed<WIDTH:
			ship.x+=moving_speed
		if (keys[pygame.K_w]or keys[pygame.K_UP]) and ship.y-moving_speed>0:
			print(ship.y)
			ship.y-=moving_speed
		if (keys[pygame.K_s]or keys[pygame.K_DOWN]) and ship.y+moving_speed<HEIGHT:
			ship.y+=moving_speed
main()


