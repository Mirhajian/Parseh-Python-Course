import turtle as t

CELL_SIZE = 100
BOARD_SIZE = CELL_SIZE * 3
HALF = BOARD_SIZE / 2
SPOTS = []

def setup_screen():
    screen = t.Screen()
    screen.title("Tic-Tac-Toe Board")
    screen.bgcolor("black")
    return screen

def setup_pen():
    pen = t.Turtle()
    pen.speed(0) # 0 = fastest
    pen.hideturtle()
    pen.pensize(3)
    pen.color("white")
    return pen

def draw_line(pen, start, end):
    pen.penup()
    pen.goto(start)
    pen.pendown()
    pen.goto(end)
    pen.penup()

def canvas(pen):
    for i in range(4):
        x = -HALF + i * CELL_SIZE
        draw_line(pen, (x, -HALF), (x, HALF))
    
    for i in range(4):
        y = -HALF + i * CELL_SIZE
        draw_line(pen, (-HALF, y), (HALF, y))

def cell_center(row, col):
    x = -HALF + CELL_SIZE * col + CELL_SIZE / 2
    y = -HALF + CELL_SIZE * row + CELL_SIZE / 2
    return x, y

def draw_x(pen, row, col):
    cx, cy = cell_center(row, col)
    half = CELL_SIZE * 0.25
    draw_line(pen, (cx - half, cy - half), (cx + half, cy + half))
    draw_line(pen, (cx - half, cy + half), (cx + half, cy - half))


def draw_o(pen, row, col):
    cx, cy = cell_center(row, col)
    radius = CELL_SIZE * 0.25
    pen.penup()
    pen.goto(cx, cy - radius)
    pen.setheading(0)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

def reserve(move):
    try:
        for i in range(0, len(SPOTS)):
            if SPOTS[i][0] == move[0] and SPOTS[i][1] == move[1]:
                raise ValueError("This spot has been reserved.")
        
        SPOTS.append(move)
        print("Your move is now reserved.")
        return True
    
    except ValueError as error:
        print(f"Error: {error} Try again.")
        return False

# def check_move_number(move_number):
    # try:
    #     if int(move_number) >= 1 and int(move_number) <= 9:
    #         return True
    #     else:
    #         raise ValueError("Your number should be between 1 to 9")
    # except ValueError as error:
    #     print(f"Error: {error}, Try again.")
    #     return False
    
def check_move_number(move_number):
    try:
        num = int(move_number)  # اگه خطا داد، به except میره
    except ValueError:
        print("Error: Please enter a number between 1 and 9, Try again.")
        return False
    
    if 1 <= num <= 9:
        return True
    else:
        print("Error: Your number should be between 1 to 9, Try again.")
        return False

def check_count(count):
    if count < 8:
        return True
    else:
        print("Game Over. Result: Draw.")
        quit()

def check_win(shape):
    board = [[None, None, None] for _ in range(3)]

    for row, col, s in SPOTS:
        board[row][col] = s

    # check row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == shape:
            return True
    
    # check col
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == shape:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == shape:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == shape:
        return True
    
    return False


def main():
    screen = setup_screen()
    pen = setup_pen()
    canvas(pen)

    move_list = {"0": (2,0), "1": (2,1), "2": (2,2), "3": (1,0), "4": (1,1), "5": (1,2), "6": (0,0), "7": (0,1), "8": (0,2)}
    count = 0
    state = "Game On"
    shape = "x"
    while(True):
        while True:

            if count % 2 == 0:
                shape = "x"
            else:
                shape = "o"

            while True:
                move_number = input(f"Player {shape} your turn (1-9) or 'e' to exit: ").strip()
                
                if move_number.lower() == "e":
                    quit()
                
                if check_move_number(move_number):
                    break
            
            move_number = str(int(move_number) - 1)

            row = move_list[move_number][0]
            col = move_list[move_number][1]

            move = (row, col, shape)
        
            if reserve(move): # == True
                break

            

        t.pendown()
    
        if shape == "x":
            draw_x(pen, row, col)
        else:
            draw_o(pen, row, col)
        
        count = count + 1

        if check_win(shape):
            print(f"Player {shape}👑 won the game! 🎉")
            break
 
        if not check_count(count):
            break

    
    t.done()

main()