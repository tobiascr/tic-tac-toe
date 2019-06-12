
from test_engine import EngineInterface
from test_engine import minimax_value_list

def draw_board(game_state):
    for row in range(3):    
        print(" --- --- ---")
        for k in range(row*3,row*3+3):
            print("| ", end="")
            print(game_state[k], end=" ")
        print("|")
    print(" --- --- ---")

engine = EngineInterface(3)

game_states = []

a = ["X", "O", " "]
for i0 in a:
 for i1 in a:
  for i2 in a:
   for i3 in a:
    for i4 in a:
     for i5 in a:
      for i6 in a:
       for i7 in a:
        for i8 in a:
            p = [i0, i1, i2, i3, i4, i5, i6, i7, i8]

            if p.count("X") == p.count("O") or p.count("X") == p.count("O") + 1:
                if p.count(" ") > 0:
                     if not engine.three_in_a_row(p):
                             game_states.append(p)

def X_in_turn(game_state):
    """Return True iff there is an odd number of " " in game_state"""
    return len([i for i in game_state if i == " "]) % 2 == 1
    
def win_in_1(game_state):
    """Return if for example it's X's turn and X can make a three in a row."""    
    available_moves = [i for i in range(9) if game_state[i] == " "]                       
    # If X is in turn.
    if len(available_moves) % 2 == 1:
        for move in available_moves:
            game_state[move] = "X"
            if engine.three_in_a_row(game_state):
                return True                    
            game_state[move] = " "               
    # If O is in turn.
    else:
        for move in available_moves:
            game_state[move] = "O"
            if engine.three_in_a_row(game_state):
                return True                    
            game_state[move] = " "
    return False
            
for p in game_states:
    if p.count(" ") == 100:
        value_list = minimax_value_list(p)
        values = []
        for x in value_list:
            if x != None and x not in values:
                values.append(x)
        if len(values) > 2:
            if values[0] >= 0 and values[1] >= 0 and values[2] >= 0:
                draw_board(p)
                print(values)
                print(value_list)
                print(win_in_1(p))
            if values[0] <= 0 and values[1] <= 0 and values[2] <= 0:
                print(values)
                print(value_list)                   

for p in game_states:
    if p.count(" ") != 10:
        value_list = minimax_value_list(p)
        values = []
        positive_values = []
        negative_values = []
        for x in value_list:
            if x != None and x not in values:
                values.append(x)
                if x > 0:
                    positive_values.append(x)
                elif x < 0:
                    negative_values.append(x)                
        if X_in_turn(p):
            if len(positive_values) > 1:
                if not win_in_1(p):
                    print("X", win_in_1(p), values, positive_values, negative_values)
                    print(value_list)
                    draw_board(p)
        else:
            if len(negative_values) > 1:
                if not win_in_1(p):            
                    print("Y", win_in_1(p), values, positive_values, negative_values)
                    print(value_list)                    
                    draw_board(p)

                
# Facts about tic tac toe.
# ------------------------

# If there are more than two ply levels of winning moves, none of them need to be an immediate win.
# That happens only when there are 5 empty places on the board. X then always have an option to make
# a fork.

# If in a game state are there more than 2 different
# ply-levels of forced winning, then one of them is an immediate win.

