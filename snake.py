import pygame
import random
from pygame import mixer
pygame.init()

#var
height=500
width=1000

# not refresh so for that time
fps=60
yellow=(255,255,50)
black=(0,0,0)
pink=(204,0,102)
white=(255,255,255)
red = (255,0,0)


#Background Music
mixer.music.load('backgroundmusic.mp3')
mixer.music.play(-3)

# icon
pygame.display.set_caption("S_N_A_K_E_~~~")
icon=pygame.image.load("snake2.png")
pygame.display.set_icon(icon)

playerImg=pygame.image.load("bggg.jpg")
playerX = 370
playerY = 480
playerX_change=0
playerY_change=0


window=pygame.display.set_mode((width,height)) # display screen but for sec so now work for its stay
clock=pygame.time.Clock()

def game(win,color,snak_list,sn_size,sn_sz):
    for snake_x,snake_y in snak_list:
        pygame.draw.rect(win,color,[snake_x,snake_y,sn_size,sn_sz])

font =  pygame.font.SysFont(None,45) #45 fontsize
def message(text,color,x,y): #x y exis position on screen
    screen=font.render(text,True,color)
    window.blit(screen,[x,y])
def snake():

    #snake
    snake_x=random.randint(5,900)
    snake_y=random.randint(5,400)
    sn_size=10
    sn_sz=5  # size of dot
    snak_list=[]
    sn_length=1
    score=0
    # snake velocity
    snvelo_x=0
    sn_velo_y=0
    speed=2

    #Food
    food_x = random.randint(200, 700)
    food_y = random.randint(100, 400)

# game var

    exit= False
    game_over = False

    ##pause the screen
    #  main
    while not exit:

        if game_over == True:
            window.fill(red)
            message("YOU DIED ",black,400,250) #message fun
            message("Replay enter ", black, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True

                if event.type==pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        snake()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit=True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        snvelo_x=0
                        sn_velo_y=-speed
                    if event.key == pygame.K_DOWN:
                        snvelo_x = 0
                        sn_velo_y = speed

                    if event.key == pygame.K_RIGHT:
                        snvelo_x = speed
                        sn_velo_y = 0
                    if event.key == pygame.K_LEFT:
                        snvelo_x = -speed
                        sn_velo_y = 0

        pygame.display.update()                     ## for game over white screen
        window.fill(black)              # for the showing the black ewhen snake moved out

        #snake food
        if abs(snake_x - food_x)<10 and (snake_y - food_y)<10:
            food_x = random.randint(300,700)
            food_y = random.randint(200 , 450)
            sn_length += 3
            score += 1*10
        message("Score : "+str(score),red,0,0)

        # for wall cross game over

        if snake_x>width or snake_x<0 or snake_y>height or snake_y<0:
            game_over=True

        pygame.draw.rect(window,yellow,[food_x,food_x,sn_sz,sn_size]) # boll
        snake_x += snvelo_x
        snake_y += sn_velo_y


        if len(snak_list)>sn_length:
            del snak_list[0]

        head=[]
        head.append(snake_x)
        head.append(snake_y)

        if head in snak_list[:-1]:  # for snake cross it self so game over
            game_over==True
        snak_list.append(head)

        game(window, pink, snak_list, sn_size,sn_sz) # argument

        clock.tick(fps)
    pygame.display.update()

    pygame.quit()
    quit()
    pygame.display.update()

snake()
