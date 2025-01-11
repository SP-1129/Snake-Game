from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 90
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "green"
FOOD_COLOUR = 'red'
BACKGROUND_COLOUR = 'black' 

class snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x +SPACE_SIZE , y + SPACE_SIZE, fill=SNAKE_COLOUR, tag='snake')
            self.square.append(square)



class food:
    def __init__(self):

        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag='food')

def next_turn(snake, turn):
    x, y = snake.coordinates[0]

    if direction == "up":
        y-=SPACE_SIZE
    elif direction == "down":
        y+=SPACE_SIZE
    elif direction == "left":
        x-=SPACE_SIZE
    elif direction == "right":
        x-=SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.square.insert(0, square)

    del snake.coordinates[-1]

    canvas.delete(snake.square[-1])

    del snake.square[-1]

    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def game_over():
    pass

window = Tk()
window.title("Snake Game")

score = 0
direction = 'down'

label = Label(window, text="score:".format(score), font=('consoles',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()                       #screen to be in the middle
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = snake()
food = food()
next_turn(snake , food)


window.mainloop()


