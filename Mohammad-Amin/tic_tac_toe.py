import turtle as t

CELL_SIZE = 100
BOARD_SIZE = CELL_SIZE * 3
HALF = BOARD_SIZE / 2

def setup_screen():
    screen = t.Screen()
    screen.title("Tic-Tac-Toe Board")
    screen.bgcolor("black")
    return screen

def setup_pen():
    pen = t.Turtle()
    pen.speed(5)
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
        print(i)
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


def main():
    screen = setup_screen()
    pen = setup_pen()
    canvas(pen)

    state = 1
    while(state == 1):
        row = int(input("Enter row: ")) # row
        col = int(input("Enter column: ")) # column

        t.pendown()

        shape = input("enter x for cross and o for circle: ")
        if shape == "x":
            draw_x(pen, row, col)
        else:
            draw_o(pen, row, col)

        state = int(input("do you want to continue? "))
    t.done()

main()