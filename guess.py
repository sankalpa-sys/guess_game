import random
def guessing_game():
    number = random.randint(0, 10)
    guess = 1
    while True:
        guessed_number = input("Guess a number : ")
        if guessed_number > number:
            print("You guessed high, Choose a smaller number")
            guess += 1
        elif guessed_number < number:
            print("you guessed low, Choose a bigger number")
            guess += 1
        else:
            print("You won and you guessed in" + " " + str(guess) + " " "times")
            break
guessing_game()

def play_again():
    while True:
        print("Do you want to play again? :")
        choice = input("Type 1 to play again and 2 to quit the game : ")
        if choice == 1:
            guessing_game()
        elif choice != 2:
            print("you have given wrong input. Type 1 for Yes and 2 for No")
            play_again()
        else:
            break
play_again()

