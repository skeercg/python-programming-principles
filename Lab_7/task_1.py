import time,pygame
pygame.init()
theFont=pygame.font.Font(None,72)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((320, 200))
pygame.display.set_caption('Pi Time')
while True:
    clock.tick(1)
    theTime=time.strftime("%H:%M:%S", time.localtime())
    timeText=theFont.render(str(theTime), True,(255,255,255),(0,0,0))
    screen.blit(timeText, (79,60))
    pygame.display.update()
    pygame.quit()