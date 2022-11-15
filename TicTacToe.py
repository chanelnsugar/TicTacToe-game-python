# TicTacToe-game-python
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

gameplay = True
winner = None
player = 'X'


def play():



    display()

    while gameplay:
    
        choose(player)

        flip()

        gameover(board)


def display():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def choose(player):
    
    position = input('Choose a position --> ')
    position = int(position) - 1

    board[position] = player


    display()

def gameover(board):

    win(board)
    checkwin(board)

def win(board):
    
    row(board)
    diagonals(board)
    collumn(board)
    tie(board)
    checkwin(board)



def flip():

    global player

    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
        
def row(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] != "-" :
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
    
    else:
        return False       
    
def collumn(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] != "-" :
        winner = board[1]
        return True
    
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True
    
    else:
        return False
    
    
def diagonals(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    
    elif board[2] == board[4] == board[6] != "-" :
        winner = board[2]
        return True
    
    else:
        return False
    
def tie(board):
    global gameplay
    if ' ' not in board:
        print('Its a Tie.')
        gameplay = False


    
def checkwin(board):
    global gameplay
    if diagonals(board) or row(board) or collumn(board) == True:
        print('Win.')
        gameplay = False


play()











