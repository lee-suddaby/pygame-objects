import pygame
from anigif import *

pygame.init()
clock = pygame.time.Clock()

imagesCA = [""] * 12
for counter in range(12):
    imagesCA[counter] = "assets/gif_frames/coin_frame_" + str(counter+1) + ".png"

coin1 = AnimatedGif(25,100,96,96,imagesCA, 10)
coin2 = AnimatedGif(140,100,96,96,imagesCA, 20)

font_fps = pygame.font.SysFont('Arial', 24)
font1 = font_fps.render("FPS = 10", True, (255,255,255))
font2 = font_fps.render("FPS = 20", True, (255,255,255))

screen = pygame.display.set_mode([250,250])
pygame.display.set_caption("AniGif Example")
screen.fill((0,0,0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    screen.blit(coin1.getCurFrame(), [coin1.x,coin1.y])
    screen.blit(coin2.getCurFrame(), [coin2.x,coin2.y])
    screen.blit(font1, [25, 200])
    screen.blit(font2, [140, 200])

    clock.tick(25)
    pygame.display.flip() #Update display

pygame.quit()