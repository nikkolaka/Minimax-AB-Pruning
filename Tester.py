import math

from Board import Board, Node
from Solver import Algorithms


# Main function
def main():
    # Get input from user
    (player, searchMethod, m, n) = input(
        "Enter player, search method, and size of board in m n format: \n ex. 1 MM 5 5").split(" ")
    root = Node(Board(int(n), int(m)))
    player = int(player)

    depth = int(input("Enter depth: \n"))



    if int(player) == 1:
        print("Player 1: AI \nPlayer 2: Human")
        ai_shape = "O"
        turn = False
    else:
        print("Player 1: Human \nPlayer 2: AI")
        ai_shape = "X"
        turn = True

    print(root.value.__str__() + "\n")

    solver = Algorithms()

    while root.value.get_utility() > 0:
        if not turn:

            # AI move based on which algorithm is selected
            if searchMethod == "MM":
                result = solver.minimax(root, depth, player == 1)
                root.value.set_square(result.last_move[0], result.last_move[1], ai_shape)
                turn = True
                print(root.value.__str__() + "\n")
            elif searchMethod == "AB":
                result = solver.minimax_alpha_beta(root, depth, -math.inf, math.inf, player == 1)
                root.value.set_square(result.last_move[0], result.last_move[1], ai_shape)
                turn = True
                print(root.value.__str__() + "\n")

        else:

            # Error handling for human move
            while True:
                try:
                    y, x = input("Enter coordinates in row/column format: \n").split("/")

                except ValueError:
                    print("Invalid input, try again")
                    continue

                if (int(x) < root.value.get_size()[0] and int(y) < root.value.get_size()[1] and root.value.get_square(
                        int(x), int(y)) == "-"):
                    if player == 1:
                        root.value.set_square(int(x), int(y), "X")
                    else:
                        root.value.set_square(int(x), int(y), "O")
                    turn = False

                    break
                else:
                    print("Invalid move, try again")

    if root.value.last_move[2] == "X" and player == 1 or root.value.last_move[2] == "O" and player == 2:
        print("You Won!\n")
    else:
        print("AI Won!\n")

    file = open("MyReadMe.txt", "a")
    file.write("\n")
    file.write("Board Size: " + str(root.value.size[0]) + "x" + str(root.value.size[1]) + "\n")
    file.write("AI player is: " + str(player) + "\n")
    if (searchMethod == 'MM'):
        file.write("Minimax\n")
    else:
        file.write("Minimax with AB pruning\n")

    file.write("Nodes expanded: " + str(solver.expanded_nodes) + "\n")
    file.write("Depth Level: " + str(depth) + "\n")
    file.write("----------------")
    file.close()




while True:
    main()
    if (input("Play again? (y/n)") == "n"):
        break
