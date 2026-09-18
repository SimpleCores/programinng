import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point and Click Adventure")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 150, 250)
GOLD = (255, 215, 0)

# Game State
current_scene = "room1"
inventory = []
message_text = "Look around the room. Click on objects to interact."

# Font Configuration
font = pygame.font.SysFont(None, 28)

class Clickable:
    """Class to manage interactive objects, items, and navigation zones."""
    def __init__(self, name, rect, action, action_arg=None):
        self.name = name
        self.rect = pygame.Rect(rect)  # (x, y, width, height)
        self.action = action           # Type of interaction: "collect", "move", "examine"
        self.action_arg = action_arg   # Destination room name or custom string info

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Define Interactive Scene Elements
# In a full game, you would replace rectangles with images/sprites.
scene_objects = {
    "room1": [
        Clickable("Rusty Key", (200, 400, 50, 30), "collect"),
        Clickable("Heavy Door", (550, 200, 120, 250), "move", "room2")
    ],
    "room2": [
        Clickable("Treasure Chest", (350, 350, 100, 80), "examine", "It requires a rusty key to unlock."),
        Clickable("Go Back", (5, 550, 100, 40), "move", "room1")
    ]
}

def draw_ui():
    """Renders the message bar and inventory slot UI."""
    # Bottom HUD panel boundary
    pygame.draw.rect(screen, GRAY, (0, 500, SCREEN_WIDTH, 100))
    
    # Text notification system
    txt_surface = font.render(message_text, True, BLACK)
    screen.blit(txt_surface, (20, 515))
    
    # Inventory displays
    inv_title = font.render("Inventory:", True, BLACK)
    screen.blit(inv_title, (550, 515))
    
    for i, item in enumerate(inventory):
        item_text = font.render(f"[{item}]", True, BLUE)
        screen.blit(item_text, (550 + (i * 100), 550))

# Core Game Loop
while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left Click
            # Check collisions with interactive hotspots in current scene
            for obj in scene_objects[current_scene][:]:
                if obj.check_click(mouse_pos):
                    
                    if obj.action == "collect":
                        inventory.append(obj.name)
                        scene_objects[current_scene].remove(obj) # Remove from world view
                        message_text = f"You picked up the {obj.name}."
                        
                    elif obj.action == "move":
                        current_scene = obj.action_arg
                        message_text = f"You entered {current_scene.capitalize()}."
                        
                    elif obj.action == "examine":
                        if "Rusty Key" in inventory and obj.name == "Treasure Chest":
                            message_text = "You unlock the chest and win the game!"
                        else:
                            message_text = obj.action_arg
                    break # Stop checking other elements after successful click

    # --- Rendering Layer ---
    screen.fill(BLACK) # Clear frame

    # Draw Scene Environments
    if current_scene == "room1":
        # Draw background floor/walls placeholders
        pygame.draw.rect(screen, (80, 50, 50), (0, 0, SCREEN_WIDTH, 500)) 
        # Render scene entities (Key & Door)
        for obj in scene_objects["room1"]:
            if obj.name == "Rusty Key":
                pygame.draw.rect(screen, GOLD, obj.rect)
            elif obj.name == "Heavy Door":
                pygame.draw.rect(screen, BLACK, obj.rect)
                
    elif current_scene == "room2":
        pygame.draw.rect(screen, (50, 80, 50), (0, 0, SCREEN_WIDTH, 500))
        # Render scene entities (Chest & Back Button)
        for obj in scene_objects["room2"]:
            if obj.name == "Treasure Chest":
                pygame.draw.rect(screen, (139, 69, 19), obj.rect)
            elif obj.name == "Go Back":
                pygame.draw.rect(screen, GRAY, obj.rect)

    # Draw Text Labels overlaying items if hovered
    for obj in scene_objects[current_scene]:
        if obj.rect.collidepoint(mouse_pos):
            label = font.render(obj.name, True, WHITE)
            screen.blit(label, (mouse_pos[0] + 12, mouse_pos[1] - 12))

    # Render User Interface
    draw_ui()

    pygame.display.flip()
    clock.tick(60)
