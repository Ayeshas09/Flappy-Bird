import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.my_index = 0
        self.counter = 0
        self.images.append(pygame.image.load(
            "images/bird1.png").convert_alpha())
        self.images.append(pygame.image.load(
            "images/bird2.png").convert_alpha())
        self.images.append(pygame.image.load(
            "images/bird3.png").convert_alpha())
        self.image = pygame.image.load("images/bird1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.game_over = False

    def update(self):
        self.counter += 1
        flap_cooldown = 5

        if self.game_over == False:
            if self.counter > flap_cooldown:
                self.counter = 0
                self.my_index += 1
                if self.my_index >= len(self.images):
                    self.my_index = 0

            self.image = self.images[self.my_index]

            if self.y < 485:
                self.y += 2
                self.rect = self.image.get_rect()
                self.rect.center = [self.x, self.y]
            else:
                self.image = pygame.transform.rotate(
                    self.images[self.my_index], 270)
                self.game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.y -= 8
                self.rect = self.image.get_rect()
                self.rect.center = [self.x, self.y]

    def kill(self):
        self.y = 490
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.image = pygame.transform.rotate(
            self.images[self.my_index], 270)

    def get_pos(self):
        return self.images[self.my_index].rect.left
