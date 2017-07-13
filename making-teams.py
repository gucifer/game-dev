#!/bin/python3;
from random import choice
players=['a','b','c','d','e']
ta=[]
tb=[]
while len(players)>0:
  pa=choice(players)
  ta.append(pa)
  players.remove(pa)
  if len(players)==0:
    break;
  pb=choice(players)
  tb.append(pb)
  players.remove(pb)
print(ta)
print(tb)
