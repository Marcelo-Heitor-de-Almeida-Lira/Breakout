import pygame
from random import randint
from random import randrange
from menu import Button

# Init pygame
pygame.init()

# Define some colors key
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Define points
score = 0
lives = 3

# Open a new window
size = (625, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BREAKOUT - PYGAME EDITION')

# Game sound
volume = 0.3
bounce_sound = pygame.mixer.Sound(
                                  'venv/Scripts/Assets/bounce.wav')
scoring_sound = pygame.mixer.Sound(
                                   'venv/Scripts/Assets/point.wav')
pygame.mixer.music.set_volume(0.3)
scoring_sound.set_volume(volume)


# Create paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveleft(self, pixels):
        self.rect.x -= pixels
        # Check that you are not going too far
        if self.rect.x < 15:
            self.rect.x = 15

    def moveright(self, pixels):
        self.rect.x += pixels
        # Check that you are not going too far
        if self.rect.x > 510:
            self.rect.x = 510

# Create the Ball


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Velocity ball random
        self.velocity = [randint(4, 8), randint(1, 8)]

        # Creat a cube to ball
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randrange(-8, 8, 3)


# Create the Brick
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        return


def menu():
    start_button = Button(30, 150, RED)
    start_button.rect.x = 240
    start_button.rect.y = 450

    credit_button = Button(30, 150, ORANGE)
    credit_button.rect.x = 240
    credit_button.rect.y = 500

    exit_button = Button(30, 150, GREEN)
    exit_button.rect.x = 240
    exit_button.rect.y = 550

    tittle_font = pygame.font.Font(
                              'venv/Scripts/Assets/AtariST8x16SystemFont.ttf',
                              130)
    menu_font = pygame.font.Font(
                            'venv/Scripts/Assets/AtariST8x16SystemFont.ttf',
                            30)
    credit_font = pygame.font.Font(
        'venv/Scripts/Assets/AtariST8x16SystemFont.ttf',
        20)

    pygame.display.flip()
    run = True

    while run:

        screen.fill(BLACK)
        menu_text = tittle_font.render("BREAKOUT", 1, WHITE)
        screen.blit(menu_text, (55, 250))

        if start_button.draw(screen):
            scoring_sound.play()
            return 'start_game'

        if credit_button.draw(screen):
            scoring_sound.play()
            haa = True
            while haa:
                screen.fill(BLACK)
                menu_text = menu_font.render("Laboratório e Programação de Computadores", 1, WHITE)
                screen.blit(menu_text, (5, 250))
                menu_text = credit_font.render("Desenvolvido por:", 1, WHITE)
                screen.blit(menu_text, (55, 350))
                menu_text = credit_font.render("Bianca Garcia, Marcelo Lira e Marcio Júnior", 1, WHITE)
                screen.blit(menu_text, (55, 370))
                for event in pygame.event.get():
                    # quit game
                    if event.type == pygame.QUIT:
                        haa = False

                pygame.display.update()

        if exit_button.draw(screen):
            return 'exit_game'

        start_text = menu_font.render("PLAY", 1, WHITE)
        screen.blit(start_text, (290, 450))

        start_text = menu_font.render("CREDITS", 1, WHITE)
        screen.blit(start_text, (265, 500))

        exit_text = menu_font.render("EXIT", 1, WHITE)
        screen.blit(exit_text, (290, 550))
        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


# Paddle settings
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 250
paddle.rect.y = 670

# Ball settings
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 300

# Bricks settings
all_bricks = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list_yellow = pygame.sprite.Group()
all_sprites_list_green = pygame.sprite.Group()
all_sprites_list_orange = pygame.sprite.Group()
all_sprites_list_red = pygame.sprite.Group()

# Create bricks to colors
for i in range(14):
    brick = Brick(RED, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 160
    all_sprites_list_red.add(brick)
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(RED, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 175
    all_sprites_list_red.add(brick)
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(ORANGE, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 190
    all_sprites_list_orange.add(brick)
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(ORANGE, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 205
    all_sprites_list_orange.add(brick)
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(GREEN, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 220
    all_sprites_list_green.add(brick)
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(GREEN, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 235
    all_sprites_list.add(brick)
    all_sprites_list_green.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(YELLOW, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 250
    all_sprites_list.add(brick)
    all_sprites_list_yellow.add(brick)
    all_bricks.add(brick)

for i in range(14):
    brick = Brick(YELLOW, 37.5, 10)
    brick.rect.x = 20 + i * 42.5
    brick.rect.y = 265
    all_sprites_list.add(brick)
    all_sprites_list_yellow.add(brick)
    all_bricks.add(brick)

# Add the paddle and the ball to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# The loop will carry on until the user exits the game
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

game_state = "menu"
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    if game_state == "menu":
        game_state = menu()
    elif game_state == "start_game":
        while carryOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False
            # Moving the paddle when the use uses the arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.moveleft(8)
            if keys[pygame.K_RIGHT]:
                paddle.moveright(8)
            # --- Game logic should go here
            all_sprites_list.update()
            # Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x >= 595:
                ball.velocity[0] = -ball.velocity[0]
                bounce_sound.play()

            if ball.rect.x <= 15:
                ball.velocity[0] = -ball.velocity[0]
                bounce_sound.play()

            if ball.rect.y > 670:
                ball.rect.x = 345
                ball.rect.y = 300
                lives -= 1
                if lives == 0:
                    # Display Game Over Message for 3 seconds
                    font = pygame.font.Font(
                                            'venv/Scripts/Assets/'
                                            'AtariST8x16SystemFont.ttf', 74)
                    text = font.render("GAME OVER", 1, WHITE)
                    screen.blit(text, (150, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    # Stop the Game
                    carryOn = False
            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]
            # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddle):
                ball.rect.x -= ball.velocity[0]
                ball.rect.y -= ball.velocity[1]
                ball.bounce()
            # Check if there is the ball collides with any of bricks
            brick_collision_list = pygame.sprite.spritecollide(
                ball, all_bricks, False)
            brick_collision_list_yellow = pygame.sprite.spritecollide(
                ball, all_sprites_list_yellow, False)
            brick_collision_list_green = pygame.sprite.spritecollide(
                ball, all_sprites_list_green, False)
            brick_collision_list_orange = pygame.sprite.spritecollide(
                ball, all_sprites_list_orange, False)
            brick_collision_list_red = pygame.sprite.spritecollide(
                ball, all_sprites_list_red, False)

            for brick in brick_collision_list_yellow:
                ball.bounce()
                score += 1
                scoring_sound.play()
                brick.kill()

            for brick in brick_collision_list_green:
                ball.bounce()
                score += 3
                scoring_sound.play()
                brick.kill()

            for brick in brick_collision_list_orange:
                ball.bounce()
                score += 5
                scoring_sound.play()
                brick.kill()

            for brick in brick_collision_list_red:
                ball.bounce()
                score += 7
                scoring_sound.play()
                brick.kill()

                if len(all_bricks) == 0:
                    # Display Level Complete Message for 3 seconds
                    font = pygame.font.Font(
                                            'venv/Scripts/Assets/'
                                            'AtariST8x16SystemFont.ttf', 74)
                    text = font.render("LEVEL COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    # Stop the Game
                    carryOn = False
            # --- Drawing code should go here
            # First, clear the screen to dark blue.

            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK,
                             [15, 30, 595, 770])
            pygame.draw.rect(screen, WHITE,
                             [340, 30, 10, 70])
            # Display the score and the number of lives
            font = pygame.font.Font(
                                    'venv/Scripts/Assets/'
                                    'AtariST8x16SystemFont.ttf', 70)
            if score < 10:
                text = font.render("00"+str(score), 1, WHITE)
                screen.blit(text, (350, 90))
            elif score <= 99:
                text = font.render("0" + str(score), 1, WHITE)
                screen.blit(text, (350, 90))
            else:
                text = font.render(str(score), 1, WHITE)
                screen.blit(text, (350, 90))
            text = font.render("Lives: " + str(lives), 1, WHITE)
            screen.blit(text, (650, 10))
            # Draw sprites
            all_sprites_list.draw(screen)
            # Update screen
            pygame.display.flip()
            # Limit to 60 frames per second
            clock.tick(60)
        game_state = "playing"
    elif game_state == "exit_game":
        carryOn = False
# Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
