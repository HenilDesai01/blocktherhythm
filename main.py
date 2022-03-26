import pygame  # imports pygame library
from pygame import *  # imports everything from the library


def init_pygame():  # funtion
    pygame.init()  # initiates library

    white = 255, 255, 255, 0
    screen = pygame.display.set_mode(size=[800, 800])
    hexagon = pygame.image.load("assets/hexagon.png")
    hexagon = pygame.transform.scale(hexagon, (150, 150))
    hex_obj = hexagon.get_rect()
    screen.fill(white)
    screen.blit(hexagon, hex_obj)
    pygame.display.flip()


def main():  # funtion of main file
    init_pygame()
    # gameloop
    while True:
        print("prussia")


if __name__ == '__main__':  # checks if the file being runs name, and if true runs main function
    main()
