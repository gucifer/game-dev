#!/bin/python3

import json
import turtle
import urllib.request
import time

url='http://api.open-notify.org/astros.json'
respose=urllib.request.urlopen(url)
reult=json.loads(respose.read())
print('People in space:',reult['number'])
people=reult['people']
for p in people:
  print(p['name'],' in ',p['craft'])
url='http://api.open-notify.org/iss-now.json'
respose=urllib.request.urlopen(url)
reult=json.loads(respose.read())
location=reult['iss_position']
lat=location['latitude']
lon=location['longitude']
print('Latitude: ',lat)
print('Longitude: ',lon)
screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')
screen.register_shape('iss.png')
iss=turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)
iss.penup()
iss.goto(lon,lat)
lat=29.5502
lon=-95.097
location=turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()
url='http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1'
respose=urllib.request.urlopen(url)
reult=json.loads(respose.read())
over=reult['response'][1]['risetime']
style=('Arial',6,'bold')
location.write(time.ctime(over),font=style)
