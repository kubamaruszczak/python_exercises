from os import system

game_table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def reset_game():
    """Filling the game table with blank fields"""
    global game_table

    for row in game_table:
        for idx, _ in enumerate(row):
            row[idx] = ' '


def print_table():
    """Printing whole game table in the terminal"""
    global game_table

    # Clear the screen
    system('clear')

    # Print current table
    print()
    for r_idx, row in enumerate(game_table):
        for e_idx, element in enumerate(row):
            print(f' {element} ', end='')
            if e_idx != 2:
                print('|', end='')
        if r_idx != 2:
            print('\n-----------')
    print('\n')


def make_choice(player: str) -> tuple:
    """Function to place user choice on the game table.
    Returns position of placed symbol in form of a tuple"""
    global game_table

    # Take user inputs
    print(f"It's {player} turn.")
    row_num = input(f"Select row (1 - 3): ")
    col_num = input(f"Select column (1 - 3): ")

    # Check if the inputs are valid
    if row_num in ['1', '2', '3'] and col_num in ['1', '2', '3']:
        row_num = int(row_num) - 1
        col_num = int(col_num) - 1
        # Check if the field is empty
        if game_table[row_num][col_num] == ' ':
            game_table[row_num][col_num] = player
            return row_num, col_num
        else:
            print_table()
            print('This field is already taken! Try again.')
            return make_choice(player)

    else:
        print_table()
        print('Invalid coordinates! Try again.')
        return make_choice(player)


def check_score(player: str, last_coordinates: tuple) -> bool:
    """Checks if the user wins or if it's a draw based on the
    last coordinates"""
    global game_table

    row_num, col_num = last_coordinates

    if ( [row_num][0] == player and game_table[row_num][1] == player and game_table[row_num][1] == player or
         game_table[0][col_num] == player and game_table[1][col_num] == player and game_table[2][col_num] == player or
         game_table[0][0] == player and game_table[1][1] == player and game_table[2][2] == player or
         game_table[0][2] == player and game_table[1][1] == player and game_table[2][0] == player):
        print(f"{player} WINS")
        return True
    elif ' ' in game_table[0] + game_table[1] + game_table[2]:
        return False
    else:
        print(f"It's a draw!")
        return True


# X starts the game
current_player = 'X'
print_table()
print(make_choice(player=current_player))

game_is_on = True
while game_is_on:
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    print_table()
    last_pos = make_choice(player=current_player)
    if check_score(current_player, last_pos) is True:
        game_is_on = False
