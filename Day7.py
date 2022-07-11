import random
def process_guess(answer , guess):
    position = 0
    guide = ''
    for letter in guess:
        if letter == answer[position]:
            guide += "*"
        elif letter in answer:
            guide += '+'
        else:
            guide += 'x'
    print(guide)

hidden_word = ['water' , 'melon' , 'skate' , 'paper' , 'table']
answer = random.choice(hidden_word)

guesses = 0
guess_correct = False
while guesses < 6 and not guess_correct:
    guess = input('Enter your guess word:')
    guesses +=1

    guess_corect = process_guess(answer , guess)

if guess_correct:
    print("congratulations" + guess)

else:
    print('You lose...' + "The correct answer is:" + answer)