import requests
import json
from os import system
from math import sqrt

width = 100
height = 40

# gets a specified amount of lines
def get_lines(num_lines, connected=0):

    if num_lines <= 0 : num_lines = 1
    if num_lines > 1000 : num_lines = 1000

    connected = int(connected)
    
    request = requests.get(f'https://api.noopschallenge.com/vexbot?count={num_lines}&width={width}&height={height}&connected=0')
    points = json.loads(request.content)["vectors"]

    return points

# clears console
def clear():
    system('cls')

# draws screen
def draw(pos, lines):
    screen = ''

    for i in range(height):
        screen += '\n'
        for j in range(width):
            if [j, i] in pos:
                screen += 'o'
            elif [j, i] in lines:
                screen += '+'
            else:
                screen += ' '

    print(screen)

# create lines
points = get_lines(5)

# work out the positions of points and lines
pos = []
lines = []
for point in points:

    x1, y1 = point["a"]["x"], point["a"]["y"]
    x2, y2 = point["b"]["x"], point["b"]["y"]

    dvelx = x2 - x1
    dvely = y2 - y1

    mag = sqrt((dvelx**2) + (dvely**2))

    normalx = dvelx / mag
    normaly = dvely / mag

    x, y = x1, y1
    while True:
        if int(x) != x2:
            x += normalx

        if int(y) != y2:
            y += normaly

        if int(x) == x2 and int(y) == y2:
            break

        if [int(x), int(y)] not in lines:
            lines.append([int(x), int(y)])

    pos.append([x1, y1])
    pos.append([x2, y2])

# clear and draw the screen    
clear()
draw(pos, lines)












