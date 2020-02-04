import requests
import json
import os

global body
body = ''

# gets a specified amount of collors
def get_colors(num_colors):

    if num_colors <= 0 : num_colors = 1
    if num_colors > 1000 : num_colors = 1000
    
    request = requests.get(f'http://api.noopschallenge.com/hexbot?count={num_colors}?')

    temp = []
    for c in json.loads(request.text)["colors"]:
        temp.append(c["value"])

    return temp

# adds to the html body
def make_grid(header, colors):
    global body
    body += f'<h3>{header}</h3><br>'    

    for i in range(h):
        body += '<br>'
        for j in range(w):
            c = colors[i*w+j]            
            body += f'<a style="background-color:{c};color:{c}">__</a> '

def by_brightness(elem):
    r, g, b = tuple(int(elem.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))
    return r + g + b

def by_red(elem):
    r, g, b = tuple(int(elem.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))
    return r

def by_green(elem):
    r, g, b = tuple(int(elem.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))
    return g

def by_blue(elem):
    r, g, b = tuple(int(elem.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))
    return b

def negative(colors):
    temp = []
    for c in colors:
        r, g, b = tuple(int(c.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))

        r = 255 - r
        g = 255 - g
        b = 255 - b

        temp.append(f'rgb({r}, {g}, {b})')
        
    return temp

def grayscale(colors):
    temp = []
    for c in colors:
        r, g, b = tuple(int(c.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))

        val = (r + g + b)/3
        temp.append(f'rgb({val}, {val}, {val})')
        
    return temp

# set screen width and height
w = 40
h = 20

# get random colors
raw_colors = get_colors(w*h)

# create grid with raw, random colors
make_grid('Unsorted Colors', raw_colors)

# add to grid with negative colors
make_grid('Negative', negative(raw_colors))

# add to grid with gray scale colors
make_grid('Gray Scale', grayscale(raw_colors))

# add to grid with sorted colors by brightness
sorted_colors = raw_colors
sorted_colors.sort(key=by_brightness)
make_grid('Sorted by Brightness', raw_colors)

# add to grid with sorted colors by red
sorted_colors.sort(key=by_red)
make_grid('Sorted by Red', raw_colors)

# add to grid with sorted colors by green
sorted_colors.sort(key=by_green)
make_grid('Sorted by Green', raw_colors)

# add to grid with sorted colors by blue
sorted_colors.sort(key=by_blue)
make_grid('Sorted by Blue', raw_colors)

# write body to file
with open('index.html', 'w') as file:
    file.write(body)

cwd = os.getcwd()
print('[!] Please open the following file')
print(f'file:///{cwd}/index.html')
