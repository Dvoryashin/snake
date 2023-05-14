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

class Snake:

    def __init__(self, canvas, root, snake, snake_x, snake_y, len_snake, apple, speed, direction, score):
        
        self.canvas = canvas
        self.snake = snake
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.len_snake = len_snake
        self.apple = apple
        self.speed = speed
        self.direction = direction
        self.score = score
        self.root = root

    def move_snake(self, event, x, y, function_direction):
        self.function_direction = function_direction
        while 1 > 0:

            if self.direction == 'Up' and self.function_direction == 'Down':
                return 0
            if self.direction == 'Down' and self.function_direction == 'Up':
                return 0
            if self.direction == 'Left' and self.function_direction == 'Right':
                return 0
            if self.direction == 'Right' and self.function_direction == 'Left':
                return 0
            d = 1
            self.snake_x = self.snake_x + x
            self.snake_y = self.snake_y + y
            if self.snake_x == -1:

                self.snake_x = 24

            if self.snake_x == 25:

                self.snake_x = 0
            #
            if self.snake_y == -1:

                self.snake_y = 24

            if self.snake_y == 25:

                self.snake_y = 0
                
            for d in range(0, len(self.snake) - 1):
                if self.canvas.coords(self.snake[len(self.snake) - 1]) == self.canvas.coords(self.snake[d]):
                    while 1 > 0:
                        time.sleep(10)

            self.snake.append(create_item(self.canvas, self.snake_x, self.snake_y, 'green'))
            if len(self.snake) > self.len_snake:
                while len(self.snake) > self.len_snake:
                    self.canvas.delete(self.snake.pop(0))
                    self.root.update()
                    time.sleep(self.speed)
            
            if self.canvas.coords(self.apple) == self.canvas.coords(self.snake[len(self.snake) - 1]):
                self.canvas.delete(self.apple)
                self.len_snake = self.len_snake + 1
                self.canvas.delete(score)
                self.score = self.canvas.create_text(300, 50, text=self.len_snake, fill='violet', font=('Helvetica 15 bold'))
                self.speed = self.speed - 0.001
                self.rand_x = random.randint(0, 24)
                self.rand_y = random.randint(0, 24)
                self.apple = create_item(self.canvas, self.rand_x, self.rand_y, 'red')
            self.direction = self.function_direction
        

snake = Snake(canvas, root, snake, snake_x, snake_y, len_snake, apple, speed, direction, score)

canvas.bind_all("<KeyPress-Up>", lambda event: snake.move_snake(event, 0, -1, 'Up'))
canvas.bind_all("<KeyPress-Down>", lambda event: snake.move_snake(event, 0, 1, 'Down'))
canvas.bind_all("<KeyPress-Left>", lambda event: snake.move_snake(event, -1, 0, 'Left'))
canvas.bind_all("<KeyPress-Right>", lambda event: snake.move_snake(event, 1, 0, 'Right'))

root.mainloop()
