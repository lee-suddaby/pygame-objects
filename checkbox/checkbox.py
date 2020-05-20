import pygame

class CheckBox:
    def __init__(self, new_x, new_y, new_dim, init_check=False, fill_col=(255,255,255), border_col = (0,0,0)):
        self.x = new_x
        self.y = new_y
        self.dim = new_dim
        self.rect = pygame.Rect(new_x, new_y, new_dim, new_dim)
        self.checked = init_check
        self.fill_col = fill_col
        self.border_col = border_col
        self.render_rect = None
        self.update()
    
    def handle_input_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
                self.update()

    def update(self):
        self.render_rect = pygame.Surface((self.dim, self.dim))
        self.render_rect.fill(self.fill_col)
        pygame.draw.rect(self.render_rect, self.border_col, pygame.Rect(0,0,self.dim,self.dim), round(self.dim/20))
        if self.checked:
            pygame.draw.line(self.render_rect, (0,0,0), [round(self.dim/20), round(self.dim/2)], [round(3*self.dim/8), round(19*self.dim/20)], round(self.dim/10)) #Display two lines corresponding to the two parts of a tick
            pygame.draw.line(self.render_rect, (0,0,0), [round(3*self.dim/8), round(19*self.dim/20)], [round(self.dim), 0], round(self.dim/10))

    def draw(self, screen):
        screen.blit(self.render_rect, [self.x, self.y]) #100,200,40,40