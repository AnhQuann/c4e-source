from turtle import *

width(5)

screensize(800, 800)

for index in range(10):
    if index % 2 == 0:
        color("red")
    else:
        color("blue")
    forward(20)
    penup()
    forward(20)
    pendown()

mainloop()
