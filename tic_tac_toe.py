

def is_input_valid(board):
    """
    Ask the user for a choice,
    check it is a number between 1 and 9
    and check the slot is available
    :param board: current board
    :return: valid user choice
    """
    while True:
        try:
            user_input = int(input("enter your choice between 1 to 9: "))
            if user_input < 1 or user_input > 9:
                print("out of range.")
                continue
        except ValueError:
            print("no letters/ signs allowed")
            continue

        row = (user_input - 1) // 3
        column = (user_input - 1) % 3

        if board[row][column] != " ":
            print("that slot is taken!")
            continue
        else:
            return user_input

def place_choice_on_board(board, user_input, symbol):
    """
    Convert user choice to its index on board and place the symbol in it
    :param board: current board
    :param user_input: valid number between 1 and 9
    :param symbol: "X" or "O"
    :return: updated board
    """
    row = (user_input - 1) // 3
    column = (user_input - 1) % 3
    board[row][column] = symbol
    return board

def check_strike(board, symbol):
    """
    Check if user's symbol appears 3 times in a row, column or diagonal
    :param board: current board
    :param symbol: "X" or "O"
    :return: True if there is a strike, False otherwise
    """
    for row in board:
        if all(slot == symbol for slot in row):
            return True

    for column in range(3):
        if all(board[row][column] == symbol for row in range(3)):
            return True

    diagonal_right = [board[0][0], board[1][1], board[2][2]]
    diagonal_left = [board[0][2], board[1][1], board[2][0]]
    if all(slot == symbol for slot in diagonal_right) or all(slot == symbol for slot in diagonal_left):
        return True

    return False

x_score = 0
o_score = 0
tie_score = 0

play_again = "y"

while play_again == "y":

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    game_over = False

    while not game_over:
        player = "X"
        user_choice = is_input_valid(board)
        place_choice_on_board(board, user_choice, player)
        for i in board:
            print(i)

        if check_strike(board, player):
            print("The winner is: player", player)
            x_score += 1
            game_over = True

        elif any(slot == " " for row in board for slot in row):
            print("next turn!")
            player = "O"
            user_choice = is_input_valid(board)
            place_choice_on_board(board, user_choice, player)
            for i in board:
                print(i)
            if check_strike(board, player):
                print("The winner is: player", player)
                o_score += 1
                game_over = True
        else:
            print("it's a tie!")
            tie_score += 1
            game_over = True

    print(f"scores: \nplayer X:  {x_score} \nplayer O:  {o_score} \ntie score: {tie_score}")
    play_again = input("play again? y/n ").lower()

    while play_again != "y" and play_again != "n":
        print("enter only y or n.")
        play_again = input("play again? ").lower()

    if play_again == "n":
        print("Goodbye!")





