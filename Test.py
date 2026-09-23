import pygame
import sys

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Point and Click Adventure")
clock = pygame.time.Clock()

# Game state
room = 1
inventory = []

# Load images
room1 = pygame.image.load("Block.png").convert()
room2 = pygame.image.load("Black Border.png").convert()

key_image = pygame.image.load("eat.png").convert_alpha()
door_image = pygame.image.load("Test image.png").convert_alpha()
chest_image = pygame.image.load("Story2.png").convert_alpha()
back_image = pygame.image.load("Story1.png").convert_alpha()

# Resize images
room1 = pygame.transform.scale(room1, (800, 600))
room2 = pygame.transform.scale(room2, (800, 600))

key_image = pygame.transform.scale(key_image, (50, 30))
door_image = pygame.transform.scale(door_image, (120, 250))
chest_image = pygame.transform.scale(chest_image, (100, 80))
back_image = pygame.transform.scale(back_image, (100, 40))

# Image positions / colliders
key_rect = key_image.get_rect(topleft=(200, 400))
door_rect = door_image.get_rect(topleft=(550, 200))
chest_rect = chest_image.get_rect(topleft=(350, 350))
back_rect = back_image.get_rect(topleft=(5, 550))

running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if room == 1:

                # Click the key
                if key_rect and key_rect.collidepoint(event.pos):
                    inventory.append("Rusty Key")
                    key_rect = None

                # Click the door
                elif door_rect.collidepoint(event.pos):
                    room = 2

            elif room == 2:

                # Click the chest
                if chest_rect.collidepoint(event.pos):

                    if "Rusty Key" in inventory:
                        print("You unlocked the chest! You win!")
                    else:
                        print("The chest is locked.")

                # Click the back button
                elif back_rect.collidepoint(event.pos):
                    room = 1

    # Change cursor when hovering over clickable objects
    if room == 1:

        if door_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    else:

        if chest_rect.collidepoint(mouse_pos) or back_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw room
    if room == 1:

        screen.blit(room1, (0, 0))
        screen.blit(door_image, door_rect)

        if key_rect:
            screen.blit(key_image, key_rect)

    else:

        screen.blit(room2, (0, 0))
        screen.blit(chest_image, chest_rect)
        screen.blit(back_image, back_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()