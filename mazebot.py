import requests
import json
from os import system
from msvcrt import getch
from time import sleep
from math import sqrt

# gets a specified amount of lines
def get_maze():
    request = requests.get(f'https://api.noopschallenge.com/mazebot/random?maxSize=20&minSize=20')

    json_obj = json.loads(request.content)

    grid = json_obj["map"]
    x, y = json_obj["startingPosition"]
    targx, targy = json_obj["endingPosition"]

    return grid, x, y, targx, targy

def clear():
    system('cls')

def draw(grid, x, y, steps):
    clear()

    screen = ''
    for i in range(len(grid)):
        screen += '\n'
        for j in range(len(grid[0])):
            if [j, i] != [x, y]:
                screen += grid[i][j] + ' '
            else:
                screen += '□ '

    print(screen.replace('X', '●'))
    print(f'Steps taken {steps}')
    print('''
Press for:
    W to move up
    A to move left
    S to move down
    D to move right

    R to reset

    P to quit
''')

def incSteps():
    global steps
    steps += 1
    
grid, x, y, targx, targy = get_maze()

savex = x
savey = y

global steps
steps = 0

while True:
    if x == targx and y == targy:
        clear()
        print(f'You have found the exit in {steps} steps!')
        sleep(1)
        steps = 0
        grid, x, y, targx, targy = get_maze()
        savex = x
        savey = y

    draw(grid, x, y, steps)

    key = getch()

    if key == b'w' and grid[y - 1][x] != 'X' and y > 0 : y -= 1 ; incSteps()
    if key == b'a' and grid[y][x - 1] != 'X' and x > 0: x -= 1 ; incSteps()

    try:
        if key == b's' and grid[y + 1][x] != 'X' : y += 1 ; incSteps()
        if key == b'd' and grid[y][x + 1] != 'X' : x += 1 ; incSteps()
    except IndexError:
        pass

    if key == b'r':
        steps = 0
        x = savex
        y = savey
    
    if key == b'p' : quit()












