# Imports
import colors
import intersects
import random
import os
import pygame

from alien import Bug, Scrubby, TieFighter, UFO
from background import Ground, Mountains, Stars
from bomb import Bomb
from bullet import Bullet
from bunker import Bunker
from cannon import Cannon

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "15, 30:"


# Initialize game engine
pygame.init()


# Window
SIZE = (1000, 660)
TITLE = "Block Invaders"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Sounds
SHOT = pygame.mixer.Sound("sounds/shot.ogg")
HIT = pygame.mixer.Sound("sounds/hit.ogg")
CLANK = pygame.mixer.Sound("sounds/clank.ogg")
THEME = pygame.mixer.Sound("sounds/take_a_chance.ogg")

# Fonts
big_font = pygame.font.Font("fonts/joystix monospace.ttf", 70)
font = pygame.font.Font("fonts/joystix monospace.ttf", 30)

# Data
score_file = "data/scores.txt"

# Stages
START = 0
PLAYING = 1
PAUSED = 2
CLEAR = 3
DIE = 4
GAME_OVER = 5


# Settings
starting_bomb_rate = 2
bomb_rate_increase = 1
shot_limit = 3
cannon_speed = 4
bullet_speed = 6
alien_speed = 2
bomb_speed = 3
extra_life_points = 1000 # then at 2000, 4000, 8000, ...
sound_on = True
default_high_score = 2000

# Make background objects
ground = Ground(0, 560, 1000, 5)
mountains = Mountains(0, 480, 1000, 80, 9)
stars = Stars(0, 0, 1000, 560, 125)

def reset_cannon():
    cannon.x = 480

def start():
    global  score, lives, level, stage, bomb_rate, cannon
    bomb_rate = starting_bomb_rate

    score = 0
    lives = 3
    level = 1
    stage = START

    cannon = Cannon(480, 530)
    setup()


def setup():
    global aliens, bombs, bullets, bunkers, hits, shots, ufos

    aliens = []

    a1 = TieFighter(230, 90)
    a2 = TieFighter(330, 90)
    a3 = TieFighter(430, 90)
    a4 = TieFighter(530, 90)
    a5 = TieFighter(630, 90)
    a6 = TieFighter(730, 90)
    a7 = Bug(230, 160)
    a8 = Bug(330, 160)
    a9 = Bug(430, 160)
    a10 = Bug(530, 160)
    a11 = Bug(630, 160)
    a12 = Bug(730, 160)
    a13 = Scrubby(230, 240)
    a14 = Scrubby(330, 240)
    a15 = Scrubby(430, 240)
    a16 = Scrubby(530, 240)
    a17 = Scrubby(630, 240)
    a18 = Scrubby(730, 240)

    tie_fighters = [a1, a2, a3, a4, a5, a6]
    bugs = [a7, a8, a9, a10, a11, a12]
    scrubbies = [a13, a14, a15, a16, a17, a18]

    aliens = tie_fighters + bugs + scrubbies

    for a in aliens:
        a.v_x = alien_speed

    ufo_x = random.randrange(3000, 10000)
    ufos = [UFO(ufo_x, 60)]

    b1 = Bunker(200, 400)
    b2 = Bunker(460, 400)
    b3 = Bunker(720, 400)
    bunkers = [b1, b2, b3]

    bombs = []
    bullets = []

    hits = 0
    shots = 0


def get_high_score():
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            return max([int(f.read().strip()), default_high_score])
    else:
        return default_high_score


def update_high_score():
    if not os.path.exists('data'):
        os.mkdir('data')

    with open((score_file), 'w') as f:
        f.write(str(high_score))


# hide mouse cursor over screen
pygame.mouse.set_visible(0)


# Game loop
done = False
high_score = get_high_score()
start()

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING

                    if sound_on:
                        THEME.play(-1)

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE and len(bullets) < shot_limit:
                    x = cannon.x + cannon.width // 2 - 3
                    y = cannon.y
                    b = Bullet(x, y)
                    b.v_y = -bullet_speed
                    bullets.append(b)
                    shots += 1

                    if sound_on:
                        SHOT.play()
                elif event.key == pygame.K_p:
                    stage = PAUSED

            elif stage == PAUSED:
                if event.key == pygame.K_p:
                    stage = PLAYING

            elif stage == DIE:
                if event.key == pygame.K_SPACE:
                    bombs = []
                    bullets = []
                    reset_cannon()
                    stage = PLAYING

            elif stage == CLEAR and bonus == 0:
                if event.key == pygame.K_SPACE:
                    level += 1
                    bomb_rate += bomb_rate_increase
                    setup()
                    stage = PLAYING

            elif stage == GAME_OVER:
                if event.key == pygame.K_r:
                    start()

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            cannon.v_x = cannon_speed
        elif key[pygame.K_LEFT]:
            cannon.v_x = -cannon_speed
        else:
            cannon.v_x = 0


    # Game logic
    if stage == PLAYING:
        ''' move cannon '''
        cannon.move()

        if cannon.x < 0:
            cannon.x = 0
        elif cannon.x > 1000 - cannon.width:
            cannon.x = 1000 - cannon.width

        ''' move bullets '''
        for b in bullets:
            b.move()

        ''' move bad guys '''
        on_edge = False

        for a in aliens:
            if a.v_x < 0 and a.x < 0 or a.v_x > 0 and a.x > 1000 - a.width:
                on_edge = True
            elif a.y >= 560 - a.height:
                stage = GAME_OVER

        if on_edge:
            for a in aliens:
                a.v_x *= -1
                a.y += 10

        for a in aliens:
            a.move()

        for u in ufos:
            u.move()

        ''' make bombs '''
        for a in aliens:
            r = random.randrange(0, 1000)

            if r < bomb_rate:
                x = a.x + a.width // 2 - 1
                y = a.y + a.height - 4
                b = Bomb(x, y)
                b.v_y = bomb_speed
                bombs.append(b)

        ''' move bombs '''
        for b in bombs:
            b.move()

        ''' check hits '''
        aliens_to_remove = []
        bullets_to_remove = []
        ufos_to_remove = []

        for b in bullets:
            if b.y < -10:
                bullets_to_remove.append(b)
            else:
                b_rect = b.get_rect()

                for a in aliens:
                    a_rect = a.get_rect()

                    if intersects.rect_rect(a_rect, b_rect):
                        if a not in aliens_to_remove:
                            aliens_to_remove.append(a)
                            score += a.value
                            hits += 1

                            if sound_on:
                                HIT.play()

                        bullets_to_remove.append(b)

                for u in ufos:
                    u_rect = u.get_rect()

                    if intersects.rect_rect(u_rect, b_rect):

                        if u not in ufos_to_remove:
                            ufos_to_remove.append(u)

                            score += u.value * level
                            hits += 1

                            if sound_on:
                                HIT.play()

                        bullets_to_remove.append(b)

                for bu in bunkers:
                    bu_rect = bu.get_rect()

                    if intersects.rect_rect(bu_rect, b_rect):
                        bullets_to_remove.append(b)

        bombs_to_remove = []

        for b in bombs:
            if b.y > 560:
                bombs_to_remove.append(b)
            else:
                c_rect = cannon.get_rect()
                b_rect = b.get_rect()

                if intersects.rect_rect(c_rect, b_rect):
                    bombs_to_remove.append(b)
                    lives -= 1
                    stage = DIE

                    if sound_on:
                        CLANK.play()

                    if lives == 0:
                        stage = GAME_OVER

                for bu in bunkers:
                    bu_rect = bu.get_rect()

                    if intersects.rect_rect(bu_rect, b_rect):
                        bombs_to_remove.append(b)

        if stage == GAME_OVER:
            update_high_score()

    if stage == CLEAR and bonus > 0:
        score += 1
        bonus -= 1

    if score > extra_life_points:
        lives += 1
        extra_life_points *= 2

    if score > high_score:
        high_score = score

    # Drawing code

    ''' draw background '''
    screen.fill(colors.BLACK)
    stars.draw(screen)
    mountains.draw(screen)
    ground.draw(screen)

    ''' draw game objects '''
    cannon.draw(screen)

    for b in bullets:
        b.draw(screen)

    for a in aliens:
        a.draw(screen)

    for b in bombs:
        b.draw(screen)

    for u in ufos:
        u.draw(screen)

    for b in bunkers:
        b.draw(screen)


    x = 20
    y = 590
    for n in range(lives - 1):
        cannon.draw_icon(screen, x, y)
        x += 60

    ''' game stats '''
    high_text = font.render("High: " + str(high_score), True, colors.WHITE)
    score_text = font.render("Score: " + str(score), True, colors.WHITE)
    level_text = font.render("Level: " + str(level), True, colors.WHITE)
    screen.blit(score_text, [30, 20])
    screen.blit(high_text, [700, 20])
    screen.blit(level_text, [760, 580])

    if stage == START:
        title_text = big_font.render("NAME OF GAME", True, colors.WHITE)
        start_text = font.render("Press SPACE to start", True, colors.WHITE)
        screen.blit(title_text, [155, 200])
        screen.blit(start_text, [250, 310])
    elif stage == PAUSED:
        start_text = font.render("Game paused", True, colors.WHITE)
        screen.blit(start_text, [390, 250])
    elif stage == DIE:
        start_text = font.render("Lives remaining: " + str(lives), True, colors.WHITE)
        screen.blit(start_text, [390, 250])
    elif stage == CLEAR:
        clear_text = font.render("Level " + str(level) + " clear!", True, colors.GREEN)
        hits_text = font.render("Hits: " + str(hits), True, colors.WHITE)
        shots_text = font.render("Shots: " + str(shots) , True, colors.WHITE)
        accuracy_text = font.render("Accuracy: " + str(accuracy) + "%", True, colors.WHITE)
        bonus_text = font.render("Bonus: " + str(bonus), True, colors.WHITE)
        screen.blit(clear_text, [350, 150])
        screen.blit(hits_text, [350, 180])
        screen.blit(shots_text, [350, 210])
        screen.blit(accuracy_text, [350, 240])
        screen.blit(bonus_text, [350, 270])
    elif stage == GAME_OVER:
        over_text = font.render("Game Over", True, colors.WHITE)
        restart_text = font.render("Press 'r' to restart", True, colors.WHITE)
        screen.blit(over_text, [390, 220])
        screen.blit(restart_text, [250, 250])


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


    # Remove hit objects (see why this works better after drawing)
    if stage == PLAYING:
        aliens = [a for a in aliens if a not in aliens_to_remove]
        bullets = [b for b in bullets if b not in bullets_to_remove]
        bombs = [b for b in bombs if b not in bombs_to_remove]
        ufos = [u for u in ufos if u not in ufos_to_remove]

        if len(aliens) == 0:
            if shots > 0:
                accuracy = int(hits / shots * 100)
            else:
                accuracy = 0

            bonus = 5 * accuracy
            stage = CLEAR


# Close window on quit
pygame.quit()