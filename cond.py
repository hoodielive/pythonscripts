#!/usr/bin/env python3

guess_me = 7
answer = input("Please guess a number between 1 and 10\n")
answer = int(answer)

if answer < guess_me:
    print('Sorry the number you guess is lower than expected')
elif answer > guess_me:
    print('Sorry the number you chose was higher than expected')

elif answer <= guess_me:
    print('Bingo, you guessed correctly')

else:
    print('this game is not for you') 
