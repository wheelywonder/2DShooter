import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

# define reusable colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)
grey = (101, 122, 160)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

# intialise and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter")
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
player = Player()
allSprites.add(player)

# Game Loop
running = True
while running:
    # keep game running at the FPS
    clock.tick(FPS)
    #  Events
#    for event in pygame.event.get():
        # check for quit
        #if event.type == pygame.QUIT:
            #running = False


    #  Update
allSprites.update()

    #  Render
screen.fill(black)
allSprites.draw(screen)


pygame.display.flip() # after rnder flip the display, for new rendering.

#pygame.quit()
