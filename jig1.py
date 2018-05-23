import pygame
import os
_image_library = {}
pygame.init()
screen = pygame.display.set_mode((1300, 1300))
done = False
clock = pygame.time.Clock()
h=20
w=20
f=1
for i in range(0,2):
    for j in range(0,2):
        img=pygame.image.load(str(f)+".png").convert()
        img=pygame.transform.scale(img,(100,100))

        screen.blit(img, (w, h))
        w += 110
        f+=1
        pygame.display.flip()
    h += 110
    w=20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    # for i in range(1,5):
    #     screen.blit(get_image(str(i)+'.png'), (h, w))
    #     h+=100
    #     w+=100
    #     pygame.display.flip()
    clock.tick(60)