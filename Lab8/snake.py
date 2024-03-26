import pygame
import sys
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
SNAKE_SIZE = 20
INITIAL_SPEED = 5
INCREMENT_SPEED = 0.5
FOOD_SIZE = 20
SCORE_PER_FOOD = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Snake:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if len(self.positions) > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.score + 1:
                self.positions.pop()

    def reset(self):
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(surface, GREEN, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def increase_speed(self):
        self.speed += INCREMENT_SPEED

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                         random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (FOOD_SIZE, FOOD_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Snake Game')

    snake = Snake()
    food = Food()

    while True:
        screen.fill(BLACK)

        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food.position:
            snake.score += 1
            if snake.score % 3 == 0:  
                snake.level += 1
                snake.increase_speed()
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)

        head_x, head_y = snake.get_head_position()
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            snake.reset()

        pygame.display.update()
        clock.tick(snake.speed)

if __name__ == '__main__':
    main()
