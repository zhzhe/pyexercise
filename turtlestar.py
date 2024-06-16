import turtle as t 
#from turtle import *
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(150)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.done()