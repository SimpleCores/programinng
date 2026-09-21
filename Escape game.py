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

#story images
Story1 = pygame.image.load("Story1.png").convert_alpha()
Story2 = pygame.image.load("Story2.png").convert_alpha()
Story3 = pygame.image.load("Story3.png").convert_alpha()
Story4 = pygame.image.load("Story4.png").convert_alpha()
Story5 = pygame.image.load("Story5.png").convert_alpha()
Story6 = pygame.image.load("Story6.png").convert_alpha()
Story7 = pygame.image.load("Story7.png").convert_alpha()
Story8 = pygame.image.load("Story8.png").convert_alpha()
Story9 = pygame.image.load("Story9.png").convert_alpha()
Story10 = pygame.image.load("Story10.png").convert_alpha()
Story11 = pygame.image.load("Story11.png").convert_alpha()
Story12 = pygame.image.load("Story12.png").convert_alpha()
Story13 = pygame.image.load("Story13.png").convert_alpha()
Story14 = pygame.image.load("Story14.png").convert_alpha()
Story15 = pygame.image.load("Story15.png").convert_alpha()
Story16 = pygame.image.load("Story16.png").convert_alpha()
Story17 = pygame.image.load("Story17.png").convert_alpha()
Story18 = pygame.image.load("Story18.png").convert_alpha()
Story19 = pygame.image.load("Story19.png").convert_alpha()
Story20 = pygame.image.load("Story20.png").convert_alpha()
Story21 = pygame.image.load("Story21.png").convert_alpha()
Story22 = pygame.image.load("Story22.png").convert_alpha()
Story23 = pygame.image.load("Story23.png").convert_alpha()
Story24 = pygame.image.load("Story24.png").convert_alpha()
Story25 = pygame.image.load("Story25.png").convert_alpha()
Story26 = pygame.image.load("Story26.png").convert_alpha()
Story27 = pygame.image.load("Story27.png").convert_alpha()
Story28 = pygame.image.load("Story28.png").convert_alpha()
Story29 = pygame.image.load("Story29.png").convert_alpha()
Story30 = pygame.image.load("Story30.png").convert_alpha()
Story31 = pygame.image.load("Story31.png").convert_alpha()
Story32 = pygame.image.load("Story32.png").convert_alpha()
Story33 = pygame.image.load("Story33.png").convert_alpha()
Story34 = pygame.image.load("Story34.png").convert_alpha()
Story35 = pygame.image.load("Story35.png").convert_alpha()
Story36 = pygame.image.load("Story36.png").convert_alpha()
Story37 = pygame.image.load("Story37.png").convert_alpha()
Story38 = pygame.image.load("Story38.png").convert_alpha()
Story39 = pygame.image.load("Story39.png").convert_alpha()
Story40 = pygame.image.load("Story40.png").convert_alpha()
Story41 = pygame.image.load("Story41.png").convert_alpha()
Story42 = pygame.image.load("Story42.png").convert_alpha()
Story43 = pygame.image.load("Story43.png").convert_alpha()
Story44 = pygame.image.load("Story44.png").convert_alpha()
Story45 = pygame.image.load("Story45.png").convert_alpha()
Story46 = pygame.image.load("Story46.png").convert_alpha()
Story47 = pygame.image.load("Story47.png").convert_alpha()
Story48 = pygame.image.load("Story48.png").convert_alpha()
Story49 = pygame.image.load("Story49.png").convert_alpha()
Story50 = pygame.image.load("Story50.png").convert_alpha()
Story51 = pygame.image.load("Story51.png").convert_alpha()
Story52 = pygame.image.load("Story52.png").convert_alpha()
Story53 = pygame.image.load("Story53.png").convert_alpha()
Story54 = pygame.image.load("Story54.png").convert_alpha()
Story55 = pygame.image.load("Story55.png").convert_alpha()
Story56 = pygame.image.load("Story56.png").convert_alpha()
Story57 = pygame.image.load("Story57.png").convert_alpha()
Story58 = pygame.image.load("Story58.png").convert_alpha()
Story59 = pygame.image.load("Story59.png").convert_alpha()
Story60 = pygame.image.load("Story60.png").convert_alpha()

#game images
game1 = pygame.image.load("game1.png").convert_alpha()
game2 = pygame.image.load("game2.png").convert_alpha()
game3 = pygame.image.load("game3.png").convert_alpha()

# Sizes images
img_test2 = pygame.transform.scale(img_test2, (720, 400))
img_test1 = pygame.transform.scale(img_test1, (800, 425))

# Story images
Story1 = pygame.transform.scale(Story1, (800, 600))
Story2 = pygame.transform.scale(Story2, (800, 600))
Story3 = pygame.transform.scale(Story3, (800, 600))
Story4 = pygame.transform.scale(Story4, (800, 600))
Story5 = pygame.transform.scale(Story5, (800, 600))
Story6 = pygame.transform.scale(Story6, (800, 600))
Story7 = pygame.transform.scale(Story7, (800, 600))
Story8 = pygame.transform.scale(Story8, (800, 600))
Story9 = pygame.transform.scale(Story9, (800, 600))
Story10 = pygame.transform.scale(Story10, (800, 600))
Story11 = pygame.transform.scale(Story11, (800, 600))
Story12 = pygame.transform.scale(Story12, (800, 600))
Story13 = pygame.transform.scale(Story13, (800, 600))
Story14 = pygame.transform.scale(Story14, (800, 600))
Story15 = pygame.transform.scale(Story15, (800, 600))
Story16 = pygame.transform.scale(Story16, (800, 600))
Story17 = pygame.transform.scale(Story17, (800, 600))
Story18 = pygame.transform.scale(Story18, (800, 600))
Story19 = pygame.transform.scale(Story19, (800, 600))
Story20 = pygame.transform.scale(Story20, (800, 600))
Story21 = pygame.transform.scale(Story21, (800, 600))
Story22 = pygame.transform.scale(Story22, (800, 600))
Story23 = pygame.transform.scale(Story23, (800, 600))
Story24 = pygame.transform.scale(Story24, (800, 600))
Story25 = pygame.transform.scale(Story25, (800, 600))
Story26 = pygame.transform.scale(Story26, (800, 600))
Story27 = pygame.transform.scale(Story27, (800, 600))
Story28 = pygame.transform.scale(Story28, (800, 600))
Story29 = pygame.transform.scale(Story29, (800, 600))
Story30 = pygame.transform.scale(Story30, (800, 600))
Story31 = pygame.transform.scale(Story31, (800, 600))
Story32 = pygame.transform.scale(Story32, (800, 600))
Story33 = pygame.transform.scale(Story33, (800, 600))
Story34 = pygame.transform.scale(Story34, (800, 600))
Story35 = pygame.transform.scale(Story35, (800, 600))
Story36 = pygame.transform.scale(Story36, (800, 600))
Story37 = pygame.transform.scale(Story37, (800, 600))
Story38 = pygame.transform.scale(Story38, (800, 600))
Story39 = pygame.transform.scale(Story39, (800, 600))
Story40 = pygame.transform.scale(Story40, (800, 600))
Story41 = pygame.transform.scale(Story41, (800, 600))
Story42 = pygame.transform.scale(Story42, (800, 600))
Story43 = pygame.transform.scale(Story43, (800, 600))
Story44 = pygame.transform.scale(Story44, (800, 600))
Story45 = pygame.transform.scale(Story45, (800, 600))
Story46 = pygame.transform.scale(Story46, (800, 600))
Story47 = pygame.transform.scale(Story47, (800, 600))
Story48 = pygame.transform.scale(Story48, (800, 600))
Story49 = pygame.transform.scale(Story49, (800, 600))
Story50 = pygame.transform.scale(Story50, (800, 600))
Story51 = pygame.transform.scale(Story51, (800, 600))
Story52 = pygame.transform.scale(Story52, (800, 600))
Story53 = pygame.transform.scale(Story53, (800, 600))
Story54 = pygame.transform.scale(Story54, (800, 600))
Story55 = pygame.transform.scale(Story55, (800, 600))
Story56 = pygame.transform.scale(Story56, (800, 600))
Story57 = pygame.transform.scale(Story57, (800, 600))
Story58 = pygame.transform.scale(Story58, (800, 600))
Story59 = pygame.transform.scale(Story59, (800, 600))
Story60 = pygame.transform.scale(Story60, (800, 600))

#game images
game1 = pygame.transform.scale(game1, (800, 600))
game2 = pygame.transform.scale(game2, (800, 600))
game3 = pygame.transform.scale(game3, (800, 600))


# Create colliders for images
img_test2_rect = img_test2.get_rect(topleft=(0, 0))
img_test1_rect = img_test1.get_rect(topleft=(0, 0))


# Cutscene images and how long they show for
cutscene = [
    (Story1, 1),
    (Story2, 1),
    (Story3, 1),
    (Story4, 1),
    (Story5, 1),
    (Story6, 1),
    (Story7, 1),
    (Story8, 1),
    (Story9, 1),
    (Story10, 1),
    (Story11, 1),
    (Story12, 1),
    (Story13, 1),
    (Story14, 1),
    (Story15, 1),
    (Story16, 1),
    (Story17, 1),
    (Story18, 1),
    (Story19, 1),
    (Story20, 1),
    (Story21, 1),
    (Story22, 1),
    (Story23, 1),
    (Story24, 1),
    (Story25, 1),
    (Story26, 1),
    (Story27, 1),
    (Story28, 1),
    (Story29, 1),
    (Story30, 1),
    (Story31, 1),
    (Story32, 1),
    (Story33, 1),
    (Story34, 1),
    (Story35, 1),
    (Story36, 1),
    (Story37, 1),
    (Story38, 1),
    (Story39, 1),
    (Story40, 1),
    (Story41, 1),
    (Story42, 1),
    (Story43, 1),
    (Story44, 1),
    (Story45, 1),
    (Story46, 1),
    (Story47, 1),
    (Story48, 1),
    (Story49, 1),
    (Story50, 1),
    (Story51, 1),
    (Story52, 1),
    (Story53, 1),
    (Story54, 1),
    (Story55, 1),
    (Story56, 1),
    (Story57, 1),
    (Story58, 1),
    (Story59, 1),
    (Story60, 1),

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

    # Cutscene after pressing play
    else:
         if current_slide < len(cutscene):
            image, duration = cutscene[current_slide]
            screen.blit(image, (0, 0))

    # The actual game thing after cutscene finishes
         else:
            screen.blit(game1, game1_rect)
            screen.blit(game2, game2_rect)
            screen.blit(game3, game3_rect)


    pygame.display.flip()

    clock.tick(FPS)

# Exit smoothly code
pygame.quit()
sys.exit()