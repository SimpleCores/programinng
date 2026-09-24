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

# Fade and click settings
FADE_SPEED = 15
CLICK_COOLDOWN = 500  # milliseconds
last_room_change = 0


# Load room images
room1 = pygame.image.load("Block.png").convert()
room2 = pygame.image.load("Black Border.png").convert()
room3 = pygame.image.load("Room3.png").convert()

# Load objects
key_image = pygame.image.load("eat.png").convert_alpha()
door_image = pygame.image.load("Test image.png").convert_alpha()
chest_image = pygame.image.load("Story2.png").convert_alpha()
back_image = pygame.image.load("Story1.png").convert_alpha()


# Resize room images
room1 = pygame.transform.scale(room1, (800, 600))
room2 = pygame.transform.scale(room2, (800, 600))
room3 = pygame.transform.scale(room3, (800, 600))

# Resize objects
key_image = pygame.transform.scale(key_image, (50, 30))
door_image = pygame.transform.scale(door_image, (120, 250))
chest_image = pygame.transform.scale(chest_image, (100, 80))
back_image = pygame.transform.scale(back_image, (100, 40))


# Image positions
key_rect = key_image.get_rect(topleft=(200, 400))
door_rect = door_image.get_rect(topleft=(550, 200))
chest_rect = chest_image.get_rect(topleft=(350, 350))
back_rect = back_image.get_rect(topleft=(5, 550))


# -------------------------
# CUSTOM DOOR CLICK AREAS
# -------------------------

# Room 1 door → Room 2
door_points = [
    (280, 200),
    (660, 200),
    (660, 450),
    (560, 450)
]

# Room 3 door → Room 1
room3_door_points = [
    (560, 200),
    (660, 200),
    (660, 450),
    (560, 450)
]


# -------------------------
# CHECK IF POINT IS IN POLYGON
# -------------------------

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


# -------------------------
# FADE TRANSITION
# -------------------------

def fade_transition(new_room):

    global room

    fade = pygame.Surface((800, 600))
    fade.fill((0, 0, 0))

    # Fade OUT
    for alpha in range(0, 256, FADE_SPEED):

        fade.set_alpha(alpha)

        # Draw the current room
        if room == 1:
            screen.blit(room1, (0, 0))

        elif room == 2:
            screen.blit(room2, (0, 0))
            screen.blit(chest_image, chest_rect)
            screen.blit(back_image, back_rect)

        elif room == 3:
            screen.blit(room3, (0, 0))
            screen.blit(back_image, back_rect)

        screen.blit(fade, (0, 0))

        pygame.display.flip()
        clock.tick(60)


    # Change room while screen is black
    room = new_room


    # Fade IN
    for alpha in range(255, -1, -FADE_SPEED):

        fade.set_alpha(alpha)

        # Draw the new room
        if room == 1:
            screen.blit(room1, (0, 0))
            screen.blit(door_image, door_rect)

            if key_rect:
                screen.blit(key_image, key_rect)

        elif room == 2:
            screen.blit(room2, (0, 0))
            screen.blit(chest_image, chest_rect)
            screen.blit(back_image, back_rect)

        elif room == 3:
            screen.blit(room3, (0, 0))
            screen.blit(back_image, back_rect)

        screen.blit(fade, (0, 0))

        pygame.display.flip()
        clock.tick(60)


# -------------------------
# GAME LOOP
# -------------------------

running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            current_time = pygame.time.get_ticks()

            # Check cooldown
            if current_time - last_room_change >= CLICK_COOLDOWN:

                # -------------------------
                # ROOM 1
                # -------------------------

                if room == 1:

                    # Pick up key
                    if key_rect and key_rect.collidepoint(event.pos):
                        inventory.append("Rusty Key")
                        key_rect = None


                    # Door → Room 2
                    elif point_in_polygon(event.pos, door_points):

                        last_room_change = current_time
                        fade_transition(2)


                # -------------------------
                # ROOM 2
                # -------------------------

                elif room == 2:

                    # Chest → Room 3
                    if chest_rect.collidepoint(event.pos):

                        if "Rusty Key" in inventory:
                            last_room_change = current_time
                            fade_transition(3)

                        else:
                            print("The chest is locked.")


                    # Back → Room 1
                    elif back_rect.collidepoint(event.pos):

                        last_room_change = current_time
                        fade_transition(1)


                # -------------------------
                # ROOM 3
                # -------------------------

                elif room == 3:

                    # Back → Room 2
                    if back_rect.collidepoint(event.pos):

                        last_room_change = current_time
                        fade_transition(2)


                    # Door → Room 1
                    elif point_in_polygon(
                        event.pos,
                        room3_door_points
                    ):

                        last_room_change = current_time
                        fade_transition(1)


    # -------------------------
    # CHANGE CURSOR
    # -------------------------

    if room == 1:

        if point_in_polygon(mouse_pos, door_points):

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_HAND
            )

        else:

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_ARROW
            )


    elif room == 2:

        if (
            chest_rect.collidepoint(mouse_pos)
            or back_rect.collidepoint(mouse_pos)
        ):

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_HAND
            )

        else:

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_ARROW
            )


    elif room == 3:

        if (
            back_rect.collidepoint(mouse_pos)
            or point_in_polygon(
                mouse_pos,
                room3_door_points
            )
        ):

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_HAND
            )

        else:

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_ARROW
            )


    # -------------------------
    # DRAW ROOM 1
    # -------------------------

    if room == 1:

        screen.blit(room1, (0, 0))
        screen.blit(door_image, door_rect)

        if key_rect:
            screen.blit(key_image, key_rect)

        # Show clickable door area
        pygame.draw.polygon(
            screen,
            (255, 0, 0),
            door_points,
            2
        )


    # -------------------------
    # DRAW ROOM 2
    # -------------------------

    elif room == 2:

        screen.blit(room2, (0, 0))
        screen.blit(chest_image, chest_rect)
        screen.blit(back_image, back_rect)


    # -------------------------
    # DRAW ROOM 3
    # -------------------------

    elif room == 3:

        screen.blit(room3, (0, 0))
        screen.blit(back_image, back_rect)

        # Show clickable door area
        pygame.draw.polygon(
            screen,
            (255, 0, 0),
            room3_door_points,
            2
        )


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()