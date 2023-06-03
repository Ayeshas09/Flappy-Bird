import pygame

class Hurdle(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/pipe.png").convert_alpha()
        if pos == 2:
            self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.game_over = False

    def update(self):

        if self.game_over == False:

            if self.x > -45:
                self.x -= 2
                self.rect = self.image.get_rect()
                self.rect.center = [self.x, self.y]
            else:
                self.kill()

    def get_pos(self):
        return self.rect.right
