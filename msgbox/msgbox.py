#Multiline textbox class
import pygame
import numpy as np

class MessageBox:
    def __init__(self, screen, message, title='Message', font=None, window_width=0):
        if window_width == 0:
            window_width = 500
        self.window_rect = pygame.Rect(0,0,window_width,0)

        self.font = font
        if self.font == None:
            self.font = pygame.font.SysFont('Arial', 24)

        self.background_colour = pygame.Color("#555555")
        self.text_colour = pygame.Color("#FFFFFF")

        self.message = message
        self.message_text_render = self.createText(self.font, self.message, self.text_colour, self.window_rect)
        self.window_rect.height = self.message_text_render[0].get_height() * len(self.message_text_render) + 100
        self.window_rect.center = screen.get_rect().center
        
        self.window_title_str = title
        self.title_text_render = self.font.render(self.window_title_str, True, self.text_colour)

        self.should_exit = False
        
        self.done_button = UTTextButton([self.window_rect[0] + (self.window_rect[2] / 2) + 45,
                                         self.window_rect[1] + self.window_rect[3] - 30, 70, 20], "Done", self.font)

        

    def handle_input_event(self, event):
        self.done_button.handle_input_event(event)

    def update(self):
        if self.done_button.was_pressed():
            self.should_exit = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, pygame.Rect(self.window_rect[0], self.window_rect[1],
                                                                     self.window_rect[2], self.window_rect[3]), 0)

        screen.blit(self.title_text_render,
                    self.title_text_render.get_rect(centerx=self.window_rect[0] + self.window_rect[2] * 0.5,
                                                    centery=self.window_rect[1] + 24))

        y_pos = self.window_rect[1]+60
        for cur_text in self.message_text_render:
            screen.blit(cur_text, [self.window_rect[0]+20, cur_text.get_rect(centery=y_pos).y])
            y_pos += cur_text.get_height()

        self.done_button.draw(screen)

    def createText(self, font, message, text_col, wind_rect):
        cur_str = str()
        word_arr = message.split(' ')
        count = 0
        ret_texts = []
        done = False
        while not done:
            new_str = cur_str + word_arr[count] + ' '
             #'\n' is used to designate a manual line break
            if font.size(new_str)[0] > wind_rect[2]-40 or count+1 >= len(word_arr) or word_arr[count] == '\n':
                if count+1 >= len(word_arr):
                    ret_texts.append(font.render(new_str, True, text_col))
                else:
                    ret_texts.append(font.render(cur_str, True, text_col))

                if word_arr[count] != '\n':
                    cur_str = word_arr[count] + ' '
                else:
                    cur_str = str()
            else:
                cur_str = cur_str + word_arr[count] + ' '
            if count+1 >= len(word_arr):
                done = True
            count += 1
        return np.array(ret_texts)

class UTTextButton:
    def __init__(self, rect, text, font):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.text_colour = pygame.Color("#FFFFFF")
        self.background_colour = pygame.Color("#151515")
        self.text_render = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = self.rect.center
        self.MOUSEPRESSED = False

    def handle_input_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.MOUSEPRESSED = True
        else:
            self.MOUSEPRESSED = False
            
    def was_pressed(self):
        mpos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mpos) and self.MOUSEPRESSED:
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, self.rect)
        screen.blit(self.text_render, self.text_rect)
