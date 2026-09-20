import pygame
import sys

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point and Click Adventure")
clock = pygame.time.Clock()

# Game state
room = 1
inventory = []
message = "Look around and find the key."

# Objects
key = pygame.Rect(200, 400, 50, 30)
door = pygame.Rect(550, 200, 120, 250)
chest = pygame.Rect(350, 350, 100, 80)
back = pygame.Rect(5, 550, 100, 40)

font = pygame.font.SysFont(None, 28)

running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if room == 1:

                if key and key.collidepoint(mouse_pos):
                    inventory.append("Rusty Key")
                    key = None
                    message = "You picked up the Rusty Key."

                elif door.collidepoint(mouse_pos):
                    room = 2
                    message = "You entered Room 2."

            elif room == 2:

                if chest.collidepoint(mouse_pos):

                    if "Rusty Key" in inventory:
                        message = "You unlocked the chest! You win!"
                    else:
                        message = "The chest is locked."

                elif back.collidepoint(mouse_pos):
                    room = 1
                    message = "You returned to Room 1."

    # Draw room
    screen.fill((40, 40, 40))

    if room == 1:
        pygame.draw.rect(screen, (80, 50, 50), (0, 0, WIDTH, 500))
        pygame.draw.rect(screen, (0, 0, 0), door)

        if key:
            pygame.draw.rect(screen, (255, 215, 0), key)

    else:
        pygame.draw.rect(screen, (50, 80, 50), (0, 0, WIDTH, 500))
        pygame.draw.rect(screen, (139, 69, 19), chest)
        pygame.draw.rect(screen, (200, 200, 200), back)

    # UI
    pygame.draw.rect(screen, (200, 200, 200), (0, 500, WIDTH, 100))

    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, (20, 515))

    inventory_text = font.render("Inventory: " + str(inventory), True, (0, 0, 0))
    screen.blit(inventory_text, (20, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()