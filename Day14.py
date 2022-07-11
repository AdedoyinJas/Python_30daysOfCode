import random
import math

def guess(answer, guess):
    answer = random.randint(1,50)
    count = 0
    while count < 6:
        count +=1
        guess = int(input('Guess a number between 1 and 50:'))
        if answer == guess:
            print('Congratulations you did it in' ,count , 'try')
            break
        elif answer > guess:
            print('You guessed too small')
        elif answer < guess:
            print('You guessed too high')
    if count >= 6:
        print('\nThe number is: ' + str(answer))
        print('\tBetter luck next time')


print(guess(30,5))







answer = random.randint(1,50)

def guess(answer, guess): 
    guess = ''
turns = 5
while turns < 5:
    if guess != answer:
        print('wrong')
    elif guess == answer:
        print("You won")
    else:
        print("quit")

print(guess(5, 4))