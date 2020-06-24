# Pygame template - skeleton for new pygame projects - from www.kidscancode.com.
import pygame
import random
import os #commands to nagigate and manipulate file in OS

WIDTH = 800 # width of new game window
HEIGHT = 600 # height ------------
FPS = 30 # frames per second

# define Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  set up assets folders


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#define sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)# set background of rect to transparent
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
#tell sprite to move 5 pxels to the right on update every loop
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
# initialise pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game Loop
running = True
while running:
    #keep loop running at correct speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()


pygame.quit()
