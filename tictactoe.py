def display_board(board):
    print('{} | {} | {}'.format(board[6], board[7], board[8]))
    print('---------')
    print('{} | {} | {}'.format(board[3], board[4], board[5]))
    print('---------')
    print('{} | {} | {}'.format(board[0], board[1], board[2]))
    print('')

def playing(board, marker, player_name):
    while True:
        position = 0
        while not position in range(1, 10):
            position = int(input('{} - Choose a number - 1-9 '.format(player_name)))

        index = position - 1
        if board[index] == ' ':
            board[index] = marker
            display_board(board)
            break

def win_chceck(board, marker):
    if (board[0] == marker and board[1] == marker and board[2] == marker) or \
        (board[3] == marker and board[4] == marker and board[5] == marker) or \
        (board[6] == marker and board[7] == marker and board[8] == marker) or \
        (board[0] == marker and board[4] == marker and board[8] == marker) or\
        (board[6] == marker and board[4] == marker and board[2] == marker) or \
        (board[0] == marker and board[3] == marker and board[6] == marker) or \
        (board[4] == marker and board[1] == marker and board[7] == marker) or \
        (board[8] == marker and board[5] == marker and board[2] == marker):
        return True
    else:
        return False

if __name__ == "__main__":
    marker_player1 = ' '
    marker_player2 = ' '
    while not(marker_player1 == 'X' or marker_player1 == 'O'):
        marker_player1 = input('Player 1- Choose X or O  ').upper()
        if marker_player1 == 'X':
            marker_player2 = 'O'
        else:
            marker_player2 = 'X'

    board = [' '] * 9

    while True:
        playing(board, marker_player1, 'Player 1')
        if win_chceck(board, marker_player1):
            print('Player 1 - You have won!')
            break
        playing(board, marker_player2, 'Player 2')
        if win_chceck(board, marker_player2):
            print('Player 2 - You have won!')
            break

