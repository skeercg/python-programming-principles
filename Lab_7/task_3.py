import pygame

pygame.init()
screen = pygame.display.set_mode((390, 390))
x = 25
y = 25
step = 20
while True:
    screen.fill((255, 255, 255))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(screen, (255,0,0), (x, y), 25)
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        if (x - step >= 25):
            x -= step
    if key_input[pygame.K_UP]:
        if (y - step >= 25):
            y -= step
    if key_input[pygame.K_RIGHT]:
        if (x + step <= 375):
            x += step
    if key_input[pygame.K_DOWN]:
        if (y + step <= 375):
            y += step
    pygame.display.update()