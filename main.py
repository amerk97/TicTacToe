# TODO: 
# Play vs player
# Play vs AI
# Simple GUI


# Simple pvp terminal game:

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}
gameNotFinished = True
player = 'X'
winner = None


def dispBoard():
    print(board['1'] + ' | ' + board['2'] + '| ' + board['3'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + '| ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + '| ' + board['9'])


def startGame():
    dispBoard()

    while gameNotFinished:
        executeTurn(player)

        check_gameFinished()
        change_Player()



def executeTurn(player):
    pos = input('Choose position from 1-9, where 1-topleft, 9-bottomright: ')
    board[pos] = 'X'

    dispBoard()


def change_Player():
    return


def check_gameFinished():
    checkTie()
    checkWin()


def checkTie():
    return


def checkWin():
    return


def checkRow():
    return

def checkCol():
    return

def checkDiag():
    return



def main():
    startGame()
    executeTurn()


if __name__ == '__main__':
    main()