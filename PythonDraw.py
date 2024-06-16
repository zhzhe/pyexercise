#PythonDraw.py
import turtle as t
#建立画布
t.setup(700,350,400,400)
#让小海龟起飞，即把笔提起来（这样，小海龟只移动，不画画）
t.penup()

t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("orange")
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done()