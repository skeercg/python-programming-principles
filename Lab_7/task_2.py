from time import sleep
from pygame import mixer
import pygame

pygame.init()
mixer.init()
mixer.music.load('track_1.wav')
screen = pygame.display.set_mode((400, 300))

isPaused = True
currentTrack = 0

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
txt = font.render('track_1', True, (255, 255, 255))

while True:
    screen.fill((0, 30, 30))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
    
    if (currentTrack == 0):
        txt = font.render('track_1', True, (255, 255, 255))
    else: 
        txt = font.render('track_2', True, (255, 255, 255))

    screen.blit(txt, (160, 80))

    pygame.draw.rect(screen, (30, 60, 60), (0, 200, 400, 100))

    pygame.draw.circle(screen, (255, 255, 255), (200, 250), 32)
    pygame.draw.circle(screen, (0, 0, 0), (200, 250), 30)

    key_input = pygame.key.get_pressed()   
    if (key_input[pygame.K_SPACE]):
        isPaused = not isPaused
        if (isPaused):
            mixer.music.pause()
        else: 
            mixer.music.play()

    if (key_input[pygame.K_LEFT]):
        currentTrack += 1
        currentTrack %= 2
        mixer.music.stop()
        mixer.music.unload()
        if (currentTrack == 0):
            mixer.music.load('track_1.wav')
        else:
            mixer.music.load('track_2.wav')
        isPaused = False
        mixer.music.play()

    if (key_input[pygame.K_RIGHT]):
        currentTrack += 1
        currentTrack %= 2
        mixer.music.stop()
        mixer.music.unload()
        if (currentTrack == 0):
            mixer.music.load('track_1.wav')
        else:
            mixer.music.load('track_2.wav')
        isPaused = False
        mixer.music.play()
    

    if (not isPaused):
        pygame.draw.rect(screen, (255, 255, 255), (188, 237, 10, 25))
        pygame.draw.rect(screen, (255, 255, 255), (203, 237, 10, 25))
    else: 
        pygame.draw.polygon(screen, (255, 255, 255), [(215, 250), (190, 235), (190, 265)])

    pygame.draw.circle(screen, (255, 255, 255), (100, 250), 32)
    pygame.draw.circle(screen, (0, 0, 0), (100, 250), 30)
    pygame.draw.polygon(screen, (255, 255, 255), [(85, 250), (105, 260), (105, 240)])
    pygame.draw.polygon(screen, (255, 255, 255), [(95, 250), (115, 260), (115, 240)])

    pygame.draw.circle(screen, (255, 255, 255), (300, 250), 32)
    pygame.draw.circle(screen, (0, 0, 0), (300, 250), 30)
    pygame.draw.polygon(screen, (255, 255, 255), [(315, 250), (295, 260), (295, 240)])
    pygame.draw.polygon(screen, (255, 255, 255), [(305, 250), (285, 260), (285, 240)])

    pygame.display.update()
    sleep(0.2)

