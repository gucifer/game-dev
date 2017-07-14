#!/bin/python3
print('Friendship Calculator')
f1=input('Enter first friend:')
f2=input('Enter second friend:')
score=0
for char in f1:
  if char in 'aeiouAEIOU':
    score+=5
  elif char in 'friendFRIEND':
    score+=10
for char in f2:
  if char in 'aeiou':
    score+=5
  elif char in 'friend':
    score+=10
print('Your friendship score is:',score)
