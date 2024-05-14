import sys
from random import randint
import pygame

pygame.init()

game_font = pygame.font.Font(None, 30)

screen_width: int = 800
screen_height: int = 600
screen_color: tuple = (31, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('My pygame Shooter')

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x: float = screen_width / 2 - fighter_width / 2
fighter_y: float = screen_height - fighter_height
fighter_is_moving_left: bool = False
fighter_is_moving_right: bool = False

STEP: float = 0.3

rocket_image = pygame.image.load('images/ball.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x: float = 0
rocket_y: float = 0
rocket_was_fired: bool = False

ROCKET_STEP: float = 0.3

alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x: float = randint(0, screen_width - alien_width)
alien_y: float = 0
alien_was_fired: bool = False
ALIEN_STEP: float = 0.05
alien_speed: float = ALIEN_STEP

game_is_running: bool = True
game_score: int = 0

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            elif event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            elif event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            elif event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= STEP:
        fighter_x -= STEP
    elif fighter_is_moving_right and fighter_x <= screen_width - fighter_width - STEP:
        fighter_x += STEP

    alien_y += alien_speed

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False
    elif rocket_was_fired:
        rocket_y -= ROCKET_STEP

    screen.fill(screen_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    screen.blit(alien_image, (alien_x, alien_y))

    game_score_text = game_font.render(f'Your score is: {game_score}', True, 'white')
    game_score_rectangle = game_score_text.get_rect()
    game_score_rectangle.center = (100, 20)
    screen.blit(game_score_text, game_score_rectangle)

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

    if rocket_was_fired and \
            alien_x < rocket_x < alien_x + alien_width - rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        alien_x = randint(0, screen_width - alien_width)
        alien_y = 0
        rocket_was_fired = False
        alien_speed += ALIEN_STEP / 2
        game_score += 1

game_over_text = game_font.render('Game Over', True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
