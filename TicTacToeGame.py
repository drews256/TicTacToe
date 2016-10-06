import random

#Create a game state for game,
#includeing the player and computer letter
#the played positions for both the player and computer
#Whos turn it is and the played positions
class Game(object):

    positions = {'player_positions': [], 'computer_positions': []}
    letters = {'player_letter': None, 'computer_letter': None}
    turn = 'computer'
    board = [[(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)]]
    win = False

# if 'Position' then build a new line with the x in the proper position
def board_position(): #translate board positions, from letter/number to a position.

    new_pos = input("What Position?: ")
    switcher = {
        'A1': {'player': 'player', 'position' : (1, 1)},
        'A2': {'player': 'player', 'position' : (1, 2)},
        'A3': {'player': 'player', 'position' : (1, 3)},
        'B1': {'player': 'player', 'position' : (2, 1)},
        'B2': {'player': 'player', 'position' : (2, 2)},
        'B3': {'player': 'player', 'position' : (2, 3)},
        'C1': {'player': 'player', 'position' : (3, 1)},
        'C2': {'player': 'player', 'position' : (3, 2)},
        'C3': {'player': 'player', 'position' : (3, 3)}
    }
    return switcher.get(new_pos)

# present the board correctly.
def board_presentation(Game):
    # Create the Top of the board game
    top_game = ('    A   B   C')
    in_between_line = ('  +---+---+---+')
    # Blank Line
    blank_line = ('|   |   |   |' + '\n')

    print(top_game)
    print(in_between_line)
    i2=0;
    for rows in Game.board:
        print( str(i2+1) + " |", end="", flush=True)
        i = 0;
        for position in rows:
            if position is "X" and i < 2:
                print(" X |", end="")
            elif position is "O" and i < 2:
                print(" O |", end="")
            elif position is "X" and i == 2:
                print(" X |")
            elif position is "O" and i == 2:
                print(" O |")
            else:
                if position[0] == 3:
                    print("   |", flush=True)
                else:
                    print("   |", end="", flush=True)
            i+=1;
        print(in_between_line)
        i2+=1;

def player_letter(Game): #pick X's or O's as the player
    player_let=input('Would you like to play as X? or O?: ')

    def switch_player_let(player_let):
        switcher = {
            'X' : 'O',
            'O' : 'X'
        }
        return switcher.get(player_let, 'You have entered an Invalid letter. Please type O or X!')

    Game.letters['player_letter'] = player_let
    Game.letters['computer_letter'] = switch_player_let(player_let)

# Now that we have the player letter, the computer gets to play first!
def random_computer_position(Game): #Get a random position for the computer
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    position = {'player' : 'computer', 'position' : (x,y)}
    return position

def position_checker_helper(player_string, position):
    Game.positions[player_string + '_positions'].append(position['position'])
    if player_string == 'player': #make sure to update whos turn it is. If you get to this point the position is availalbe
        Game.turn = 'computer'
    elif player_string == 'computer':
        Game.turn = 'player'

    board = Game.board
    pos = position['position']

    row = board[pos[1] - 1] #a little hackish to get the letter in the right spot. In the Game
    row[pos[0] - 1] = Game.letters[player_string+'_letter']

    check_win(Game) #see if anyone wins?!
    whos_turn(Game) #run the game to play the next turn, based on whos turn it is.


def position_checker(position, Game): # def check a position for previous play
    if position == None:
        print('You entered a position that does not exist? Try again')
        whos_turn(Game)
    elif position['position'] in Game.positions['player_positions'] or position['position'] in Game.positions['computer_positions'] or len(position['position']) != 2:
        print('Looks like that position is taken. Try again. ')
        whos_turn(Game) #if the position already exists in the game board, rerun either the computer or player
    else:
        if position['player'] is 'computer':
            position_checker_helper('computer',position) # keeping it nice and dry gotta love python
        else:
            position_checker_helper('player', position)

def whos_turn(Game): #Update whos turn it is.
    if Game.turn == 'computer': #if its computers turn, get a random position and checkit
        position_checker(random_computer_position(Game), Game)
    else:
        board_presentation(Game)
        position_checker(board_position(), Game) #check the position of a user selected postion

def end_game(): #end the game and show the final game board.
    board_presentation(Game)
    exit()

def check_win(Game): #provide winning combininations. There are only 9.
    winning_positions = [[(1,1),(1,2),(1,3)],
                         [(2,1),(2,2),(2,3)],
                         [(3,1),(3,2),(3,3)],
                         [(1,1),(2,1),(3,1)],
                         [(1,2),(2,2),(3,2)],
                         [(1,3),(2,3),(3,3)],
                         [(1,1),(2,2),(3,3)],
                         [(1,3),(2,2),(3,1)]]

    for winning_position in winning_positions:
        if winning_position[0] in Game.positions['player_positions'] and winning_position[1] in Game.positions['player_positions'] and winning_position[2] in Game.positions['player_positions']:
            Game.win == True
            print('You win! Good Job!')
            end_game()
        elif winning_position[0] in Game.positions['computer_positions'] and winning_position[1] in Game.positions['computer_positions'] and winning_position[2] in Game.positions['computer_positions']:
            print('You lose! Youre not very good at this!')
            Game.win == True
            end_game()
        elif len(Game.positions['player_positions']) + len(Game.positions['computer_positions']) == 9 and Game.win == False:
            print('Draw! You managed to tie a random number generator with raw skill ;)')
            end_game()
    whos_turn(Game)

def run_game(Game): #make sure we have a correct letter
    if not Game.letters['player_letter'] == 'X' and not Game.letters['player_letter'] == 'O':
        player_letter(Game)
        run_game(Game)

    whos_turn(Game)

run_game(Game) #start the game!
