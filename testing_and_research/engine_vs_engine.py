
from engine_copy import EngineInterface

import random

def draw_board(game_state):
    for row in range(3):    
        print(" --- --- ---")
        for k in range(row*3,row*3+3):
            print("| ", end="")
            print(game_state[k], end=" ")
        print("|")
    print(" --- --- ---")

engine_level_1 = EngineInterface(1)
engine_level_2 = EngineInterface(2)
engine_level_3 = EngineInterface(3)

def game(engine1, engine2, engine1_makes_first_move=True):
    """engine1 and engine2 are instances of EngineInterface."""
    game_state = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]
    one_in_turn = engine1_makes_first_move
    while " " in game_state:
        if one_in_turn:
            move = engine1.engine_move(game_state)
            if engine1_makes_first_move:
                game_state[move] = "X"
            else:
                game_state[move] = "O"            
            if engine1.three_in_a_row(game_state):
                return "engine1"
        else:
            move = engine2.engine_move(game_state)
            if engine1_makes_first_move:
                game_state[move] = "O"
            else:
                game_state[move] = "X"
            if engine1.three_in_a_row(game_state):
                return "engine2"               
        one_in_turn = not one_in_turn

def games(engine1, engine2, number_of_games):
    """Let engine1 and engine2 play several games against each other.
    Each begin every second game."""
    engine1_wins = 0
    engine2_wins = 0
    draws = 0
    for n in range(number_of_games):
        if n % 2:
           result = game(engine1, engine2, True)
        else:
           result = game(engine1, engine2, False)
        if result == "engine1":
            engine1_wins += 1
        elif result == "engine2":
            engine2_wins += 1
        else:
            draws += 1    
    return ("engine1 wins: " + str(engine1_wins) +
            " engine2 wins: " + str(engine2_wins) + " draws: " + str(draws))
                                
print(games(engine_level_2, engine_level_3, 10000))

        

                  
                  
