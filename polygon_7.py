from turtle import *

speed('fastest')
pencolor('yellow')
bgcolor('white')
pensize(10)
side = 6
size = 100
fillcolor('green')
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()