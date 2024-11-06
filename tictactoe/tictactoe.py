"""
Tic Tac Toe Player
"""

import math

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
action = (1,1)
action = (0,0)
action = (2,2)
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return 'O'  # O's turn
    else:
        return 'X'  # X's turn



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actionboard = deepcopy(board)
    i,j = action
    if actionboard[i][j] == EMPTY:
        actionboard[i][j] =player(board)
    print(actionboard)
    """print(player(board))
    print(i,j)"""
    return actionboard







def winner(board):
    """
    
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]


    


def terminal(board):
    if winner(board) is not None:  # Game is over if there's a winner
        return True
    for row in board:
        if EMPTY in row:  # Game is not over if there's an empty cell
            return False
    return True  # Game is over if there are no empty cells
      
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0     
    


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
result(board,action)