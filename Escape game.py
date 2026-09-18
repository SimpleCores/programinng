import pygame
import sys
import time

#type (python "Escape game.py") in terminal to open 
#load images
pygame.init()
pygame.display

#game setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game")

clock = pygame.time.Clock()
FPS = 60

# Load images to game
 into my game
img_test2 = pygame.image.load("eat.png").convert_alpha()
img_test1 = pygame.image.load("Test image.png").convert_alpha()

# Size images
img_test2 = pygame.transform.scale(img_test2, (720, 400))
img_test1 = pygame.transform.scale(img_test1, (800, 425))

# Create colliders for the images
img_test2_rect = img_test2.get_rect(topleft=(0, 0))
img_test1_rect = img_test1.get_rect(topleft=(0, 0))


running = True

while running:

    # mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check events or something
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if img_test1_rect.collidepoint(mouse_pos):
                print("Image clicked!")

    # Change cursor when hovering
    if img_test1_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw stuf
    screen.fill((40, 40, 40))

    screen.blit(img_test2, img_test2_rect)
    screen.blit(img_test1, img_test1_rect)


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()