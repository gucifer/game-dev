#!/bin/python3
alphabet='abcdefghijklmnopqrstuvwxyz'

newmessage=''
message=input('Please input a message(characters):')
key=input('Enter a key(number):')
typ=input('Encrypt(e) or Decrypt(d):')
if typ=='e':
  for char in message:
    if char in alphabet:
      pos=alphabet.find(char)
      newpos=pos+int(key)
      newchar=alphabet[newpos%26]
      newmessage+=newchar
    else:
      newmessage+=char
  print('The encrypted message is:',newmessage)
elif typ=='d':
  for char in message:
    if char in alphabet:
      pos=alphabet.find(char)
      newpos=pos-int(key)
      newchar=alphabet[newpos%26]
      newmessage+=newchar
    else:
      newmessage+=char
  print('The decrypted message is:',newmessage)
