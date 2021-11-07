import random
def guess_number():
    """
    This function  generates random number, then the user will be ask to enter the guess

    the function will compare guess and random number and then will tell to the user, if the guess was right or not

    there is a counter of guess tries

    and maybe some sort of score?


    """

while True:
    try:
        range = int(input("What range do you want to guess from?: "))
        print(".................................................")
        break;
    except ValueError:
        print("Please enter only whole number value.")
        print(".....................................")

number = random.randrange(0,range)
tries = 0
while True:

    try:
        guess = int(input("What is your guess?: "))
        print(".......................")
        if guess == number:
            tries += 1
            print("Great! Your guess is correct! You needed " + str(tries) + " tries to find an answer.")
            print("***************************************************************************************")
            print("Your score is: ", range / tries)
            break;
        else:
            if guess > number:
                print("Your guess is to high, go lower")
                print("*******************************")
                tries += 1
            elif guess < number:
                print("Your guess is to low, go higher")
                print("*******************************")
                tries += 1
    except ValueError:
        print("Please enter only whole number value.")
        print("**************************************")