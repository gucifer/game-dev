#!/bin/python3
from turtle import *
from random import randint
import os
count='y'
wn = Screen()
while count=='y':
  os.system('clear')
  wn.reset()
  bet=input('Place your bet:red(r) or green(g) or blue(b) or yellow(y)')
  speed(20)
  penup()
  goto(-140,140)
  for step in range(15):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
  
  ada = Turtle()
  ada.color('red')
  ada.shape('turtle')
  ada.penup()
  ada.goto(-160,100)
  ada.pendown()
  bob = Turtle()
  bob.color('green')
  bob.shape('turtle')
  bob.penup()
  bob.goto(-160,70)
  bob.pendown()
  tim = Turtle()
  tim.color('blue')
  tim.shape('turtle')
  tim.penup()
  tim.goto(-160,40)
  tim.pendown()
  x = Turtle()
  x.color('yellow')
  x.shape('turtle')
  x.penup()
  x.goto(-160,10)
  x.pendown()
  for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    tim.forward(randint(1,5))
    x.forward(randint(1,5))
    if(ada.ycor()==140):
      print('Winner is red turtle',end='')
      if(bet=='r'):
        print('You win!')
      else:
        print('You Lose!')
      break;
    elif(bob.xcor()==140):
      print('Winner is green turtle')
      if(bet=='g'):
        print('You win!')
      else:
        print('You Lose!')
      break
    elif(tim.xcor()==140):
      print('Winner is blue turtle')
      if(bet=='b'):
        print('You win!')
      else:
        print('You Lose!')
      break
    elif(x.xcor()==140):
      print('Winner is yellow turtle')
      if(bet=='y'):
        print('You win!')
      else:
        print('You Lose!')
      break
  hideturtle()  
  count=input("Do you want to continue(y or n)?")
