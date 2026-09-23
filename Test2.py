import pygame
import sys

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cutscene")

clock = pygame.time.Clock()

# Load cutscene images
image1 = pygame.image.load("cutscene1.png").convert()
image2 = pygame.image.load("cutscene2.png").convert()
image3 = pygame.image.load("cutscene3.png").convert()

# Resize images to fit the screen
image1 = pygame.transform.scale(image1, (800, 600))
image2 = pygame.transform.scale(image2, (800, 600))
image3 = pygame.transform.scale(image3, (800, 600))

# Cutscene images and how long they show
cutscene = [
    (image1, 3),
    (image2, 3),
    (image3, None)
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

    else:
        # Your actual game starts here
        screen.fill((40, 40, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()