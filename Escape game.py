import pygame
import sys
import time

# Type python "Escape game.py" in terminal to open

pygame.init()

# Game setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game")

# Game state
room = 1
inventory = []

# Text font
font = pygame.font.SysFont(None, 50)

# Buttons
play_button = pygame.Rect(300, 200, 200, 70)
quit_button = pygame.Rect(300, 320, 200, 70)

skip_button = pygame.Rect(716, 550, 80, 40)

# Caps frames to 60
clock = pygame.time.Clock()
FPS = 60

# Room transition
fade_alpha = 0
fading = False
fade_speed = 15

# Click cooldown
last_click_time = 0
CLICK_COOLDOWN = 500  # milliseconds


# Loads images
# Story images
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
Room1 = pygame.image.load("Room1.png").convert_alpha()
Room2 = pygame.image.load("Room2.png").convert_alpha()
Room3 = pygame.image.load("Room3.png").convert_alpha()
Room4 = pygame.image.load("Room4.png").convert_alpha()
Room_left1 = pygame.image.load("Room_left1.png").convert_alpha()
Room_right1 = pygame.image.load("Room_right1.png").convert_alpha()

#clickable images
BackUI = pygame.image.load("BackUI.png").convert_alpha()
BackUI_Text = pygame.image.load("BackUI_Text.png").convert_alpha()


# Sizes images
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
Room1 = pygame.transform.scale(Room1, (800, 425))
Room2 = pygame.transform.scale(Room2, (800, 425))
Room3 = pygame.transform.scale(Room3, (800, 425))
Room4 = pygame.transform.scale(Room4, (800, 425))
Room_left1 = pygame.transform.scale(Room_left1, (800, 425))
Room_right1 = pygame.transform.scale(Room_right1, (800, 425))

#clickable images
BackUI = pygame.transform.scale(BackUI, (825, 100))
BackUI_Text = pygame.transform.scale(BackUI_Text, (200, 35))


# Create position and colliders for images
#game images
Room1_rect = Room1.get_rect(topleft=(0, 0))
Room2_rect = Room2.get_rect(topleft=(0, 0))
Room3_rect = Room3.get_rect(topleft=(0, 0))
Room4_rect = Room4.get_rect(topleft=(0, 0))
Room_left1_rect = Room_left1.get_rect(topleft=(0, 0))
Room_right1_rect = Room_right1.get_rect(topleft=(0, 0))

#clickable images
BackUI_rect = BackUI.get_rect(topleft=(-15, 353))
BackUI_Text_rect = BackUI_Text.get_rect(topleft=(315, 390))


# Cutscene images and how long they show for
cutscene = [
    (Story1, 2),
    (Story2, 1),
    (Story3, 1),
    (Story4, 1),
    (Story5, 1),
    (Story6, 1),
    (Story7, 1),
    (Story8, 1),
    (Story9, 0.5),
    (Story10, 0.5),
    (Story11, 0.5),
    (Story12, 0.25),
    (Story13, 0.5),
    (Story14, 1),
    (Story15, 1),
    (Story16, 1),
    (Story17, 1),
    (Story18, 0.4),
    (Story19, 0.4),
    (Story20, 0.4),
    (Story21, 0.4),
    (Story22, 0.4),
    (Story23, 0.4),
    (Story24, 0.4),
    (Story25, 0.4),
    (Story26, 0.4),
    (Story27, 0.7),
    (Story28, 0.5),
    (Story29, 0.5),
    (Story30, 0.5),
    (Story31, 0.5),
    (Story32, 0.5),
    (Story33, 0.5),
    (Story34, 0.5),
    (Story35, 0.5),
    (Story36, 0.5),
    (Story37, 0.5),
    (Story38, 0.5),
    (Story39, 0.5),
    (Story40, 0.5),
    (Story41, 0.5),
    (Story42, 0.5),
    (Story43, 0.5),
    (Story44, 0.7),
    (Story45, 0.7),
    (Story46, 0.7),
    (Story47, 0.7),
    (Story48, 0.7),
    (Story49, 0.7),
    (Story50, 0.7),
    (Story51, 0.7),
    (Story52, 0.2),
    (Story53, 0.2),
    (Story54, 0.2),
    (Story55, 1),
    (Story56, 1),
    (Story57, 0.2),
    (Story58, 0.2),
    (Story59, 0.2),
    (Story60, 0.2),
]

current_slide = 0
start_time = pygame.time.get_ticks()

# Room 1 door to Room 2
door_point1 = [
    (384, 165), #Top left
    (418, 165), #Top right
    (417, 228), #Bottom right
    (383, 232)  #Bottom left
]

# Room 2 door to Room 3
door_point2 = [
    (584, 58),
    (666, 39),
    (645, 244),
    (570, 233)
]

# Room 2 door to Room 4
door_point3 = [
    (81, 80),
    (209, 98),
    (216, 213),
    (98, 219)
]

door_point4 = [
    (243, 1),
    (310, 84),
    (310, 253),
    (259, 328)
]

door_point5 = [
    (501, 87),
    (543, 2),
    (527, 324),
    (490, 252)
]


# Check if mouse is inside a polygon
def point_in_polygon(point, polygon):

    x, y = point
    inside = False

    j = len(polygon) - 1

    for i in range(len(polygon)):

        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if ((yi > y) != (yj > y)) and \
           (x < (xj - xi) * (y - yi) / (yj - yi) + xi):

            inside = not inside

        j = i

    return inside


#fade in and out transition between game states
def fade_to_room(new_room):

    global room

    # Fade out
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0, 0, 0))

    for alpha in range(0, 256, fade_speed):
        fade.set_alpha(alpha)

        screen.blit(fade, (0, 0))
        pygame.display.flip()

        clock.tick(FPS)

    # Change room while screen is black
    room = new_room

    # Fade in
    for alpha in range(255, -1, -fade_speed):
        fade.set_alpha(alpha)

        # Draw the new room
        if room == 1:
            screen.blit(Room1, Room1_rect)

        elif room == 2:
            screen.blit(Room2, Room2_rect)
            screen.blit(BackUI, BackUI_rect)
            screen.blit(BackUI_Text, BackUI_Text_rect)

        elif room == 3:
            screen.blit(Room3, Room3_rect)
            screen.blit(BackUI, BackUI_rect)
            screen.blit(BackUI_Text, BackUI_Text_rect)

        elif room == 4:
            screen.blit(Room4, Room4_rect)
            screen.blit(BackUI, BackUI_rect)
            screen.blit(BackUI_Text, BackUI_Text_rect)

        elif room == 5:
            screen.blit(Room_left1, Room_left1_rect)
            screen.blit(BackUI, BackUI_rect)
            screen.blit(BackUI_Text, BackUI_Text_rect)    

        elif room == 6:
            screen.blit(Room_right1, Room_right1_rect)
            screen.blit(BackUI, BackUI_rect)
            screen.blit(BackUI_Text, BackUI_Text_rect)          


        screen.blit(fade, (0, 0))
        pygame.display.flip()

        clock.tick(FPS)


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
            print(event.pos)

            if menu:

                if play_button.collidepoint(event.pos):
                    menu = False

                if quit_button.collidepoint(event.pos):
                    running = False


    # Change cursor for menu buttons
    if menu:

        if play_button.collidepoint(mouse_pos) or quit_button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    else:
    # Move to the next image after its timer
        if current_slide < len(cutscene):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            image, duration = cutscene[current_slide]

            if duration is not None:
                if current_time - start_time >= duration * 1000:
                    current_slide += 1
                    start_time = current_time


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


    # Cutscene occuring after pressing play
    else:
         if current_slide < len(cutscene):
            image, duration = cutscene[current_slide]
            screen.blit(image, (0, 0))

            pygame.draw.rect(screen, (60, 60, 60), skip_button)

            skip_text = font.render("SKIP", True, (255, 255, 255))
            screen.blit(skip_text, (718, 550))

        # Skip button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if skip_button.collidepoint(event.pos):
                    current_slide = len(cutscene)

    # Change cursor when hovering over skip
                if skip_button.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # The actual game thing after cutscene finishes
         else:

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                #check cooldown
                if current_time - last_click_time >= CLICK_COOLDOWN:

                    #Room1
                    if room == 1:

                        if point_in_polygon(event.pos, door_point1):
                            last_click_time = current_time
                            fade_to_room(2)

                    #Room2
                    elif room == 2:

                        #door to room3
                        if point_in_polygon(event.pos, door_point2):
                            last_click_time = current_time
                            fade_to_room(3)
                        
                        #door to room4
                        elif point_in_polygon(event.pos, door_point3):
                            last_click_time = current_time
                            fade_to_room(4)

                        #Back button
                        elif BackUI_rect.collidepoint(event.pos):
                            last_click_time = current_time
                            fade_to_room(1)

                    #Room3
                    elif room == 3:
                        
                        if BackUI_rect.collidepoint(event.pos):
                            last_click_time = current_time
                            fade_to_room(2)

                    #room4
                    elif room == 4:

                        #door to room3
                        if point_in_polygon(event.pos, door_point4):
                            last_click_time = current_time
                            fade_to_room(5)
                        
                        #door to room4
                        elif point_in_polygon(event.pos, door_point5):
                            last_click_time = current_time
                            fade_to_room(6)

                        #Back button
                        elif BackUI_rect.collidepoint(event.pos):
                            last_click_time = current_time
                            fade_to_room(4)


                    elif room == 5:
                        if BackUI_rect.collidepoint(event.pos):
                            last_click_time = current_time
                            fade_to_room(4)                        

                    elif room == 6:
                        if BackUI_rect.collidepoint(event.pos):
                            last_click_time = current_time
                            fade_to_room(4)   

               #click to go to other rooms
                elif room == 2:

                    #door to room3
                    if point_in_polygon(event.pos, door_point2):
                        room = 3
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    
                    #door to room4
                    elif point_in_polygon(event.pos, door_point3):
                        room = 4
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                    #back to room1
                    elif BackUI_rect.collidepoint(event.pos):
                        room = 1

                #room3
                elif room == 3:
                    if BackUI_rect.collidepoint(event.pos):
                        room = 2
                       
                
                elif room == 4:
                    #door to room_left1
                    if point_in_polygon(event.pos, door_point4):
                        room = 5
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    
                    #door to room_right1
                    elif point_in_polygon(event.pos, door_point5):
                        room = 6
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                    #back to room1
                    elif BackUI_rect.collidepoint(event.pos):
                        room = 2
                    

                elif room == 5:
                    if BackUI_rect.collidepoint(event.pos):
                        room = 4


                elif room == 6:
                    if BackUI_rect.collidepoint(event.pos):
                        room = 4


# change cursor when hovering over an interactable object

            #room collidepoints
            if room == 1:
                if point_in_polygon(mouse_pos, door_point1):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            elif room == 2:
                if (BackUI_rect.collidepoint(mouse_pos)
                    or point_in_polygon(mouse_pos, door_point2)
                    or point_in_polygon(mouse_pos, door_point3)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            elif room == 3:
                if BackUI_rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)      

            elif room == 4:
                if (BackUI_rect.collidepoint(mouse_pos)
                    or point_in_polygon(mouse_pos, door_point4)
                    or point_in_polygon(mouse_pos, door_point5)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)    

            elif room == 5:
                if BackUI_rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  

            elif room == 6:
                if BackUI_rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  
                                              

           # Display images
            if room == 1:
               screen.blit(Room1, Room1_rect)

            elif room ==2:
               screen.blit(Room2, Room2_rect)
               screen.blit(BackUI, BackUI_rect)
               screen.blit(BackUI_Text, BackUI_Text_rect)

            elif room == 3:
                screen.blit(Room3, Room3_rect)
                screen.blit(BackUI, BackUI_rect)
                screen.blit(BackUI_Text, BackUI_Text_rect)

            elif room == 4:
                screen.blit(Room4, Room4_rect)
                screen.blit(BackUI, BackUI_rect)
                screen.blit(BackUI_Text, BackUI_Text_rect)
                pygame.draw.polygon(
                   screen,
                   (255, 0, 0),
                   door_point4,
                   2
               )

                pygame.draw.polygon(
                screen,
                (0, 255, 0),
                door_point5,
                2
               )

            elif room == 5:
                screen.blit(Room_left1, Room_left1_rect)
                screen.blit(BackUI, BackUI_rect)
                screen.blit(BackUI_Text, BackUI_Text_rect)              

            elif room == 6:
                screen.blit(Room_right1, Room_right1_rect)
                screen.blit(BackUI, BackUI_rect)
                screen.blit(BackUI_Text, BackUI_Text_rect)             


    pygame.display.flip()
    clock.tick(FPS)

# Exit smoothly code
pygame.quit()
sys.exit()