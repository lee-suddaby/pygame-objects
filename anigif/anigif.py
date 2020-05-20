import numpy as np
import pygame

#Custom object containing data for displaying an animated GIF
#Created as python is not very friendly when it comes to interacting with animated GIFs
class AnimatedGif:
    def __init__(self, new_x, new_y, new_w, new_h, new_paths, new_fps=10):
        self.frameCounter = 0 #Index of frame array that contains the next image to be displayed
        self.x = new_x
        self.y = new_y
        self.w = new_w
        self.h = new_h
        self.fps = new_fps #FPS = Frames per Second
        self.time_dif = int(1000/self.fps)
        self.init_ticks = pygame.time.get_ticks()
        self.noOfFrames = len(new_paths)
        self.framePaths = np.array(new_paths) #Array of string, to store the file paths
        self.frames = np.array([None] * self.noOfFrames) #Array of pygame Surface objects, to store the actual graphical frames
        for n in range(self.noOfFrames):
            self.frames[n] = pygame.transform.scale(pygame.image.load(new_paths[n]), [self.w, self.h])

    #Return frame of the GIF to be displayed at any given moment, based on ticks (i.e. time) and fps of the gif
    #The GIF loops indefinitely
    def draw(self, screen):
        self.frameCounter = int((pygame.time.get_ticks() - self.init_ticks) / self.time_dif) % self.noOfFrames
        screen.blit(self.frames[self.frameCounter], [self.x, self.y])
