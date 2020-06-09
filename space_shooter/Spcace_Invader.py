import time
import os
import pygame
import random

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

BG=pygame.image.load(os.path.join("images","background.png"))

def main():
	run=True
	FPS=60
	clock=pygame.time.Clock()
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
main()


