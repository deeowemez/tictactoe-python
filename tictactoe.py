def display_board(a,b,c,d,e,f,g,h,i):
    # The function accepts parameters regarding different space status
    # and prints it out to the console.

    playing_board = (f"""
    +-------+-------+-------+
    |       |       |       |
    |   {a}   |   {b}   |   {c}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {d}   |   {e}   |   {f}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {g}   |   {h}   |   {i}   |
    |       |       |       |
    +-------+-------+-------+
    """)
    print(playing_board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = {}
    for j in range(3):
        for k in range(3):
            if board[j][k] != "O" and board[j][k] != "X":
                if (j,k) == (0,0):
                    free_fields[1] = [0,0]
                if (j,k) == (0,1):
                    free_fields[2] = [0,1]
                if (j,k) == (0,2):
                    free_fields[3] = [0,2]
                if (j,k) == (1,0):
                    free_fields[4] = [1,0]
                if (j,k) == (1,2):
                    free_fields[6] = [1,2]
                if (j,k) == (2,0):
                    free_fields[7] = [2,0]
                if (j,k) == (2,1):
                    free_fields[8] = [2,1]
                if (j,k) == (2,2):
                    free_fields[9] = [2,2]
    if free_fields == {}:
        print("Draw!")
        return False
##    print("Free Fields: ", free_fields)
    return free_fields

user_move = '1', '2', '3', '4', 'X', '6', '7', '8', '9'
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move_user = input("Enter your move: ")
            move_user = int(move_user)
            if move_user in list(free_space.keys()):
                a, b, c, d, e, f, g, h, i = user_move
                if move_user == 1:
                    a = board[0][0] = "O"
                elif move_user == 2:
                    b = board[0][1] = "O"
                elif move_user == 3:
                    c = board[0][2] = "O"
                elif move_user == 4:
                    d = board[1][0] = "O"
                elif move_user == 6:
                    f = board[1][2] = "O"
                elif move_user == 7:
                    g = board[2][0] = "O"
                elif move_user == 8:
                    h = board[2][1] = "O"
                else:
                    i = board[2][2] = "O"
                
                display_board(a,b,c,d,e,f,g,h,i)
                return a, b, c, d, e, f, g, h, i
            else:
                print("Space already taken. Invalid move!")
        except:
            print(f'Error: {move_user} is not a valid input.')

   

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (
        (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or
        (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or
        (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or
        (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or
        (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or
        (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or
        (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or
        (board[2][0] == sign and board[1][1] == sign and board[0][2] == sign)
    ):
        if sign == "O":
            print("Congratulations! \nPlayer: User -- You won!")
        if sign == "X":
            print("Congratulations! \nPlayer: Computer -- You won!")
        return True
    else: return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import randrange
    valid_move = False
    while not valid_move:
        comp_move = randrange(1,10)
##        print(comp_move)
        keys_list = list(free_space.keys())

        if comp_move in keys_list:
            [j,k] = free_space[comp_move] 
##            print("free_space[cm]: ", free_space[comp_move])
            board[j][k] = "X"
            a, b, c, d, e, f, g, h, i = user_move
            if [j,k] == [0,0]:
                a = "X"
            if [j,k] == [0,1]:
                b = "X"
            if [j,k] == [0,2]:
                c = "X"
            if [j,k] == [1,0]:
                d = "X"
            if [j,k] == [1,2]:
                f = "X"
            if [j,k] == [2,0]:
                g = "X"
            if [j,k] == [2,1]:
                h = "X"
            if [j,k] == [2,2]:
                i = "X"

            print("Computer's Move:")
            display_board(a,b,c,d,e,f,g,h,i)
            return a, b, c, d, e, f, g, h, i
        else:
            comp_move = randrange(1,10)
##            print("CM: ", comp_move)
            continue


def start_game(board):
    ##START OF GAME
    while True:
        global free_space
        global user_move
        free_space = make_list_of_free_fields(board)
        if free_space == False: break
        user_move = enter_move(board)
        vic_user = victory_for(board, "O")
        if vic_user == True: break
    ##    print("User move: ", user_move)
        free_space = make_list_of_free_fields(board)
        user_move = draw_move(board)
        vic_comp = victory_for(board, "X")
        if vic_comp == True: break

# Initialize playing board and display
def initialize_board():
    global board
    board = []
    empty = ""
    for i in range(3):
        row = [empty for i in range(3)]
        board.append(row)

    a = board[0][0] = "1"
    b = board[0][1] = "2"
    c = board[0][2] = "3"
    d = board[1][0] = "4"
    e = board[1][1] = "X"
    f = board[1][2] = "6"
    g = board[2][0] = "7"
    h = board[2][1] = "8"
    i = board[2][2] = "9"

    ##for row in board: print(row)
    ##print("board: ", board)
    display_board(a,b,c,d,e,f,g,h,i)
    start_game(board)

initialize_board()