rom time import *
import random
from tkinter import *
from tkinter import ttk

root = Tk()    
cell_x = 0
cell_y = 0
arr_cells_x = []
arr_cells_y = []  
head = 0
apple = 0


root.title("Приложение на Tkinter")   
root.geometry("500x500")  
canvas = Canvas(root,width=500,height=500,bg="black",cursor="pencil")
canvas.pack()

for i in range(8):
    for i in range(8):
        canvas.create_rectangle(cell_x, cell_y, cell_x + 62.5, cell_y + 62.5, fill="black", outline="blue") 
        arr_cells_x.append(cell_x)
        arr_cells_y.append(cell_y)
        cell_x = cell_x + 62.5
    cell_x = 0
    cell_y = cell_y + 62.5

def create_head(head_x, head_y):
    head = canvas.create_rectangle(head_x, head_y, head_x + 62.5, head_y + 62.5, fill="blue", outline="blue")
    return head

def create_apple():
    rand_x = random.randint(0, len(arr_cells_x) - 1)
    rand_y = random.randint(0, len(arr_cells_y) - 1)
    apple = canvas.create_rectangle(arr_cells_x[rand_x], arr_cells_y[rand_y], arr_cells_x[rand_x] + 62.5, arr_cells_y[rand_y] + 62.5, fill="red", outline="blue")
    return apple


head = create_head(312.5, 312.5)
apple = create_apple()

def move_snake(event, x, y):
    canvas.move(head, x, y)
    # head_x = canvas.coords(head)[0]
    # head_y = canvas.coords(head)[1]
    canvas.delete("all")

    # for i in range(8):
    #     for i in range(8):
    #         canvas.create_rectangle(cell_x, cell_y, cell_x + 62.5, cell_y + 62.5, fill="black", outline="blue") 
    #         arr_cells_x.append(cell_x)
    #         arr_cells_y.append(cell_y)
    #         cell_x = cell_x + 62.5
    #     cell_x = 0
    #     cell_y = cell_y + 62.5

    # head = create_head(head_x, head_y)
    # apple = create_apple()
    # if canvas.coords(apple) == canvas.coords(head):
    #     canvas.delete("all")

root.update()
canvas.bind_all("<KeyPress-Up>", lambda event: move_snake(event, 0, -62.5))
canvas.bind_all("<KeyPress-Down>", lambda event: move_snake(event, 0, 62.5))
canvas.bind_all("<KeyPress-Left>", lambda event: move_snake(event, -62.5, 0))
canvas.bind_all("<KeyPress-Right>", lambda event: move_snake(event, 62.5, 0))

root.mainloop()

# canvas.delete("all")
# head_pos = canvas.coords(head)






