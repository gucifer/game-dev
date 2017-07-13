#!/bin/python3
from random import randint
import os
count='y'
while count=='y':
  choice=input('rock(r) or paper(p) or scissors(s)?')
  choice=str(choice)
  if(choice=='r'):
    print('O vs ',end='')
  elif(choice=='p'):
    print('Ll vs ',end='')
  elif(choice=='s'):
    print('8 vs ',end='')
  chosen=randint(1,3)
  #print(chosen)
  if(chosen==1):
    computer = 'r'
  elif(chosen==2):
    computer = 'p'
  elif(chosen==3):
    computer = 's'
  choice=str(choice)
  if(computer=='r'):
    print('O')
  elif(computer=='p'):
    print('Ll')
  elif(computer=='s'):
    print('8')
  if(choice==computer):
    print('DRAW!')
  elif(choice=='r' and computer=='p'):
    print('LOST!')
  elif(choice=='r' and computer=='s'):
    print('WIN!')
  elif(choice=='p' and computer=='r'):
    print('WIN!')
  elif(choice=='p' and computer=='s'):
    print('LOST!')
  elif(choice=='s' and computer=='r'):  
    print('LOST!')
  elif(choice=='s' and computer=='p'):
    print('WIN!')
  count = input('Do you want to continue playing(y or n)?')
  os.system('clear')
