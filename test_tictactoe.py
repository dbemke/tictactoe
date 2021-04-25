import tictactoe

def test_wincheck_lost():
    marker = "X"
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    assert tictactoe.win_chceck(board, marker) == False