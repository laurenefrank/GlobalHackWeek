import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dual Player Ball Bounce")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball settings
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5
ball_dir = 1  # 1 = right, -1 = left

# Player settings
player1_x = 50
player2_x = WIDTH - 50
player_y = HEIGHT // 2
player_radius = 30

font = pygame.font.SysFont(None, 36)

def draw():
    screen.fill(WHITE)
    # Draw players
    pygame.draw.circle(screen, BLACK, (player1_x, player_y), player_radius)
    pygame.draw.circle(screen, BLACK, (player2_x, player_y), player_radius)
    # Draw ball
    pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)
    pygame.display.flip()

def show_message(msg):
    text = font.render(msg, True, (255, 0, 0))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(2000)

turn = 1  # 1 = Player 1, 2 = Player 2
running = True

while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Player 1 bounce
            if turn == 1 and event.key == pygame.K_a:
                if abs(ball_x - player1_x) < player_radius + ball_radius:
                    ball_dir = 1
                    ball_speed += 1
                    turn = 2
                else:
                    show_message("Player 2 Wins!")
                    running = False
            # Player 2 bounce
            elif turn == 2 and event.key == pygame.K_l:
                if abs(ball_x - player2_x) < player_radius + ball_radius:
                    ball_dir = -1
                    ball_speed += 1
                    turn = 1
                else:
                    show_message("Player 1 Wins!")
                    running = False

    # Move ball
    ball_x += ball_dir * ball_speed

    # Check for out of bounds
    if ball_x < 0:
        show_message("Player 2 Wins!")
        running = False
    elif ball_x > WIDTH:
        show_message("Player 1 Wins!")
        running = False

    pygame.time.delay(30)

pygame.quit()
sys.exit()