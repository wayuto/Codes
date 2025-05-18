import pygame as pg
from random import randint


SCREEN = pg.display.set_mode([800, 600])
towards = 0
A = 19
move = V = R = 10
head = [300, 400]
snacks = [head]
foods = [(220, 350), (450, 250), (390, 340), (690, 400)]
kind = ((0, 800), (0, 600))                          
keytype = ((pg.K_d, 0, V), (pg.K_a, 0, -V), (pg.K_s, 1, V), (pg.K_w, 1, -V))
while True:
    SCREEN.fill((255, 255, 255))
    for event in pg.event.get([pg.KEYDOWN, pg.QUIT]):
        if event.type == pg.QUIT:                                              
            quit()
        else:                          
            for key in keytype:
                if event.key == key[0]:
                    towards, move = key[1], key[2]
    pg.event.clear()
    head[towards] += move
    for i in range(2):
        for b in range(2):
            if head[i] == kind[i][b]:
                head[i] = kind[i][1 - b]
                break
    snacks.insert(0, head.copy())
    snacks.pop()
    if head in snacks[1:]:
        quit()
    for snack in snacks:
        pg.draw.rect(SCREEN, (0, 200, 200), (snack[0], snack[1], A, A))
    if len(foods) <= 3:
        foods.append((randint(0, 750), randint(0, 550)))
    for food in foods:
        pg.draw.circle(SCREEN, (200, 200, 200), (food[0], food[1]), R)
        if food[0] - R - A <= head[0] <= food[0] + R and food[1] - R - A <= head[1] <= food[1] + R:
            foods.remove(food)
            snacks.append([head[0] - A, head[1]])
    pg.display.update()
    pg.time.Clock().tick(20)