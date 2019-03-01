from turtle import *

shape("turtle")
speed(-1)

for i in range(100):
    forward(10 + i * 4)
    left(90)

mainloop()
