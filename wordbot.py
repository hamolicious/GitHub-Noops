import requests
import json

def get_word(count, word_set=''):
    if word_set != '':
        word_set = '&set=' + word_set
    
    r = requests.get(f'https://api.noopschallenge.com/wordbot?count={count}{word_set}')

    words = json.loads(r.content)["words"]

    return words

def get_sets():
    r = requests.get(f'https://api.noopschallenge.com/wordbot/sets')
    sets = json.loads(r.content)

    return sets

def clear():
    print('\n' * 50)

def start():
    clear()
    print('Welcome to the sentance builder... the most useless "keyboard" ever')
    print('You can type in "help" to show the available commands')
    input('Press enter to start: ')

def show_sets():
    for i in range(len(sets)):
        print(f'[{i}]  {sets[i]}')

def show_commands():
    print('sets - shows the available sets')
    print('addword - adds a word to the sentance')
    print('fromset <NUM> - add a word from a set, add the set number to the end')
    print('output - show the created sentance')
    print('input - add your own words to the sentance')
    print('clear - clear the console')
    print('tofile <filename> - output the sentance to a txt file [no spaces]')

def main():
    clear()

    sentance = ''
    while (cmd := input('[>> ').lower().strip()) != 'q':
        if cmd == 'help' or cmd == 'h' : show_commands()
        if cmd == 'sets' : show_sets()
        if cmd == 'addword': sentance += get_word(1)[0] + ' '
        if cmd == 'output' : print('\n\nSentance: ' + sentance + '\n\n')
        if cmd.split(' ')[0] == 'input' : sentance += cmd[5:len(cmd)].strip() + ' '
        if cmd == 'clear' : clear()
        
        if cmd.split(' ')[0] == 'tofile':
            with open('{}.txt'.format(cmd.split(' ')[1]), 'w') as file:
                file.write(sentance)

        if cmd.split(' ')[0] == 'fromset':
            try:
                sentance += get_word(1, sets[int(cmd.split(' ')[1])])[0].strip() + ' '
            except IndexError:
                pass

sets = get_sets()
count = 20
words = get_word(count)

start()
main()



































