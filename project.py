from bird import Bird
from hurdle import Hurdle

import random
import time
import pygame
from pygame.locals import *

pygame.init()


def main():
    clock = pygame.time.Clock()

    width = 800
    height = 500
    score = 0

    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)

    bg_img = pygame.image.load('images/bg.png')
    bg_img = pygame.transform.scale(bg_img, (width, height))

    screen = pygame.display.set_mode((width, height))

    bird_group = pygame.sprite.Group()
    x = 200
    y = cal_y(height)
    player_bird = Bird(x, y)
    bird_group.add(player_bird)

    # restart button
    button = pygame.image.load("images/restart.png").convert_alpha()
    button_rect = button.get_rect()
    button_rect.center = [width/2, height/2]

    # quit button
    quit = pygame.image.load("images/quit1.png").convert_alpha()
    quit_rect = quit.get_rect()
    quit_rect.center = [width/2, quit_position(height)]

    random.seed(time.time())
    hurdle_height = random.randint(500, 800)
    hurdle_group = pygame.sprite.Group()

    hurdle_list = []
    hurdle = Hurdle(width+40, hurdle_height, 1)
    hurdle2 = Hurdle(width+40, cal_position(hurdle_height), 2)
    hurdle_list.append(hurdle)
    hurdle_list.append(hurdle2)
    hurdle_group.add(hurdle)
    hurdle_group.add(hurdle2)

    pygame.display.set_caption('Flappy Bird')

    pygame.display.flip()

    running = True

    counter = 0
    delay = 150

    out = False

    while running:
        screen.blit(bg_img, (0, 0))

        # score
        text = font.render(f'Score : {int(score)}', True, white)
        textRect = text.get_rect()
        textRect.center = (width/2, 20)

        for hurdle in hurdle_list:
            if hurdle.get_pos() < x:
                score += 0.5
                hurdle_list.remove(hurdle)

        if out == False:
            counter += 1
            if counter > delay:
                hurdle_height = random.randint(500, 800)
                hurdle = Hurdle(width+20, hurdle_height, 1)
                hurdle2 = Hurdle(width+20, cal_position(hurdle_height), 2)
                hurdle_group.add(hurdle)
                hurdle_group.add(hurdle2)
                hurdle_list.append(hurdle)
                hurdle_list.append(hurdle2)
                counter = 0

        hurdle_group.draw(screen)
        screen.blit(text, textRect)

        if out == False:
            hurdle_group.update()
        else:
            screen.blit(button, button_rect)
            screen.blit(quit, quit_rect)

        bird_group.draw(screen)
        bird_group.update()

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.left <= mouse[0] <= button_rect.right and button_rect.top <= mouse[1] <= button_rect.bottom:
                    main()
                elif quit_rect.left <= mouse[0] <= quit_rect.right and quit_rect.top <= mouse[1] <= quit_rect.bottom:
                    running = False

        if pygame.sprite.spritecollideany(player_bird, hurdle_group):
            player_bird.kill()
            out = True

        clock.tick(60)

    pygame.quit()


def quit_position(height):
    return height/2+50


def cal_y(height):
    return height/2


def cal_position(hurdle_height):
    return hurdle_height-700


if __name__ == "__main__":
    main()
