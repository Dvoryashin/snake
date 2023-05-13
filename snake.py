import time
import random
from tkinter import *
from tkinter import ttk

root = Tk()    
apple = 0
snake = []
snake_item = 20
snake_x = 12
snake_y = 12
len_snake = 1
speed = 0.1
t = 1
direction = ''


root.title("Приложение на Tkinter")   
root.geometry("500x600")  
root.resizable(0, 0)
canvas = Canvas(root,width=500,height=600,bg="black",cursor="pencil")
canvas.create_rectangle(3, 507, 497, 597, fill = "black", outline = "violet", width = 8)
score = canvas.create_text(480, 540, text=len_snake, fill='violet', font=('Helvetica 15 bold'))
canvas.pack()
root.update()

def create_item(canvas, x, y, fill):
    head = canvas.create_rectangle(snake_item * x, snake_item * y, snake_item * x + snake_item, snake_item * y + snake_item, fill=fill, outline="black")
    return head

rand_x = random.randint(0, 24)
rand_y = random.randint(0, 24)

snake.append(create_item(canvas, snake_x, snake_y, 'green'))
apple = create_item(canvas, rand_x, rand_y, 'red')

def move_snake(event, x, y, function_direction):
    global snake
    global snake_x
    global snake_y
    global len_snake
    global apple
    global speed
    global direction
    global score
    while 1 > 0:

        if direction == 'Up' and function_direction == 'Down':
            return 0
        if direction == 'Down' and function_direction == 'Up':
            return 0
        if direction == 'Left' and function_direction == 'Right':
            return 0
        if direction == 'Right' and function_direction == 'Left':
            return 0
        d = 1
        snake_x = snake_x + x
        snake_y = snake_y + y
        if snake_x == -1:

            snake_x = 24

        if snake_x == 25:

            snake_x = 0
        #
        if snake_y == -1:

            snake_y = 24

        if snake_y == 25:

            snake_y = 0

            
        for d in range(0, len(snake) - 1):
            if canvas.coords(snake[len(snake) - 1]) == canvas.coords(snake[d]):
                while 1 > 0:
                    time.sleep(10)

        snake.append(create_item(canvas, snake_x, snake_y, 'green'))
        if len(snake) > len_snake:
            while len(snake) > len_snake:
                canvas.delete(snake.pop(0))
                root.update()
                time.sleep(speed)
        
        if canvas.coords(apple) == canvas.coords(snake[len(snake) - 1]):
            canvas.delete(apple)
            len_snake = len_snake + 1
            canvas.delete(score)
            score = canvas.create_text(300, 50, text=len_snake, fill='violet', font=('Helvetica 15 bold'))
            speed = speed - 0.001
            rand_x = random.randint(0, 24)
            rand_y = random.randint(0, 24)
            apple = create_item(canvas, rand_x, rand_y, 'red')
        direction = function_direction


canvas.bind_all("<KeyPress-Up>", lambda event: move_snake(event, 0, -1, 'Up'))
canvas.bind_all("<KeyPress-Down>", lambda event: move_snake(event, 0, 1, 'Down'))
canvas.bind_all("<KeyPress-Left>", lambda event: move_snake(event, -1, 0, 'Left'))
canvas.bind_all("<KeyPress-Right>", lambda event: move_snake(event, 1, 0, 'Right'))

root.mainloop()


