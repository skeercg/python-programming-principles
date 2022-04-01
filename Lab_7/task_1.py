import datetime
import pygame

pygame.init()
theFont=pygame.font.Font(None,72)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((934, 700))
bg = pygame.image.load('bg.jpeg')
bg = pygame.transform.scale(bg, (934, 700))
leftHand = pygame.image.load('left.png')
leftHand = pygame.transform.scale(leftHand, (80, 400))
rightHand = pygame.image.load('right.png')
rightHand = pygame.transform.scale(rightHand, (80, 300))
rotatedRightHand = rightHand
rotatedLeftHand = leftHand

minutes = datetime.datetime.now().minute
seconds = datetime.datetime.now().second
rightHandAngle = minutes * 6
leftHandAngle = seconds * 6

while True:
    currentTime = datetime.datetime.now()
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(rotatedLeftHand, rotatedLeftHand.get_rect(center = (467, 350)))

    screen.blit(rotatedRightHand, rotatedRightHand.get_rect(center = (467, 350)))

    

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
    
    rotatedRightHand = pygame.transform.rotate(rightHand, -rightHandAngle)
    rightHandAngle += abs(currentTime.minute - minutes) * 6

    minutes = currentTime.minute

    rotatedLeftHand = pygame.transform.rotate(leftHand, -leftHandAngle)
    leftHandAngle += abs(currentTime.second - seconds) * 6

    seconds = currentTime.second

    pygame.display.flip()
    pygame.display.update()
