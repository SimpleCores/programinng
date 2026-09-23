import pygame
import sys

# type python "Test2.py" in terminal to open

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cutscene")

clock = pygame.time.Clock()

# Skip button
skip_button = pygame.Rect(700, 540, 80, 40)
font = pygame.font.Font(None, 28)

# Load cutscene images
Story1 = pygame.image.load("Story1.png").convert()
Story2 = pygame.image.load("Story2.png").convert()
Story3 = pygame.image.load("Story3.png").convert()

# Resize images to fit the screen
Story1 = pygame.transform.scale(Story1, (800, 600))
Story2 = pygame.transform.scale(Story2, (800, 600))
Story3 = pygame.transform.scale(Story3, (800, 600))

# Cutscene images and how long they show
cutscene = [
    (Story1, 3),
    (Story2, 3),
    (Story3, 3)
]

current_slide = 0
start_time = pygame.time.get_ticks()

running = True

while running:

    current_time = pygame.time.get_ticks()
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Skip button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if skip_button.collidepoint(event.pos):
                current_slide = len(cutscene)

    # Change cursor when hovering over skip
    if skip_button.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Move to the next image after its timer
    if current_slide < len(cutscene):

        image, duration = cutscene[current_slide]

        if duration is not None:
            if current_time - start_time >= duration * 1000:
                current_slide += 1
                start_time = current_time

    # Draw
    screen.fill((0, 0, 0))

    if current_slide < len(cutscene):

        image, duration = cutscene[current_slide]
        screen.blit(image, (0, 0))

        # Draw skip button
        pygame.draw.rect(screen, (60, 60, 60), skip_button)

        skip_text = font.render("SKIP", True, (255, 255, 255))
        screen.blit(skip_text, (718, 550))

    else:

        # Your actual game starts here
        screen.fill((40, 40, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()