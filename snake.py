from time import *
import random
from tkinter import *
from tkinter import ttk

root = Tk()    

root.title("Приложение на Tkinter")   
root.geometry("500x500")  
canvas = Canvas(root,width=500,height=500,bg="black",cursor="pencil")
canvas.pack()

cell_x = 0
cell_y = 0
arr_cells_x = []
arr_cells_y = []  

for i in range(8):
    for i in range(8):
        canvas.create_rectangle(cell_x, cell_y, cell_x + 62.5, cell_y + 62.5, fill="black", outline="blue") 
        arr_cells_x.append(cell_x)
        arr_cells_y.append(cell_y)
        cell_x = cell_x + 62.5
    cell_x = 0
    cell_y = cell_y + 62.5
cell_x = 62.5

head = canvas.create_rectangle(312.5, 312.5, 375, 375, fill="blue", outline="blue")

rand_x = random.randint(0, len(arr_cells_x) - 1)
rand_y = random.randint(0, len(arr_cells_y) - 1)

apple = canvas.create_rectangle(arr_cells_x[rand_x], arr_cells_y[rand_y], arr_cells_x[rand_x] + 62.5, arr_cells_y[rand_y] + 62.5, fill="red", outline="blue")

apple_pos = canvas.coords(apple)
head_pos = canvas.coords(head)

if head_pos == apple_pos:
    print('ahaha')

def move_up(event):
    canvas.move(head, 0, -62.5)
    if head_pos == apple_pos:
        canvas.move(appple, 0, -62.5)
def move_down(event):
    canvas.move(head, 0, 62.5)
def move_left(event):
    canvas.move(head, -62.5, 0)
def move_right(event):
    canvas.move(head, 62.5, 0)

root.update()
canvas.bind_all("<KeyPress-Up>", move_up)
canvas.bind_all("<KeyPress-Down>", move_down)
canvas.bind_all("<KeyPress-Left>", move_left)
canvas.bind_all("<KeyPress-Right>", move_right)



root.mainloop()





