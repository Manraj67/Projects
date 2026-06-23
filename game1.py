import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and backround image")
backround_image = pygame.transform.scale(pygame.image.load("abc.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
peinguin_image = pygame.transform.scale(pygame.image.load("abcd.png")).convert_alpha(), (200, 200)
peinguin_rect = peinguin_image.get_rect(center=(SCREEN_WIDTH))
pygame