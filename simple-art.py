#!/bin/python3

from turtle import *
from random import randint
speed(0)
def randomcolor():
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  color(r,g,b)
def randomplace():
  penup()
  x=randint(-100,100)
  y=randint(-100,100)
  goto(x,y)
  pendown()
def randomheading():
  a=randint(0,360)
  right(a)
def drawrectangle():
  randomcolor()
  randomplace()
  hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
def drawcircle():
  randomcolor()
  randomplace()
  hideturtle()
  rad=randint(10,100)
  dot(rad)
def drawstar():
  randomcolor()
  randomplace()
  begin_fill()
  size=randint(10,100)
  for side in range(5):
    left(144)
    forward(size)
  end_fill()
shape('turtle')
#for i in range(30):
#  randomcolor()
#  randomplace()
#  randomheading()
#  stamp()
clear()
setheading(0)
#for i in range(20):
#  drawrectangle()
#for i in range(20):
#  drawcircle()
#for i in range(20):
#  drawstar()
