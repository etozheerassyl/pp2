import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Initial speed of enemies
SPEED = 5

# Initial scores and coin count
SCORE = 0
coin_count = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("street.jpg")

# Set up display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                0,
            )  # Randomize enemy position


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            0,
        )  # Randomize coin position
        self.weight = random.choice([1, 1, 1, 2, 2, 3])  # Assigning different weights to coins

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                0,
            )  # Reset coin position


P1 = Player()
E1 = Enemy()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Create a coin instance
coin = Coin()

# Sprite group for coins
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites.add(coin)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # Increase speed every second
            if coin_count >= 5:  # Check if player collected N coins
                SPEED += 1  # Increase speed additionally if N coins collected
                coin_count = 0  # Reset coin count

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))  # Draw background

    # Render and display score and coin count
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Coins: " + str(coin_count), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_text, (300, 10))

    # Draw and move sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision detection with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("death.mp3").play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision detection with coins
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 10
        coin_count += coin.weight  # Increase coin count based on weight
        coin.rect.top = 0
        coin.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            0,
        )  # Reset coin position

    pygame.display.update()
    FramePerSec.tick(FPS)
