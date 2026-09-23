import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invisible Collider Example")

# 1. Define the invisible collider area (x, y, width, height)
invisible_button = pygame.Rect(300, 250, 200, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # 2. Check for mouse button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # 3. Check if the mouse position is inside the invisible rect
                if invisible_button.collidepoint(event.pos):
                    print("Invisible collider clicked!")

    # Fill the screen with a solid color (the rect is never drawn)
    screen.fill((40, 40, 40))
    
    pygame.display.flip()
