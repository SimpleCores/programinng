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

#font
font = pygame.font.SysFont(None,50)

#buttons
play_button = pygame.Rect(300,200,200,70)
quit_button = pygame.Rect(300,320,200,70)

#caps frames to 60
clock = pygame.time.Clock()
FPS = 60

# Load images to game
img_test2 = pygame.image.load("eat.png").convert_alpha()
img_test1 = pygame.image.load("Test image.png").convert_alpha()

# Size images
img_test2 = pygame.transform.scale(img_test2, (720, 400))
img_test1 = pygame.transform.scale(img_test1, (800, 425))

# Create colliders for the images
img_test2_rect = img_test2.get_rect(topleft=(0, 0))
img_test1_rect = img_test1.get_rect(topleft=(0, 0))



#game loop
menu = True
running = True
while running:

    # mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check events or something
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        #menu button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu:

                if play_button.collidepoint(event.pos):
                    menu = False
                
                if quit_button.collidepoint(event.pos):
                    running = False



    # Draw stuf
    screen.fill((40, 40, 40))
    
    #menu
    if menu:

        pygame.draw.rect(screen, (50,150,50), play_button)
        pygame.draw.rect(screen,(150,50,50), quit_button)

        play_text = font.render("PLAY", True, (255,255,255))
        quit_text = font.render("QUIT", True, (255,255,255))

        screen.blit(play_text, (350, 215))
        screen.blit(quit_text, (350, 335))

    else:
        pygame.draw.rect(screen, (80,50,50), (0,0, 0, 0))

        screen.blit(img_test2, img_test2_rect)
        screen.blit(img_test1, img_test1_rect)
        #mouse click thing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if img_test1_rect.collidepoint(mouse_pos):
                print("Image clicked!")

    # Change cursor when hovering
            if img_test1_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    


    pygame.display.flip()

    clock.tick(FPS)

#quit window 
pygame.quit()
sys.exit()