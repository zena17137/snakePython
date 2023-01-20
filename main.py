import pygame
from random import randrange

RES = 600
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {
    'W': True, 'S': True, 'A': True, 'D': True,
}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1

    if x < 0 or x > RES - SIZE + SIZE or y < 0 or y > RES - SIZE + SIZE:
        break
    if len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dirs = {
            'W': True, 'S': False, 'A': True, 'D': True,
        }
        dx, dy = 0, -1
    if key[pygame.K_s] and dirs['S']:
        dirs = {
            'W': False, 'S': True, 'A': True, 'D': True,
        }
        dx, dy = 0, 1
    if key[pygame.K_a] and dirs['A']:
        dirs = {
            'W': True, 'S': True, 'A': True, 'D': False,
        }
        dx, dy = -1, 0
    if key[pygame.K_d] and dirs['D']:
        dirs = {
            'W': True, 'S': True, 'A': False, 'D': True,
        }
        dx, dy = 1, 0