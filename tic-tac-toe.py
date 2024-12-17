# Initialize the game board as a 4x4 matrix with indices for rows and columns
matrix = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]


# Function to print the current state of the game board
def print_current_state():
    # Loop through each row and column to print the board state
    for r in range(4):
        for c in range(4):
            print(matrix[r][c], end=' ')
        print()


# Function to check if the game has ended
def check_if_game_ended():
    # Check for winning rows
    for i in range(1, 4):
        if matrix[i][1] == matrix[i][2] == matrix[i][3] and matrix[i][1] != '-':
            return True
        # Check for winning columns
        if matrix[1][i] == matrix[2][i] == matrix[3][i] and matrix[1][i] != '-':
            return True
    # Check for winning diagonals
    if matrix[1][1] == matrix[2][2] == matrix[3][3] and matrix[1][1] != '-':
        return True
    if matrix[1][3] == matrix[2][2] == matrix[3][1] and matrix[1][3] != '-':
        return True
    return False


# Function to validate whether a player's move is correct
def is_correct_move(coordinates):
    # A move is valid if the chosen cell is currently unoccupied ('-')
    if matrix[coordinates[0]][coordinates[1]] == '-':
        return True
    return False


# Start of the main game loop
start = input('Do you want to start the game? Y/N: ')

# Validate user input for starting the game
while start != 'Y' or start != 'N':
    if start == 'Y' or start == 'y':  # If user agrees to start the game
        # Reset the game board for a new session
        matrix = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]
        last_moved = None  # Track the last player who moved
        move_counter = 0  # Track the number of moves to detect a draw

        # Main gameplay loop
        while not check_if_game_ended():
            print_current_state()  # Display the current game state
            print('Input two digits')

            # Handle Player 1's move
            p1 = input('Player 1 move: ')
            # Validate Player 1's input
            while (not (len(p1) == 2 and p1[0] in '123' and p1[1] in '123')) and (
                    not (len(p1) == 3 and p1[0] in '123' and p1[2] in '123' and p1[1] == ' ')):
                print('Input two digits')
                p1 = input('Player 1 move: ')

            # Parse Player 1's input into row and column indices
            if ' ' in p1:
                p1 = [int(x) for x in p1.split()]
            else:
                p1 = [int(p1[0]), int(p1[1])]

            # Ensure Player 1's move is valid
            while not is_correct_move(p1):
                p1 = input('Player 1 move: ')
                while (not (len(p1) == 2 and p1[0] in '123' and p1[1] in '123')) and (
                        not (len(p1) == 3 and p1[0] in '123' and p1[2] in '123' and p1[1] == ' ')):
                    print('Input two digits')
                    p1 = input('Player 1 move: ')
                if ' ' in p1:
                    p1 = [int(x) for x in p1.split()]
                else:
                    p1 = [int(p1[0]), int(p1[1])]

            # Update the game board with Player 1's move
            matrix[p1[0]][p1[1]] = 'x'
            move_counter += 1  # Increment the move counter
            last_moved = 'Player 1'  # Update the last player who moved
            print_current_state()  # Display the updated game board

            # Check if Player 1 has won
            if check_if_game_ended():
                break

            # Check for a draw after 5 moves
            if move_counter == 5:
                print('Draw!')
                break

            print('Input two digits')

            # Handle Player 2's move
            p2 = input('Player 2 move: ')
            # Validate Player 2's input
            while (not (len(p2) == 2 and p2[0] in '123' and p2[1] in '123')) and (
                    not (len(p2) == 3 and p2[0] in '123' and p2[2] in '123' and p2[1] == ' ')):
                print('Input two digits')
                p2 = input('Player 2 move: ')

            # Parse Player 2's input into row and column indices
            if ' ' in p2:
                p2 = [int(x) for x in p2.split()]
            else:
                p2 = [int(p2[0]), int(p2[1])]

            # Ensure Player 2's move is valid
            while not is_correct_move(p2):
                p2 = input('Player 2 move: ')
                while (not (len(p2) == 2 and p2[0] in '123' and p2[1] in '123')) and (
                        not (len(p2) == 3 and p2[0] in '123' and p2[2] in '123' and p2[1] == ' ')):
                    print('Input two digits')
                    p2 = input('Player 2 move: ')
                if ' ' in p2:
                    p2 = [int(x) for x in p2.split()]
                else:
                    p2 = [int(p2[0]), int(p2[1])]

            # Update the game board with Player 2's move
            matrix[p2[0]][p2[1]] = 'o'
            last_moved = 'Player 2'  # Update the last player who moved
            temp = check_if_game_ended()  # Check if Player 2 has won

        print_current_state()  # Display the final game state

        # Announce the winner if no draw occurred
        if move_counter != 5:
            print(last_moved + ' wins!')

        move_counter = 0  # Reset the move counter for the next game
        start = input('Do you want to play again? Y/N: ')  # Prompt to start a new game
    elif start == 'N' or start == 'n':  # If user declines to play
        print('OK, bye!')
        break
    else:  # Handle invalid input for starting the game
        print('Input only "Y" or "N"')
        start = input('Do you want to start the game? Y/N: ')