import random

def chooseRandNumber(difficulty = 10):
    secret_number = int(random.randint(0,difficulty))
    askQuestion("please write down a number\n", secret_number)
    return secret_number

def askQuestion(question = "please write down a number\n", secret_number = 0):
    try: 
        input_number = int(input(question))
        main(input_number, secret_number)
        return input_number

    except ValueError:
        print("Error please write down a number \n")
        askQuestion(secret_number)

def main(input_number, secret_number):
    user_number = input_number
    print("secret key", secret_number)

    if int(user_number) == int(secret_number):
        print(f"Congrats, you guess the correct number {secret_number}\n")
        replay = input(("Do you want to play again? (y/n)\n"))
        
        if replay.lower() == "y":
            chooseRandNumber(20)
        else:
            pass
    else:
        askQuestion("your were wrong, please write down another number \n", secret_number)

chooseRandNumber()


        
