import turtle as t
t.speed(5)
colors=['red','blue']
t.shape('turtle')

for x in range(1,14):
 t.color(colors[x%2])
 t.begin_fill()
 for _ in range(4):
    t.fd(100)
    t.lt(360/4)
 t.end_fill()
 t.seth(30*x)
t.done()
 
