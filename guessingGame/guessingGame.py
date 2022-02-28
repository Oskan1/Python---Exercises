import random

def get_integer(prompt):
    """
    Get an integer from standart input from stdint

    The function will continue looping and prompting the user
    until a valid 'int' is entered.

    :param prompt: The string that the user will see, when
        they are prompted to enter the value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("You gave an invalid input")

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

#
help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")