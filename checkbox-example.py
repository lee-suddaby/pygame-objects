import pygame
from checkbox import *

pygame.init()
clock = pygame.time.Clock()

check = CheckBox(50,50,50,False)

font_40 = pygame.font.SysFont("Arial", 40)
check_txt = font_40.render("Fill Screen Green?", True, (0,0,0))

screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Checkbox Example")
screen.fill((0,0,0))
running = True

while running:
    for event in pygame.event.get():
        check.handle_input_event(event)
        if event.type == pygame.QUIT:
            running = False

    if check.checked:
        screen.fill((0,255,0))
    else:
        screen.fill((255,255,255))

    check.draw(screen)
    screen.blit(check_txt, [110, 55])

    clock.tick(25)
    pygame.display.flip()

pygame.quit()