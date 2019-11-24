
"""This engine is made for examination of the game and for production of an opening book.
It does not aim for high efficiency, because if so, it might not give complete solutions
which can be needed in other situations than playing the game, where only one good move is
what is asked for.

In this module game states are often used as parameters. A game state is
stored in a list of length 9 where each entry is " ", "X" or "O"
(the letter O). The diagram below shows which square corresponds to
which place in the list.

     --- --- ---
    | 0 | 1 | 2 |
     --- --- ---
    | 3 | 4 | 5 |
     --- --- ---
    | 6 | 7 | 8 |
     --- --- ---
    
X is the first to move in each game.
"""    

import random


class EngineInterface():
    def __init__(self, difficulty_level):
        """difficulty_level can be 1, 2 or 3. 1 is easy.
        2 is intermediate and 3 is perfect play.
        """
        self.difficulty_level = difficulty_level

    def three_in_a_row(self, game_state):
        """Return true if X or O have three in a row and false otherwise."""
        x = game_state
        for n in ["O", "X"]:
            if x[:3] == [n,n,n]: return True
            if x[3:6] == [n,n,n]: return True
            if x[6:9] == [n,n,n]: return True
            if [x[0],x[3],x[6]] == [n,n,n]: return True
            if [x[1],x[4],x[7]] == [n,n,n]: return True
            if [x[2],x[5],x[8]] == [n,n,n]: return True
            if [x[0],x[4],x[8]] == [n,n,n]: return True
            if [x[2],x[4],x[6]] == [n,n,n]: return True
        return False

    def engine_move(self, game_state):
        """Return an integer from 0 to 8 that represents a move made
        by the engine."""
        if self.difficulty_level == 1:
            return random_move(game_state)
        if self.difficulty_level == 2:
            return random_move(game_state)
        if self.difficulty_level == 3:
            value_list = minimax_value_list(game_state)
            print(value_list[:3])
            print(value_list[3:6])
            print(value_list[6:])
            print()
            max_value = max([i for i in value_list if i != None])
            min_value = min([i for i in value_list if i != None])
            if X_in_turn(game_state):
                return random.choice([move for move in range(9) if value_list[move] == max_value])
            else:
                return random.choice([move for move in range(9) if value_list[move] == min_value])

def X_in_turn(game_state):
    """Return True iff there is an odd number of " " in game_state"""
    return len([i for i in game_state if i == " "]) % 2 == 1

def random_move(game_state):
    "Return a random move 0-8 that is legal given game_state."
    return random.choice([i for i in range(9) if game_state[i] == " "])

def minimax_value_list(game_state, depth=10):
    """Return minimax values for each of the available moves in game_state.
    The values is returned in the form of a list of length 9, where the indices
    correspond to the moves and the values are the minimax values. For moves
    that are not legal, the value None is given.
    """
    value_list = [None] * 9
        
    if X_in_turn(game_state):
        for move in range(9):
            if game_state[move] == " ":
                game_state[move] = "X"
                value_list[move] = minimax(game_state, move, False, depth)
                game_state[move] = " "
    else:
        for move in range(9):
            if game_state[move] == " ":
                game_state[move] = "O"
                value_list[move] = minimax(game_state, move, True, depth)
                game_state[move] = " "

    return value_list    

def minimax(game_state, last_move, maximizing_player_in_turn=True, depth=10):
    """Computes a value of game_state. Return >= 1 for a winning game_state for
    the maximizing player, 0 for a draw or unkowns outcome and <= -1 for a loss
    for the maximizing player. The returned numbers are higher i absolute value
    for forced wins or losses in fewer moves. last_move is the last
    index in game_state where a move has been made. Player X is considered
    the maximizing player and maximizing_player_in_turn is True
    if player O made the last move and vice versa."""
    # If win.
    if three_in_a_row(game_state, last_move):
        if maximizing_player_in_turn:
            return -(1 + depth)
        else:
            return 1 + depth
    # If the board is full and nobody have three in a row it's a draw.
    available_moves = [i for i in range(9) if game_state[i] == " "]
    if not available_moves:
        return 0
    # If unknown if the game state is winning, losing or drawing and return 0.
    if depth == 0:
        return 0
    # If not an endnode, try make moves and evaluate them recursively.
    if maximizing_player_in_turn:
        value = -1000
        for move in available_moves:
            # Make a move.
            game_state[move] = "X"
            # Evaluate the move.
            value = max(value, minimax(game_state, move, False, depth - 1))
            # Undo the move.
            game_state[move] = " "
        return value
    else:
        value = 1000
        for move in available_moves:
            # Make a move.
            game_state[move] = "O"
            # Evaluate the move.
            value = min(value, minimax(game_state, move, True, depth - 1))
            # Undo the move.
            game_state[move] = " "
        return value

def three_in_a_row(game_state, last_move):
    """Return true if X or O have three in a row in one of the
    rows that include last_move. Else return false."""    
    if last_move == 0:
        if game_state[0] == game_state[1] == game_state[2]: return True
        if game_state[0] == game_state[4] == game_state[8]: return True 
        if game_state[0] == game_state[3] == game_state[6]: return True

    if last_move == 1:
        if game_state[1] == game_state[0] == game_state[2]: return True
        if game_state[1] == game_state[4] == game_state[7]: return True

    if last_move == 2:
        if game_state[2] == game_state[0] == game_state[1]: return True
        if game_state[2] == game_state[5] == game_state[8]: return True
        if game_state[2] == game_state[4] == game_state[6]: return True

    if last_move == 3:
        if game_state[3] == game_state[0] == game_state[6]: return True
        if game_state[3] == game_state[4] == game_state[5]: return True

    if last_move == 4:
        if game_state[4] == game_state[1] == game_state[7]: return True
        if game_state[4] == game_state[3] == game_state[5]: return True
        if game_state[4] == game_state[0] == game_state[8]: return True
        if game_state[4] == game_state[2] == game_state[6]: return True

    if last_move == 5:
        if game_state[5] == game_state[3] == game_state[4]: return True
        if game_state[5] == game_state[2] == game_state[8]: return True

    if last_move == 6:
        if game_state[6] == game_state[0] == game_state[3]: return True
        if game_state[6] == game_state[7] == game_state[8]: return True
        if game_state[6] == game_state[2] == game_state[4]: return True

    if last_move == 7:
        if game_state[7] == game_state[1] == game_state[4]: return True
        if game_state[7] == game_state[6] == game_state[8]: return True

    if last_move == 8:
        if game_state[8] == game_state[2] == game_state[5]: return True
        if game_state[8] == game_state[6] == game_state[7]: return True
        if game_state[8] == game_state[0] == game_state[4]: return True

    return False
