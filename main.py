import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render(game,current):
    '''Display current location'''
    print('\nYou are at the ' + game['rooms'][current]['name'] + '!')
    print(game['rooms'][current]['desc'])

def update(response,game,current):
    '''Process the input and update the state of the world'''
    for e in game['rooms'][current]['exits']:
        if e['verb'] == response:
            current = e['target']
    return current

def check_input():
    '''Get user input'''
    response = input('What would you like to do?\n').strip().upper()
    return response

def main():
    game = {}
    with open('game.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'START'

    quit = False
    while not quit:
        #render
        render(game,current)
        #check player input
        selection = check_input()
        #update
        current = update(selection,game,current)

    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()