import requests
import json
from os import system
from time import sleep
from math import sqrt
from random import randint, choice

width = 100
height = 40

class Ball():
    def __init__(self, pos, vel):
        self.pos = pos

        mag = sqrt((vel[0]**2) + (vel[1]**2))

        self.vel = vel[0] / mag, vel[1] / mag

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] > width - 1 : self.pos[0] = 0
        if self.pos[0] < 0 : self.pos[0] = width - 1
        if self.pos[1] > height - 1 : self.pos[1] = 0
        if self.pos[1] < 0 : self.pos[1] = height - 1

# gets a specified amount of lines
def get_dir(num_dir, connected=0, pattern=''):

    if num_dir <= 0 : num_dir = 1
    if num_dir > 1000 : num_dir = 1000

    connected = int(connected)

    if pattern != '':
        pattern = f'pattern="{pattern}"'
    
    request = requests.get(f'http://api.noopschallenge.com/directbot?count={num_dir}&width={width}&height={height}&connected={connected}' + pattern)
    points = json.loads(request.content)["directions"]

    return points

# clears console
def clear():
    system('cls')

# draws screen
def draw(pos):
    screen = ''

    for i in range(height):
        screen += '\n'
        for j in range(width):
            if [j, i] in pos:
                screen += choice(['o', 'O'])
            else:
                screen += ' '

    print(screen)

balls = []
for dir_ in get_dir(20):
    head = dir_["direction"]
    speed = dir_["speed"]

    if head == 'up' : vel = [0, -speed]
    if head == 'down' : vel = [0, speed]
    if head == 'left' : vel = [-speed, 0]
    if head == 'right' : vel = [speed, 0]
    
    balls.append(Ball([randint(0, width - 1), randint(0, height - 1)], vel))

while True:
    pos = []
    for ball in balls:
        ball.update()
        pos.append(ball.pos)

    clear()
    draw(pos)












