# Play vs player
# Play vs AI
# Simple GUI

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}


def dispBoard():
    print(board['1'] + ' | ' + board['2'] + '| ' + board['3'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + '| ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + '| ' + board['9'])


def startGame():
    dispBoard()


def executeTurn():
    pos = input('Choose position from 1-9, where 1-topleft, 9-bottomright: ')
    board[pos] = 'X'

    dispBoard()


def main():
    startGame()
    executeTurn()


if __name__ == '__main__':
    main()




# Generere et brett.
# Vise et brett

# Spille.

# Sjekke om det er seier, uavgjort



