import pygame
import sys

# type python "Test1.py" in terminal to open

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cutscene")

clock = pygame.time.Clock()

# Load cutscene images
Story1 = pygame.image.load("Story1.png").convert_alpha()
Story2 = pygame.image.load("Story2.png").convert_alpha()
Story3 = pygame.image.load("Story3.png").convert_alpha()

# Resize images to fit the screen
Story1 = pygame.transform.scale(Story1, (800, 600))
Story2 = pygame.transform.scale(Story2, (800, 600))
Story3 = pygame.transform.scale(Story3, (800, 600))

# Cutscene images and how long they show
cutscene = [
    (Story1, 2),
    (Story2, 2),
    (Story3, 2)
]

current_slide = 0
start_time = pygame.time.get_ticks()

running = True

while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

   



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



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()