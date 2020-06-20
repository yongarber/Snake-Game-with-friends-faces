import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = int(600*1.4)
dis_height = int(400*1.4)
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game for Stav')
 
clock = pygame.time.Clock()

Neta=pygame.image.load("./20200110_143850.jpg").convert()
Yon=pygame.image.load("./20200526_142506.jpg").convert()
Itamar=pygame.image.load("./20200526_142331.jpg").convert()
Leah=pygame.image.load("./20200526_142629.jpg").convert()
Gil=pygame.image.load("./20200526_142831.jpg").convert()

FOODLIST=[Yon,Neta, Gil, Leah,Itamar]




IMAGE= pygame.image.load("20200526_141844.jpg").convert()
Neta= pygame.image.load("20200110_143850.jpg").convert()
snake_block = IMAGE.get_rect()
# food_block = FOOD.get_rect()
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 30)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(IMAGE, snake_list):
    for x in snake_list:
        dis.blit(IMAGE, (x[0],x[1]))
        # pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 2])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block[2])/20 )*20 
    foody = round(random.randrange(0, dis_height - snake_block[3])/20 ) *20
    FOOD=random.choice(FOODLIST)
    
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block[2]
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block[2]
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block[3]
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block[3]
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        dis.blit(FOOD, (foodx,foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(IMAGE, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block[2]) / 20 )*20
            foody = round(random.randrange(0, dis_height - snake_block[3]) /20 )*20
            FOOD=random.choice(FOODLIST)
            Length_of_snake += 1
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()