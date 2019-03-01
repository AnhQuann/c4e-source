from turtle import *

shape('turtle')
speed(-1)

color('blue')
pensize('2')

length = 20

for i in range(50):
    for i in range(4):
        forward(length)
        left(90)

    length += 5
    left(10)

mainloop()
