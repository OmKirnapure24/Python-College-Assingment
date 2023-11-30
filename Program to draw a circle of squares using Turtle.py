import turtle
t = turtle.Turtle()

t.speed(10)
t.color("blue")
def draw_square():
  for i in range(4):
    t.forward(100)
    t.right(90)
for i in range(36):
  draw_square()
  t.left(10)
turtle.done()
