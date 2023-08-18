import pygame
import time
import random, math

pygame.init()

#seting up the window
WIDTH = 1080
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
COLORS = ["green", "yellow", "blue", "purple"]



#defining the game colors
red = (255,0,0)
green = (0,255,0)

snake_block_size = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg,True, color)
    screen.blit(mesg, [WIDTH/6, HEIGHT/3])

    pygame.display.update()

def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.circle(screen,"red",(x,y),snake_block_size)
        #pygame.draw.rect(screen, "red", [x,y ,snake_block_size, snake_block_size])

def gameloop():
    game_close = False
    game_over = False
    

    x1 = WIDTH/2  
    y1 = HEIGHT/2

    x1_change = 0
    y1_change = 0

    food_x = round(random.randrange(0, WIDTH - 2*(snake_block_size))/10.0)*10.0
    food_y = round(random.randrange(0, HEIGHT - 2*(snake_block_size))/10.0)*10.0
    print(food_x,food_y)
    snake_body = []
    lenght_of_snake = 1
    score = 0

    clock = pygame.time.Clock()
    while not game_over:
        screen.fill("white")
        color = COLORS[random.randrange(0, len(COLORS ))]
        
        while game_close == True:    
        
            screen.fill("red")
            message("You lost! Press Q-Quit or C-Play again", "black")
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:                        
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
    
        if x1 + snake_block_size >= WIDTH or x1 - snake_block_size < 0 or y1 + snake_block_size >= HEIGHT or y1 - snake_block_size < 0:
            game_close = True
    
        x1 += x1_change
        y1 += y1_change

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)    
        if len(snake_body) > lenght_of_snake:
            del snake_body[0]

        dist = math.sqrt((x1 - food_x)**2 + (y1 - food_y)**2)
        if dist<2*snake_block_size:
        #if food_x == x1 and food_y == y1:
            food_x = round(random.randrange(0, WIDTH - 2*snake_block_size)/10.0)*10.0
            food_y = round(random.randrange(0, HEIGHT - 2*snake_block_size)/10.0)*10.0
            score += 10
            lenght_of_snake +=1

        draw_snake(snake_body)

        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True
        
        
        mesg = font_style.render("SCORE: " +str(score),True, "yellow")
        screen.blit(mesg, (WIDTH - mesg.get_width() - 10,10))
        #pygame.draw.rect(screen,color, [food_x,food_y,snake_block_size,snake_block_size])
        pygame.draw.circle(screen,COLORS[random.randrange(0, len(COLORS ))],(food_x,food_y),snake_block_size)
        pygame.display.update()
        clock.tick(15)

gameloop()