import pygame,sys,random,os
import time
from pygame.locals import *
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE	  = (  0, 0,   255)
HEAD=0
BGCOLOR = BLACK
window_width,window_height=800,600
CELLSIZE=20
cell_width=40
cell_height=30
os.environ['SDL_VIDEO_WINDOW_POS']="50,50"
pygame.init()
Display=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("SNAKE")
def score(a):
	print(a)
	FontObj=pygame.font.Font('freesansbold.ttf',32)
	text=FontObj.render("Score:"+str(a),True,GREEN)
	textrect=text.get_rect()
	textrect.center=(300,30)
	Display.blit(text,textrect)
	pygame.display.update()
def speed():
	global FPS
	FontObj=pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceSlow = FontObj.render('S for Slow', True, GREEN, BLUE)
	textSurfaceNormal = FontObj.render('N for Normal', True, GREEN, BLUE)
	textSurfaceFast = FontObj.render('F for Fast', True, GREEN, BLUE)
	textRectSlow = textSurfaceSlow.get_rect()
	textRectSlow.center = (200, 150)
	textRectNormal = textSurfaceNormal.get_rect()
	textRectNormal.center = (200, 200)
	textRectFast = textSurfaceFast.get_rect()
	textRectFast.center = (200, 250)

	while True:
		#Display.fill(WHITE)
		Display.blit(textSurfaceSlow,textRectSlow)
		Display.blit(textSurfaceNormal,textRectNormal)
		Display.blit(textSurfaceFast,textRectFast)
						
		pygame.display.update()
		for event in pygame.event.get():
			if event.type==KEYDOWN:		
				if event.key==K_s:
					FPS=10
					return
				elif event.key==K_n:
					FPS=15
					return
				elif event.key==K_f:
					FPS=30
					return
			if event.type==QUIT:
				terminate()

	
	
def terminate():
    pygame.quit()
    sys.exit()

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(Display, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE -8, CELLSIZE -8)
        pygame.draw.rect(Display, RED, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(Display, RED, appleRect)

def getRandomLocation():
    return {'x': random.randint(0, cell_width - 1), 'y': random.randint(0, cell_height - 1)}
def Draw_Screen():
	for h in range(0,window_height,20):
		pygame.draw.line(Display,RED,(0,h),(window_width,h),2)
	for v in range(0,window_width,20):
		pygame.draw.line(Display,BLUE,(v,0),(v,window_height),2)
def pause():
	while True:
		for event in pygame.event.get():
			if event.type==KEYDOWN:		
				if event.key==13:
					return
			if event.type==QUIT:
				terminate()
def runGame():
    # Set a random start point.
    a=0
    startx = random.randint(5, cell_width - 6)
    starty = random.randint(5, cell_height - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    # Start the apple in a random place.
    apple = getRandomLocation()

    FPSCLOCK=pygame.time.Clock()
    
    while True: # main game loop
       # time.sleep(.1)
        
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
                elif event.key ==13:
                    pause()

        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == cell_width or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == cell_height:
         print("quit",wormCoords[HEAD]['x'])           
         return # game over
        c=1
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                print(c)
                return # game over
            c+=1
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
            a=a+1
            #print("Apple=",apple);time.sleep(3)
        else:
            #score(a)
            del wormCoords[-1] # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead),print(wormCoords)
        Display.fill(BGCOLOR)
        score(a)
        #Draw_Screen()
        drawWorm(wormCoords)
        drawApple(apple)
        #score(a)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        pygame.quit()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key

    
while True:
	speed()
	runGame()
	for event in pygame.event.get():
		time.sleep(1)
		print(event)		
		if event.type==QUIT:
			pygame.quit()
	pygame.display.update()
