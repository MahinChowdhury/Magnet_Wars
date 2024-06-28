import numpy as np
import time


from tkinter import *

position = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# Mathematical grid
board = np.zeros((8, 8))  # 8x8 grid
BLACK = 1
WHITE = -1
turn = BLACK
GAMEOVER = False
choice=1

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def open_popup():
    global position
    position = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Mathematical grid
    global board,BLACK,WHITE,turn,GAMEOVER,choice
    board = np.zeros((8, 8))  # 8x8 grid
    BLACK = 1
    WHITE = -1
    turn = BLACK
    GAMEOVER = False
    choice=1

    def option1():
        global choice
        choice=1
        popup.destroy()

    def option2():
        global choice
        choice=2
        popup.destroy()

    def option3():
        global choice,turn
        choice=3
        turn=WHITE
        popup.destroy()
    
    # Create a new window (pop-up window)


    popup = Toplevel(root)
    popup.title("Choose game type")
    center_window(popup, 400, 250)
    popup.grab_set()
    popup.transient(root)  # Set the pop-up window as a temporary window for the root window
    popup.lift()  # Bring the pop-up window to the front
    popup.focus_force()  # Focus on the pop-up window
    
    # Add a label to the pop-up window
    frame11 = Frame(popup)
    frame11.pack()
    titleLabel1 = Label(frame11 , text="Choose game type" , font=("Arial" , 26) , bg="#63B8DE" , width=16 )
    titleLabel1.grid(row=0 , column=0)
    
    frame22 = Frame(popup , bg="yellow")
    frame22.pack()

    choiceButton1 = Button(frame22 , text="Player vs Player" , width=24 , height=1 , font=("Arial" , 20) , bg="#FFFDD0" , relief=RAISED , borderwidth=5 , command=option1 )
    choiceButton1.grid(row=0 , column=0)
    choiceButton2 = Button(frame22 , text="Player(Black) vs AI(White)" , width=24 , height=1 , font=("Arial" , 20) , bg="#FFFDD0" , relief=RAISED , borderwidth=5 , command=option2 )
    choiceButton2.grid(row=1 , column=0)
    choiceButton3 = Button(frame22 , text="Player(White) vs AI(Black)" , width=24 , height=1 , font=("Arial" , 20) , bg="#FFFDD0" , relief=RAISED , borderwidth=5 , command=option3 )
    choiceButton3.grid(row=2 , column=0)
    



def open_popup2(st):

    def option1():
        popup2.destroy()
        restartgame()
    popup2 = Toplevel(root)
    popup2.title("Results")
    center_window(popup2, 600, 130)
    popup2.grab_set()
    popup2.transient(root)  # Set the pop-up window as a temporary window for the root window
    popup2.lift()  # Bring the pop-up window to the front
    popup2.focus_force()  # Focus on the pop-up window
    
    # Add a label to the pop-up window
    frame11 = Frame(popup2)
    frame11.pack()
    titleLabel1 = Label(frame11 , text=st , font=("Arial" , 24) , bg="#63B8DE" , width=32 )
    titleLabel1.grid(row=1 , column=0,padx=10,pady=10)
    close_button = Button(popup2, text="Close",font = ("Arial",16) ,  bg="#A7C7E7" ,command=option1)
    close_button.pack(pady=10)
    

root = Tk()
center_window(root, 600, 780)
root.title("Magnet Wars")

root.resizable(0,0)

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1 , text="Magnet Wars" , font=("Arial" , 26) , bg="#5dbea3" , width=16 )
titleLabel.grid(row=0 , column=0)

frame2 = Frame(root)
frame2.pack(pady=10) 
frame2.pack()

open_popup()

def evaluate(board) -> int:
    window = np.array([0] * 5)  # Sliding Window of 5

    score = 0  # Score of the board currently
    # Horizontal windows of 5  checked
    for row in range(0, 8):
        for column in range(0, 4):
            window = board[row, column:column + 5]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[
                4]  # Score of the window
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:  # If 5 in a row of BLACK
                score += 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:  # If 5 in a row of WHITE
                score += -100000
    # Vertical windows of 5 checked
    for column in range(0, 8):
        for row in range(0, 4):
            window = board[row:row + 5, column]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[
                4]  # Score of the window
            if row > 0:
                if window[row - 1] == window[row] and window[row + 1] == window[row]:
                    score += (50 * window[row])
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:  # If 5 in a row of BLACK
                score += 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:  # If 5 in a row of WHITE
                score += -100000
    # Diagonal windows of 5 checked
    for row in range(4, 8):
        for column in range(0, 4):
            window = board[row - 4:row + 1, column:column + 5]
            score += 1 * window[0, 0] + 2 * window[1, 1] + 3 * window[2, 2] + 2 * window[3, 3] + 1 * window[
                4, 4]  # Score of the window diagonally positive
            score += 1 * window[4, 0] + 2 * window[3, 1] + 3 * window[2, 2] + 2 * window[1, 3] + 1 * window[
                0, 4]  # Score of the window diagonally negative
            if (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == 5 or (
                    window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == 5:
                score += 100000
            elif (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == -5 or (
                    window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == -5:
                score += -100000
    return score


def possible_moves(board: np.ndarray):  # Returns a set of possible moves
    moves = set()  # Set of possible moves
    for row in range(0, 8):
        for column in range(0, 8):
            if is_legal(row, column):  # If the move is legal
                moves.add((row, column))  # Add it to the set
                break
        for column in range(7, -1, -1):
            if is_legal(row, column):
                moves.add((row, column))
                break

    return list(moves)


def mini_max(current_board_position, depth_limit: int, max_turn: bool, depth: int, alpha,
             beta):  # Minimax algorithm with alpha beta pruning
    if max_turn:  # If it's the max turn then the turn is 1
        turn = 1
    else:  # If it's the min turn then the turn is -1
        turn = -1

    if depth == depth_limit:  # If the depth limit is reached then return the evaluation of the board and the board
        # print("Depth Limit Reached")
        return evaluate(current_board_position), current_board_position,

    elif is_over(current_board_position, turn):
        # print("--------------Is Over-----------------")
        return evaluate(current_board_position), current_board_position
    if max_turn:
        max_eval = -np.inf  # Max evaluation of the board
        best_move = [(0, 0)]

        for move in possible_moves(current_board_position):
            current_board_position[move[0], move[1]] = 1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, False, (depth + 1), alpha, beta)

            # print("MAX EVAL = ", evaluation, "DEPTH = ", depth)
            # print(".", end="")
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            max_eval = max(max_eval, evaluation)  # Max evaluation of the board

            if evaluation == max_eval:
                best_move = move

            alpha = max(alpha, max_eval)  # Alpha Beta Pruning

            if alpha >= beta:  # Pruning
                break

        return max_eval, best_move  # return the best move and the evaluation of the board
    else:

        min_eval = np.inf  # Min evaluation of the board
        best_move = [(0, 0)]  # dummy move

        for move in possible_moves(current_board_position):  # For all the possible moves
            current_board_position[move[0], move[1]] = -1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, True, (depth + 1), alpha,
                                       beta)  # Recursively call the minimax algorithm
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            min_eval = min(min_eval, evaluation)  # Min evaluation of the board

            if evaluation == min_eval:  # If the evaluation is the minimum evaluation
                best_move = move

            beta = min(beta, min_eval)

            if beta <= alpha:
                break

        return min_eval, best_move  # return the best move and the evaluation of the board


def make_move(board: np.ndarray, turn):  # Makes a move based on the minimax algorithm
    if turn == 1:  # If it's the max turn then the turn is 1
        max_turn = False
    else:  # If it's the min turn then the turn is -1
        max_turn = True

    move_eval, move_position = mini_max(board, 3, max_turn, 0, alpha=-np.inf,
                                        beta=np.inf)  # Minimax algorithm with alpha beta pruning
    row = move_position[0]  # Get the row and column of the move
    column = move_position[1]  # Get the row and column of the move
    board[row, column] = turn  # Place the piece on the board
    # print(row, column)
    print(row)
    print(column)
    if turn == BLACK:
        position[row][column] = "■"  # Place the piece on the grid
        buttons[row*8+column]["text"]="■"
    else:
        position[row][column] = "□"   # Place the piece on the grid
        buttons[row*8+column]["text"]="□"


#

# Method to print the grid
def print_grid():  # Prints the grid
    print("    A   B   C   D   E   F   G   H")
    for row in range(0, 8):
        print("  +---+---+---+---+---+---+---+---+")
        print(row + 1, "| ", end="")
        for column in range(0, 8):
            print(position[row][column], "| ", end="")
        print(row + 1)
    print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H")


# Method to check if the move wanted is legal
def is_legal(row, column):  # Checks if the move is legal
    # Checks if the space is empty
    if board[row, column] != 0:
        return False
    # Checks if it's at the edge of the board
    if column == 0 or column == 7:
        return True

    # Checks the column behind and in front to place a piece
    if board[row, column - 1] == 0 and board[row, column + 1] == 0:
        return False

    # If no rule violation occurs then it's legal
    return True


# Method to check if the game is over
def is_over(board, turn):  # Checks if the game is over
    # Checking for 5 in a row vertically
    # Checks all the possible places a 5 in a row could start
    for column in range(0, 8):
        for row in range(0, 4):
            if board[row, column] == turn \
                    and board[(row + 1), column] == turn \
                    and board[(row + 2), column] == turn \
                    and board[(row + 3), column] == turn \
                    and board[(row + 4), column] == turn:
                return True

    # Checking for 5 in a row horizontally
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 8):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[row, (column + 1)] == turn \
                    and board[row, (column + 2)] == turn \
                    and board[row, (column + 3)] == turn \
                    and board[row, (column + 4)] == turn:
                return True

    # Checking for 5 in a row positively diagonal
    # Checks all the possible places a 5 in a row could start
    for row in range(4, 8):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[(row - 1), (column + 1)] == turn \
                    and board[(row - 2), (column + 2)] == turn \
                    and board[(row - 3), (column + 3)] == turn \
                    and board[(row - 4), (column + 4)] == turn:
                return True

    # Checking for 5 in a row negatively diagonal
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 4):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[(row + 1), (column + 1)] == turn \
                    and board[(row + 2), (column + 2)] == turn \
                    and board[(row + 3), (column + 3)] == turn \
                    and board[(row + 4), (column + 4)] == turn:
                return True

    return False

def restartgame():
    print("hoise vai")
    for row in range(0,8):
        for column in range(0,8):
            buttons[row*8+column]["text"]=" "
    open_popup()







def play(event):
    global turn,GAMEOVER
    if GAMEOVER:
        return
    
    button = event.widget
    buttonText = str(button)
    print(buttonText)
    row = buttonText[-2]
    col = buttonText[-1]
    if col=='n':
        row=0
        col=0
    elif row=='n':
        col=int(col)
        row=col/8
        col=col%8
        if col==0:
            col=8
            row=0
        col=col-1
    else:
        val=int(row)
        val=val*10
        val2=int(col)
        val=val+val2
        row=val/8
        col=val%8
        if col==0:
            col=8
            row=row-1
        col=col-1
    row=int(row)
    col=int(col)
    print(row)
    print(col)
    print(choice)
    print(button["text"])
    if button["text"] == " ":
        print("yes")
        if choice == 1:
            if turn == BLACK:
                print("Black") 
                if col in range(0,8) and row in range(0, 8):
                    # Gets the value from the Hashmap based on the key entered
                    if is_legal(row, col):
                        position[row][col] = "■"
                        button["text"]="■"
                        board[row, col] = BLACK
                        turn = WHITE
                        GAMEOVER = is_over(board, BLACK)
                
                print_grid()
                print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    
                if GAMEOVER:
                    print('==============================================')
                    print("Black won!")
                    print('==============================================')
                    st="Player1(Black) Has Won The Game"
                    open_popup2(st)
                    #restartgame()
                if np.all(board):
                    st="The game finished in a draw"
                    open_popup2(st)
                    #restartgame()
                    print("Draw!")
            if turn == WHITE:
                
                if col in range(0,8) and row in range(0, 8):
                    if is_legal(row, col):
                        position[row][col] = "□"
                        button["text"]="□"
                        board[row, col] = WHITE
                        turn = BLACK
                        GAMEOVER = is_over(board, WHITE)
                    
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("White won!")
                        print('==============================================')
                        st="Player2(White) Has Won The Game"
                        open_popup2(st)
                        #restartgame()
                        
                    if np.all(board):
                        st="The game finished in a draw"
                        open_popup2(st)
                        #restartgame()
                        print("Draw!")

        elif choice == 2:  # Player vs AI
    
            if turn == BLACK:
                print(turn)
                if col in range(0,8) and row in range(0, 8):
                    
                    if is_legal(row, col):
                        position[row][col] = "■"
                        button["text"]="■"
                        board[row, col] = BLACK
                        turn = WHITE
                        GAMEOVER = is_over(board, BLACK)
                        print("done")
                    
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("Black won!")
                        print('==============================================')
                        st="Player(Black) Has Won The Game"
                        open_popup2(st)
                        #restartgame()
                    if np.all(board):
                        st="The game finished in a draw"
                        open_popup2(st)
                        #restartgame()
                        print("Draw!")
            if turn == WHITE:
                print("Loading Move")
                timer_start = time.time()
                make_move(board, WHITE)
                GAMEOVER = is_over(board, WHITE)
                # print('test1')
                print_grid()
                print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                timer_end = time.time()
                print(f'Time taken from AI = {timer_end - timer_start} Seconds')

                # print(board)

                turn = BLACK
                if GAMEOVER:
                    print('==============================================')
                    print("White won!")
                    print('==============================================')
                    st="AI(White) Has Won The Game"
                    open_popup2(st)
                    #restartgame()
                    
                if np.all(board):
                    st="The game finished in a draw"
                    open_popup2(st)
                    #restartgame()
                    print("Draw!")
        elif choice == 3:
        
            if turn == WHITE:
                    if col in range(0,8) and row in range(0, 8):
                        # Gets the value from the Hashmap based on the key entered
                        if is_legal(row, col):
                            position[row][col] = "□"
                            button["text"]="□"
                            board[row, col] = WHITE
                            turn = BLACK
                            GAMEOVER = is_over(board, WHITE)
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("White won!")
                        print('==============================================')
                        st="Player(White) Has Won The Game"
                        open_popup2(st)
                        #restartgame()
                    if np.all(board):
                        st="The game finished in a draw"
                        open_popup2(st)
                        #restartgame()
                        print("Draw!")
            if turn == BLACK:
                print("Loading Move")
                timer_start = time.time()
                make_move(board, BLACK)
                GAMEOVER = is_over(board, BLACK)
                print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                timer_end = time.time()
                print(f'Time taken from AI = {timer_end - timer_start} Seconds')  #

                # print(board)

                turn = WHITE
                if GAMEOVER:
                    print('==============================================')
                    print("Black won!")
                    print('==============================================')
                    st="AI(Black) Has Won The Game"
                    open_popup2(st)
                    #restartgame()
                    
                if np.all(board):
                    st="The game finished in a draw"
                    open_popup2(st)
                    #restartgame()
                    print("Draw!")
                    
        
                        

#first row
button11 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button11.grid(row = 0 , column=0)
button11.bind("<Button-1>" , play)

button12 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button12.grid(row = 0 , column=1)
button12.bind("<Button-1>" , play)

button13 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button13.grid(row = 0 , column=2)
button13.bind("<Button-1>" , play)

button14 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button14.grid(row = 0 , column=3)
button14.bind("<Button-1>" , play)

button15 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button15.grid(row = 0 , column=4)
button15.bind("<Button-1>" , play)

button16 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button16.grid(row = 0 , column=5)
button16.bind("<Button-1>" , play)

button17 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button17.grid(row = 0 , column=6)
button17.bind("<Button-1>" , play)

button18 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button18.grid(row = 0 , column=7)
button18.bind("<Button-1>" , play)

#second row
button21 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button21.grid(row = 1 , column=0)
button21.bind("<Button-1>" , play)

button22 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button22.grid(row = 1 , column=1)
button22.bind("<Button-1>" , play)

button23 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button23.grid(row = 1 , column=2)
button23.bind("<Button-1>" , play)

button24 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button24.grid(row = 1 , column=3)
button24.bind("<Button-1>" , play)

button25 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button25.grid(row = 1 , column=4)
button25.bind("<Button-1>" , play)

button26 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button26.grid(row = 1 , column=5)
button26.bind("<Button-1>" , play)

button27 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button27.grid(row = 1 , column=6)
button27.bind("<Button-1>" , play)

button28 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button28.grid(row = 1 , column=7)
button28.bind("<Button-1>" , play)

#third row
button31 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button31.grid(row = 2 , column=0)
button31.bind("<Button-1>" , play)

button32 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button32.grid(row = 2 , column=1)
button32.bind("<Button-1>" , play)

button33 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button33.grid(row = 2 , column=2)
button33.bind("<Button-1>" , play)

button34 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button34.grid(row = 2 , column=3)
button34.bind("<Button-1>" , play)

button35 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button35.grid(row = 2 , column=4)
button35.bind("<Button-1>" , play)

button36 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button36.grid(row = 2 , column=5)
button36.bind("<Button-1>" , play)

button37 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button37.grid(row = 2 , column=6)
button37.bind("<Button-1>" , play)

button38 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button38.grid(row = 2 , column=7)
button38.bind("<Button-1>" , play)

#fourth row
button41 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button41.grid(row = 3 , column=0)
button41.bind("<Button-1>" , play)

button42 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button42.grid(row = 3 , column=1)
button42.bind("<Button-1>" , play)

button43 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button43.grid(row = 3 , column=2)
button43.bind("<Button-1>" , play)

button44 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button44.grid(row = 3 , column=3)
button44.bind("<Button-1>" , play)

button45 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button45.grid(row = 3 , column=4)
button45.bind("<Button-1>" , play)

button46 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button46.grid(row = 3 , column=5)
button46.bind("<Button-1>" , play)

button47 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button47.grid(row = 3 , column=6)
button47.bind("<Button-1>" , play)

button48 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button48.grid(row = 3 , column=7)
button48.bind("<Button-1>" , play)

#fifth row
button51 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button51.grid(row = 4 , column=0)
button51.bind("<Button-1>" , play)

button52 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button52.grid(row = 4 , column=1)
button52.bind("<Button-1>" , play)

button53 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button53.grid(row = 4 , column=2)
button53.bind("<Button-1>" , play)

button54 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button54.grid(row = 4 , column=3)
button54.bind("<Button-1>" , play)

button55 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button55.grid(row = 4 , column=4)
button55.bind("<Button-1>" , play)

button56 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button56.grid(row = 4 , column=5)
button56.bind("<Button-1>" , play)

button57 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button57.grid(row = 4 , column=6)
button57.bind("<Button-1>" , play)

button58 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button58.grid(row = 4 , column=7)
button58.bind("<Button-1>" , play)

#sixth row
button61 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button61.grid(row = 5 , column=0)
button61.bind("<Button-1>" , play)

button62 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button62.grid(row = 5 , column=1)
button62.bind("<Button-1>" , play)

button63 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button63.grid(row = 5 , column=2)
button63.bind("<Button-1>" , play)

button64 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button64.grid(row = 5 , column=3)
button64.bind("<Button-1>" , play)

button65 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button65.grid(row = 5 , column=4)
button65.bind("<Button-1>" , play)

button66 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button66.grid(row = 5 , column=5)
button66.bind("<Button-1>" , play)

button67 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button67.grid(row = 5 , column=6)
button67.bind("<Button-1>" , play)

button68 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button68.grid(row = 5 , column=7)
button68.bind("<Button-1>" , play)


#seven row
button71 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button71.grid(row = 6 , column=0)
button71.bind("<Button-1>" , play)

button72 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button72.grid(row = 6 , column=1)
button72.bind("<Button-1>" , play)

button73 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button73.grid(row = 6 , column=2)
button73.bind("<Button-1>" , play)

button74 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button74.grid(row = 6 , column=3)
button74.bind("<Button-1>" , play)

button75 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button75.grid(row = 6 , column=4)
button75.bind("<Button-1>" , play)

button76 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button76.grid(row = 6 , column=5)
button76.bind("<Button-1>" , play)

button77 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button77.grid(row = 6 , column=6)
button77.bind("<Button-1>" , play)

button78 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button78.grid(row = 6 , column=7)
button78.bind("<Button-1>" , play)

#eight row
button81 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30) , bg="#F0FFFF" , relief=RAISED , borderwidth=3)
button81.grid(row = 7 , column=0)
button81.bind("<Button-1>" , play)

button82 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button82.grid(row = 7 , column=1)
button82.bind("<Button-1>" , play)

button83 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button83.grid(row = 7 , column=2)
button83.bind("<Button-1>" , play)

button84 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button84.grid(row = 7 , column=3)
button84.bind("<Button-1>" , play)

button85 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button85.grid(row = 7 , column=4)
button85.bind("<Button-1>" , play)

button86 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button86.grid(row = 7 , column=5)
button86.bind("<Button-1>" , play)

button87 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button87.grid(row = 7 , column=6)
button87.bind("<Button-1>" , play)

button88 = Button(frame2 , text= " " , width=2 , height=1  , font=("Arial" , 30), bg="#F0FFFF" , relief=RAISED , borderwidth=3 )
button88.grid(row = 7 , column=7)
button88.bind("<Button-1>" , play)


restartButton = Button(frame2 , text="Restart Game" , width=14 , height=1 , font=("Arial" , 20) , bg="#A7C7E7" , relief=RAISED , borderwidth=5 , command=restartgame )
restartButton.grid(row=8 , column=2 , columnspan=4,pady=10)

buttons = [button11 , button12 , button13 , button14 , button15 , button16 , button17 , button18,
           button21 , button22 , button23 , button24 , button25 , button26 , button27 , button28,
           button31 , button32 , button33 , button34 , button35 , button36 , button37 , button38,
           button41 , button42 , button43 , button44 , button45 , button46 , button47 , button48,
           button51 , button52 , button53 , button54 , button55 , button56 , button57 , button58,
           button61 , button62 , button63 , button64 , button65 , button66 , button67 , button68,
           button71 , button72 , button73 , button74 , button75 , button76 , button77 , button78,
           button81 , button82 , button83 , button84 , button85 , button86 , button87 , button88]

root.mainloop()
