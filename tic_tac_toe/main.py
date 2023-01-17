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


def make_choice(player: str):
    """Function to place user choice on the game table"""
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
        else:
            print_table()
            print('This field is already taken! Try again.')
            make_choice(player)

    else:
        print_table()
        print('Invalid coordinates! Try again.')
        make_choice(player)


def check_score():
    global


# X starts the game
current_player = 'X'
print_table()
make_choice(player=current_player)

game_is_on = True
while game_is_on:
    if current_player == 'X':
        current_player = 'O'
        print_table()
        make_choice(player=current_player)
    else:
        current_player = 'X'
        print_table()
        make_choice(player=current_player)
