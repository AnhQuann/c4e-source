from turtle import *

shape('turtle')
speed(-1)

color('blue')
pensize('2')

for i in range(6):
    for i in range(4):
        for i in range(4):
            forward(150)
            left(90)
        left(90)

    left(15)

mainloop()
