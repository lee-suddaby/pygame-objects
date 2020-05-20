import pygame
from textbox import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([400,300])
screen.fill((255,255,255))

test_box = TextBox((100, 150, 200, 30), clear_on_enter=False, inactive_on_enter=False, active=False, active_color=pygame.Color("red"))

exit = False

counter = 0
while not exit:
    for event in pygame.event.get():
        test_box.get_event(event)
        if event.type == pygame.QUIT:
            exit = True
    
    screen.fill((255,255,255))
    test_box.update()
    test_box.draw(screen)

    clock.tick(30)
    pygame.display.flip()

pygame.quit()