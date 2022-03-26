import pygame  # imports pygame library
from pygame import *  # imports everything from the library
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = 255, 255, 255

screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill(WHITE)


def init_pygame():  # funtion
    pygame.init()  # initiates library


# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location


class Hexagon:  # creats a class of many functions to call upon
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/hexagon.svg")
        self.image = pygame.transform.scale(
            self.image, (self.height, self.width))

    def draw(self):
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        screen.blit(self.image, self.rect)
        pygame.display.flip()
        pygame.display.update()


def render():
    for x in range(5):
        for y in range(5):
            if x % 2 == 0:
                hex = Hexagon(75 + x*115, y*130 + 65 + 50, 150, 150)
                hex.draw()
            else:
                hex = Hexagon(75 + x*115, y*130 + 50, 150, 150)
                hex.draw()


def main():  # funtion of main file
    init_pygame()
    render()
    #BackGround = Background('background_image.png', [0,0])
    # gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


if __name__ == '__main__':  # checks if the file being runs name, and if true runs main function
    main()
