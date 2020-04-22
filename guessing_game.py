# Guessing game:
# User is able to guess numbers against a number set by your program
# If user enters anything other than number, user should be told
# There are 3 levels, easy, medium and hard
# At easy, Users get a chance to guess the number between 1 - 10, and the user gets 6 guesses
# Medium, the users is required to guess the number between 1 - 20, and the user gets 4 guesses
# Hard, users are required to guess between 1 - 50, and they only get 3 guesses
# User should be able to set the level they want to play
# Users should see how many guesses they have left after each guess
# If user guesses right, user should be told "You got it right!"
# If the user guesses wrong, user should be told "That was wrong"
# If users uses all available guessing power and still unable to guess right, user should be told "Game over!"
import random

print('''
Welcome to the Guessing Game:
    For Easy: Press E
    For Medium: Press M
    For Hard: Press H

Press Q to quit
''')

command = ""

while True:
    command = input("Please input a letter: ").upper()

    if command == "Q":
        break

    elif command == "E":
        guess_count = 0
        guess_limit = 6
        number_of_chances = 6
        min_num = 1
        max_num = 10

    elif command == "M":
        guess_count = 0
        guess_limit = 4
        number_of_chances = 4
        min_num = 1
        max_num = 20

    elif command == "H":
        guess_count = 0
        guess_limit = 3
        number_of_chances = 3
        min_num = 1
        max_num = 50

    else:
        print('''
    Please input either:
        E
        M
        H
    or Press Q to quit
    ''')
        continue

    secret_number = (random.randint(min_num,max_num))
    print(f'''
Guess a number between {min_num} and {max_num}
You have {number_of_chances} chances''')

    while guess_count < guess_limit:
        try:
            guess = float(input("Guess: "))
            guess_count += 1
            number_of_chances -= 1
            if guess == secret_number:
                print("You Got It Right!")
                break
            else:
                if number_of_chances > 0:
                    print(f'''
        That was wrong
        You have {number_of_chances} chances left''')
        except ValueError:
            print("Input must be an interger or a float")
    else:
        print("Game Over!")
    break
