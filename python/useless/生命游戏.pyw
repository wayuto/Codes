import pygame
import sys
import time
import random

width = 102
high = 102
size = 6


def initialization(arr):
    for i in range(high):
        for j in range(width):
            ran = random.random()
            if ran > 0.9:
                arr[i][j] = 1
            else:
                pass
    return arr


def nextmultiply(arr):
    newarr = [([0] * width) for n in range(high)]
    for i in range(high):
        for j in range(width):
            num = 0
            if (i == 0 or i == high - 1) or (j == 0 or j == width - 1):
                newarr[i][j] = 0
            else:
                num = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j - 1] + arr[i][j + 1] + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
                if arr[i][j] == 0:
                    if num == 3:
                        newarr[i][j] = 1
                else:
                    if num == 2 or num == 3:
                        newarr[i][j] = 1
                    else:
                        newarr[i][j] = 0
    return newarr


if __name__ == '__main__':
    color_white = pygame.Color(255, 255, 255)
    color_LightSkyBlue = pygame.Color(135, 206, 250)
    color_black = pygame.Color(0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((width * size, high * size))
    screen.fill(color_white)
    pygame.display.set_caption("生命游戏(Game of Life)")
    arr = [([0] * width) for i in range(high)]
    arr = initialization(arr)
    while True:
        screen.fill(color_white)
        time.sleep(0.5)
        for i in range(high):
            for j in range(width):
                if arr[i][j] == 1:
                    pygame.draw.rect(screen, color_black, (i * size, j * size, size, size))
                elif (i == 0 or i == high - 1) or (j == 0 or j == width - 1):
                    pygame.draw.rect(screen, color_LightSkyBlue, (i * size, j * size, size, size))
                else:
                    pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        arr = nextmultiply(arr)
        pygame.display.update()