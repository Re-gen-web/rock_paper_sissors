from random import randint import time
  
player = input('rock (r), paper (p) or scissors (s)?')

time.sleep(5)

if player == 'r':
  print('O', end=' ')
  
elif player == 'p':
  print('___', end=' ')
  
elif player == 's':
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if chosen == 1 :
  computer = 'r'
  print('O')
  
elif chosen == 2 :
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if player == computer:
  print('DRAW!')
  time.sleep(5)
  
elif player == 'r' and computer == 's':
  print('Player wins!')
  time.sleep(5)
  
elif player == 'r' and computer == 'p':
  print('Computer wins!')
  time.sleep(5)
  
elif player == 'p' and computer == 'r':
  print('Player wins!')
  time.sleep(5)
  
elif player == 'p' and computer == 's':
  print('Computer wins!')
   time.sleep(5)

elif player == 's' and computer == 'p':
  print('Player wins!')
   time.sleep(5)
  
elif player == "s" and computer == 'r':
  print('Computer wins!')
  time.sleep(5)

else:
  print('Huh?')
  time.sleep(5)
