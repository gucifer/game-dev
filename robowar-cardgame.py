#!/bin/python3
from turtle import *
from random import choice
screen=Screen()
screen.bgcolor('white')
penup()
hideturtle()
robots={}
file=open('cards.txt','r')
for line in file.read().splitlines():
  name,battery,intel,image=line.split(', ')
  robots[name]=[battery,intel,image]
  screen.register_shape(image)
file.close()
print(robots)
robot=input('Choose a robot:')
if(robot=='random'):
  robot=choice(robots.keys())
  print(robot)
if robot in robots:
  stats = robots[robot]
  style=('Arial',14,'bold')
  clear()
  goto(0,100)
  shape(stats[2])
  setheading(90)
  stamp()
  setheading(-90)
  forward(60)
  write('Name: '+ robot,font=style,align='center')
  forward(25)
  write('Battery: '+ stats[0],font=style,align='center')
  forward(25)
  write('Intelligence: '+ stats[1],font=style,align='center')
else:
  print('Robot does\'t exist.')
