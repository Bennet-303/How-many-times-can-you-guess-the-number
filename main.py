from random import randint
# import functions from score_keeper

while(True):
    print("Guess the number!")
    hidden_number = randint(1, 10)
    print("Enter any number from 1 to 10 or 0 to close the game: ")
    guessNumber = int(input())

    if guessNumber == hidden_number :
        print("You guessed correctly!")
    elif guessNumber == 0:
        break
    else:
        print(f"The correct number is {hidden_number}")

    close_game = input("Do you want to play again? y/n: ")
    if (close_game == "n"):
        break
