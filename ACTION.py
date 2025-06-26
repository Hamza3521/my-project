

import random

display = []
words = ['hamza', 'nana', 'mama', 'baba']
random_choice = random.choice(words)
for i in random_choice:
  display.append('-')
print(display)
attemts=6
while '-'in display and attemts>0:
    count=0
    guessed=input('enter a guess ').lower()
    for n in range(len(random_choice)):
        if random_choice[n]==guessed:
            display[n]=guessed
            count+=1
    if count==0:
        attemts -=1                           
    print(display)
    print(f'you have attemts {attemts}')
if '-' not in display:
    print('''
    ***********
    YOU WIN
    ***********
    
    
    
    ''')
else:
    print('''
    
    <+---+>
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    
    
    
    ''')
    print(display)
    

    

    
    
  