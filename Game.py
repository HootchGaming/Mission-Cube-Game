import pygame
import random
import sys


pygame.init()

WIDTH = 800
HEIGHT = 600

background = pygame.image.load("C:/Users/DELL/Documents/Mission-Cube/data/background1.png")
background1 = pygame.image.load("C:/Users/DELL/Documents/Mission-Cube/data/cube.png")

background2 = pygame.image.load("C:/Users/DELL/Documents/Mission-Cube/data/cube2.png")

GREEN = (0,128,0)
RED = (255,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
BLUE = (0, 255, 255)
colours = [BLUE, GREEN, RED, PURPLE]
BACKGROUND_COLOUR = (0,0,0)

music = pygame.mixer.music.load("C:/Users/DELL/Documents/Mission-Cube/data/song2.mp3")
pygame.mixer.music.play(-1)

SPEED = 10

player_size = 50
player_pos = [WIDTH/2, HEIGHT - 1.1*player_size]
x_po = player_pos[0]
y_po = player_pos[1]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

score = 0

game_over = False

finish = True

clock = pygame.time.Clock()

font = pygame.font.SysFont("monospace", 25)


class button(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 15 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    x = 0
    for enemy_pos in enemy_list:
         pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def set_level(score, SPEED):
    if score < 10:
        SPEED = 10
    elif score < 30:
        SPEED = 15
    elif score < 50:
        SPEED = 20
    elif score < 70:
        SPEED = 25
    elif score < 80:
        SPEED = 30
    else:
        SPEED = 50
    return SPEED

def update_enemy_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score
    if detect_collision(player_pos, enemy_pos):
        game_over = True
        finish = True

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False



def show_go_screen():
    holo = True
    while holo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    holo = False

        screen.fill((0,0,0))
        clock.tick(30)
        screen.blit(background2,(0, 0))
        text1 = "        " + str(score)
        label1 = font.render(text1, 1, (255, 255, 255))
        screen.blit(label1, (WIDTH-445, HEIGHT- 523) )
        pygame.display.update()

menu = True

while not game_over:

    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    menu = False
                    music = pygame.mixer.music.load("C:/Users/DELL/Documents/Mission-Cube/data/song1.mp3")
                    pygame.mixer.music.play(-1)


        screen.fill((0,0,0))
        clock.tick(30)
        screen.blit(background1,(0, 0))
        pygame.display.update()



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT and x > 40:
                x -= 50
            elif event.key == pygame.K_RIGHT and x < WIDTH - player_size - 49.5:
                x += 50
            player_pos = [x, y]



    screen.fill(BACKGROUND_COLOUR)

    drop_enemies(enemy_list)
    score = update_enemy_pos(enemy_list, score)

    SPEED = set_level(score, SPEED)

    text = "Score : " + str(score)
    label = font.render(text, 1, RED)
    screen.blit(label, (WIDTH-170, HEIGHT-40) )

    if collision_check(enemy_list, player_pos):
        game_over = True

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, ORANGE, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()

if finish:
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load("C:/Users/DELL/Documents/Mission-Cube/data/song3.mp3")
    pygame.mixer.music.play(0)
    show_go_screen()
    finish = False
