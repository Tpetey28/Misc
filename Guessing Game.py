#!/usr/bin/env python
# coding: utf-8

# In[29]:


import random

def guessing_game(num):
    guess = 0
    random_num = random.randint(1, num)
    guess = int(input('Guess a number between 1 and {}: '.format(num)))
    
    count = 0
    while guess != random_num:
        if guess < random_num:
            print('Too low! Guess again!\n')
            count += 1
            guess = int(input('Guess a number between 1 and {}: '.format(num)))
        elif guess > random_num:
            print('Too high! Guess again!\n')
            count +=1
            guess = int(input('Guess a number between 1 and {}: '.format(num)))
    count +=1
    print('Congrats! You guessed the correct number {}! It only took {} tries!'.format(random_num, count))
    

guessing_game(10)


# In[ ]:




