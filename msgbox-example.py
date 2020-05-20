import pygame
from msgbox import MessageBox
from button import Button

pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()

message = 'The quick brown fox jumps over the lazy dog, but that does not tell us anything about what the cat did. \n This starts a new line.'
title = 'This is a title'

messageBox = None
msgBut = Button(250, 200, 250, 80, "Show Message", pygame.font.SysFont("Arial", 40), but_col=(75, 181, 49), txt_col=(255,255,255))

running = True
while running:
    for event in pygame.event.get():
        msgBut.handle_input_event(event)

        if messageBox != None:
            messageBox.handle_input_event(event)
            if messageBox.should_exit == False: #Prevents any other actions taking place on screen while the messagebox is visible.
                break
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if msgBut.clicked():
        messageBox = MessageBox(screen, message, title)

    msgBut.render(screen)
    if messageBox != None:
        messageBox.update()
        if messageBox.should_exit == False:
            messageBox.draw(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
