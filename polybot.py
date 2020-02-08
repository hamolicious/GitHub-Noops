import requests
import json
from os import system
from math import sqrt

def clear():
    system('cls')

def get_shape():
    req = requests.get(f'https://api.noopschallenge.com/polybot?count=1&width={width}&height={height}')

    points = []
    shape = json.loads(req.content)["polygons"]

    for i in shape[0]:
        points.append([i["x"], i["y"]])

    return points

def draw(points, lines):
    clear()
    screen = ''
    for i in range(height):
        screen += '\n'
        for j in range(width):
            if [j, i] in points:
                screen += 'O'
            elif [j, i] in lines:
                screen += '+'
            else:
                screen += ' '

    print(screen)

width = 50
height = 40

shape = get_shape()
lines = []

for x1, y1 in shape:
    for x2, y2 in shape:
        dx = x2 - x1
        dy = y2 - y1

        mag = sqrt(dx**2 + dy**2)

        if mag != 0:
            vec = [dx / mag, dy / mag]
        else:
            vec = [0, 0]

        while int(x1) != x2 and int(y1) != y2:
            x1 += vec[0]
            y1 += vec[1]

            if [int(x1), int(y1)] not in lines:
                lines.append([int(x1), int(y1)])

draw(shape, lines)
print(shape)

























