import pygame
import sys
import time

# type python "Escape game.py" in terminal to open

pygame.init()

# game setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game")

# text font
font = pygame.font.SysFont(None, 50)

# menu buttons
play_button = pygame.Rect(300, 200, 200, 70)
quit_button = pygame.Rect(300, 320, 200, 70)

# caps frames to 60
clock = pygame.time.Clock()
FPS = 60

# Loads images
img_test2 = pygame.image.load("eat.png").convert_alpha()
img_test1 = pygame.image.load("Test image.png").convert_alpha()
Story1 = pygame.image.load("Story1.png").convert_alpha()
Story2 = pygame.image.load("Story2.png").convert_alpha()
Story3 = pygame.image.load("Story3.png").convert_alpha()
Story4 = pygame.image.load("Story4.png").convert_alpha()
Story5 = pygame.image.load("Story5.png").convert_alpha()
Story6 = pygame.image.load("Story6.png").convert_alpha()
Story7 = pygame.image.load("Story7.png").convert_alpha()
Story8 = pygame.image.load("Story8.png").convert_alpha()


# Sizes images
img_test2 = pygame.transform.scale(img_test2, (720, 400))
img_test1 = pygame.transform.scale(img_test1, (800, 425))
Story1 = pygame.transform.scale(Story1, (800, 600))
Story2 = pygame.transform.scale(Story2, (800, 600))
Story3 = pygame.transform.scale(Story3, (800, 600))
Story4 = pygame.transform.scale(Story4, (800, 600))
Story5 = pygame.transform.scale(Story5, (800, 600))
Story6 = pygame.transform.scale(Story6, (800, 600))
Story7 = pygame.transform.scale(Story7, (800, 600))
Story8 = pygame.transform.scale(Story8, (800, 600))


# Create colliders for images
img_test2_rect = img_test2.get_rect(topleft=(0, 0))
img_test1_rect = img_test1.get_rect(topleft=(0, 0))


# Cutscene images and how long they show
cutscene = [
    (Story1, 1),
    (Story2, 1),
    (Story3, 1),
    (Story4, 1),
    (Story5, 1),
    (Story6, 1),
    (Story7, 1),
    (Story8, 1),
]

current_slide = 0
start_time = pygame.time.get_ticks()



# Game loop
menu = True
running = True

while running:

    current_time = pygame.time.get_ticks()

    # Mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Menu button click
        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu:

                if play_button.collidepoint(event.pos):
                    menu = False

                if quit_button.collidepoint(event.pos):
                    running = False

# code here uncessceasry but lets me know if the button clik  actually work or not
            else:

                if img_test1_rect.collidepoint(event.pos):
                    print("button cliked")

    # Change cursor
    if menu:

        if play_button.collidepoint(mouse_pos) or quit_button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    else:
    # Move to the next image after its timer
        if current_slide < len(cutscene):

            image, duration = cutscene[current_slide]

            if duration is not None:
                if current_time - start_time >= duration * 1000:
                    current_slide += 1
                    start_time = current_time



        if img_test1_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Background color
    screen.fill((40, 40, 40))

    # Menu
    if menu:

        pygame.draw.rect(screen, (50, 150, 50), play_button)
        pygame.draw.rect(screen, (150, 50, 50), quit_button)

        play_text = font.render("PLAY", True, (255, 255, 255))
        quit_text = font.render("QUIT", True, (255, 255, 255))

        screen.blit(play_text, (350, 215))
        screen.blit(quit_text, (350, 335))

    # Game
    else:
         if current_slide < len(cutscene):
            image, duration = cutscene[current_slide]
            screen.blit(image, (0, 0))

         else:
            screen.blit(img_test2, img_test2_rect)
            screen.blit(img_test1, img_test1_rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()