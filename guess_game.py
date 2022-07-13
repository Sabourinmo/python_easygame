import random

def chooseRandNumber(difficulty = 10):
    secret_number = int(random.randint(0,difficulty))
    askQuestion(secret_number, "please write down a number\n")
    #return secret_number

def askQuestion(secret_number, question = "please write down a number\n"):
    print("Test to check secret number", secret_number)
    try: 
        input_number = int(input(question))
        main(input_number, secret_number)  

    except ValueError:
        print("Error please write down a number \n")
        askQuestion(secret_number) 
    
def main(input_number, secret_number):
    user_number = input_number
    if int(user_number) == int(secret_number):
        print(f"Congrats, you guess the correct number {secret_number}\n")
        replay = input(("Do you want to play again? (y/n)\n"))
        
        if replay.lower() == "y":
            chooseRandNumber(20)
        else:
            pass
    else:
        askQuestion(secret_number, "your were wrong, please write down another number \n")

chooseRandNumber()
