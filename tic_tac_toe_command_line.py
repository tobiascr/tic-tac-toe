
from engine import EngineInterface

def draw_board(game_state):
    for row in range(3):
        print(" --- --- ---")
        for k in range(row*3,row*3+3):
            print("| ", end="")
            print(game_state[k], end=" ")
        print("|")
    print(" --- --- ---")

if __name__ == "__main__":
    print()
    print("The squares are numbered as follows:")
    print()
    print(" --- --- ---")
    print("| 0 | 1 | 2 |")
    print(" --- --- ---")
    print("| 3 | 4 | 5 |")
    print(" --- --- ---")
    print("| 6 | 7 | 8 |")
    print(" --- --- ---")
    print()
    print("To play the game, enter the number for the square of choice.")
    print()
    print("Print q to quit.")
    print()

    exit_program = False

    while True:
        answer = input("Difficulty level (1-3): ")
        if answer == "1" or answer == "2" or answer == "3":
            difficulty = int(answer)
            engine = EngineInterface(difficulty)
            print()
            break
        elif answer == "q":
            exit_program = True
            break

    game_state = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]

    # Variables to keep track of number of winning games.
    player_wins = 0
    computer_wins = 0

    game_over = False

    # A variable to keep track of when player is X.
    player_is_X = True

    # A variable to keep track of when it's X's turn to move.
    X_to_move = True

    while not exit_program:
        # If computer is in turn.
        if (X_to_move and not player_is_X) or (not X_to_move and player_is_X):
            if X_to_move:
                game_state[engine.engine_move(game_state)] = "X"
            else:
                game_state[engine.engine_move(game_state)] = "O"
        # If player is in turn.
        else:
            while True:
                if X_to_move:
                    choice = input("X to move: ")
                else:
                    choice = input("O to move: ")

                if choice in "012345678" and len(choice) == 1:
                    if game_state[int(choice)] == " ":
                        if X_to_move:
                            game_state[int(choice)] = "X"
                        else:
                            game_state[int(choice)] = "O"
                        print()
                        break
                    else:
                        print()
                        print("Invalid move.")
                        print()
                elif choice == "q":
                    exit_program = True
                    break
        if exit_program: break

        X_to_move = not X_to_move

        # Draw board if draw or players turn or somebody win.
        if (" " not in game_state or (X_to_move and player_is_X) or
                                     (not X_to_move and not player_is_X) or
                                     engine.three_in_a_row(game_state)):
            draw_board(game_state)
            print()

        # If win.
        if engine.three_in_a_row(game_state):
            if (X_to_move and not player_is_X) or (not X_to_move and player_is_X):
                print("You win. Congratulations!")
                player_wins += 1
            else:
                print("Computer win.")
                computer_wins += 1
            game_over = True

        # If draw.
        elif " " not in game_state:
            print("Draw")
            game_over = True

        if game_over:
            print()
            print("Player - Computer: " + str(player_wins) + " - " + str(computer_wins))
            choice = ""
            while choice != "y" and choice != "n" and choice != "q":
                print()
                choice = input("Play again (y/n)? ")

            if choice == "y":
                game_over = False  
                game_state=list(" "*9)
                player_is_X = not player_is_X
                X_to_move = True
                print()
                if player_is_X:
                    draw_board(game_state)
                    print()

            if choice == "n" or choice == "q": break

