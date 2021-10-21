import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print('Opps...Sorry, guess again. Too small.')
        elif guess > random_number:
            print('Opps...Sorry, guess again. Too big.')

    print(f'Yessir,you can have a cookie... congrats. You have guessed the number {random_number} ')

def computer_guess(x):
    small = 1
    big = x
    feedback = ''
    while feedback != 'c':
        if small !=big:
           guess = random.randint(small, big)
        else:
            guess = small #could also be big b/c small = big
        feedback = input(f'Is {guess} too big (B), too small (S), or correct (C)?? ').lower()
        if feedback =='h':
            big = guess - 1
        elif feedback == 'l' :
            small = guess + 1   

    print(f'Yesssir! The computer guessed your number, {guess}, correctly!')       


computer_guess(100)        