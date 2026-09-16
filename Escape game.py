# Load images
img_test2 = pygame.image.load("eat.png").convert_alpha()
img_test1 = pygame.image.load("Test image.png").convert_alpha()

# Size images
img_test2 = pygame.transform.scale(img_test2, (720, 350))
img_test1 = pygame.transform.scale(img_test1, (720, 400))

# Create colliders for the images
img_test2_rect = img_test2.get_rect(topleft=(280, 75))
img_test1_rect = img_test1.get_rect(topleft=(280, 30))
