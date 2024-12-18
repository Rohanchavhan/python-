import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Running Game")

# Load car image
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(RED)

# Function to draw the car
def draw_car(x, y):
    screen.blit(car_image, (x, y))

# Function to create an obstacle
def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    return x, -OBSTACLE_HEIGHT

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    x = (SCREEN_WIDTH // 2) - (CAR_WIDTH // 2)
    y = SCREEN_HEIGHT - CAR_HEIGHT - 10
    obstacle_x, obstacle_y = create_obstacle()
    speed = 5
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - CAR_WIDTH:
            x += speed

        # Move the obstacle down
        obstacle_y += speed
        if obstacle_y > SCREEN_HEIGHT:
            obstacle_x, obstacle_y = create_obstacle()
            score += 1  # Increase score when obstacle is passed

        # Check for collision
        if (obstacle_y + OBSTACLE_HEIGHT > y) and (obstacle_x < x + CAR_WIDTH and obstacle_x + OBSTACLE_WIDTH > x):
            print(f"Game Over! Your score: {score}")
            running = False

        # Fill the screen with white
        screen.fill(WHITE)
        draw_car(x, y)

        # Draw the obstacle
        pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Update the display
        pygame.display.flip()
        clock.tick(30)  # Limit to 30 frames per second

    pygame.quit()

if __name__ == "__main__":
    game_loop()