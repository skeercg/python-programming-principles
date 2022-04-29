import pygame
import random
 
pygame.init()
   
screen = pygame.display.set_mode((600, 400))
 
clock = pygame.time.Clock()
 
snake_block = 10
 
font_style = pygame.font.SysFont(None, 25)
 
 
def score_view(score, level):
    value = font_style.render("Score: " + str(score) + " || Level: " + str(level), True, (0, 0, 0))
    screen.blit(value, [0, 0])
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (255, 0, 0), [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [600 / 6, 400 / 3])

game_over = False
game_close = False

x1 = 600 / 2
y1 = 400 / 2

x1_change = 0
y1_change = 0

snake_List = []
Length_of_snake = 1
level = 1
snake_speed = 15

foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

superfoodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
superfoody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

time_delay = 5000
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

while not game_over:

    while game_close == True:
        screen.fill((255, 0, 0))
        font = pygame.font.SysFont("Verdana", 60)
        game_over = font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over, (150,150))
        pygame.display.update()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change <= 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change >= 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change <= 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change >= 0:
                y1_change = snake_block
                x1_change = 0
        if event.type == pygame.USEREVENT + 1:
            superfoodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            superfoody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

    if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(screen, (0, 255, 255), [superfoodx, superfoody, snake_block, snake_block])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    our_snake(snake_block, snake_List)
    score_view(Length_of_snake - 1, level)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
        Length_of_snake += 1
        if (level != (Length_of_snake - 1) // 5 + 1):
            snake_speed = snake_speed + 10
        level = (Length_of_snake - 1) // 5 + 1

    if x1 == superfoodx and y1 == superfoody:
        superfoodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
        superfoody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
        Length_of_snake += 2
        if (level != (Length_of_snake - 1) // 5 + 1):
            snake_speed = snake_speed + 10
        level = (Length_of_snake - 1) // 5 + 1

    clock.tick(snake_speed)

pygame.quit()
