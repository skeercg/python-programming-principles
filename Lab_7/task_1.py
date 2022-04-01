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
# leftHand = pygame.transform.flip(leftHand, flip_x=False, flip_y=True)
rightHand = pygame.image.load('right.png')
rightHand = pygame.transform.scale(rightHand, (80, 300))
rotatedRightHand = rightHand
rotatedLeftHand = leftHand

minutes = datetime.datetime.now().minute
seconds = datetime.datetime.now().second
rightHandAngle = minutes * 6
leftHandAngle = seconds * 6

def getOrigin(image, angle):
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    origin = (467 + min_box[0], 350 - max_box[1])
    return origin

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
