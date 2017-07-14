#!/bin/python3
import pygal
piechart=pygal.Pie()
piechart.title='Favourite Pets'
piechart.add('Dog',6)
piechart.add('Cat',4)
piechart.add('Hamster',3)
piechart.add('Fish',2)
piechart.add('Snake',1)
#piechart.render()
barchart=pygal.Bar()
barchart.add('Dog',6)
barchart.add('Cat',4)
barchart.add('Hamster',3)
barchart.add('Fish',2)
barchart.add('Snake',1)
#barchart.render()
piechart2=pygal.Pie()
file=open('pets.txt','r')
for line in file.read().splitlines():
  label,value=line.split(" ")
  piechart2.add(label,int(value))
file.close()
piechart2.render()
