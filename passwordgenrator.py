#!/bin/python3

import random
chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`-=[]\;\',./~!@#$%^&*()_+{}|:<>?"'
length=int(input('Password Length?'))
password=''
for c in range(length):
  password+=random.choice(chars)
print(password)
