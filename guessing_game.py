import random

def guessing_game():

    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    yes = "y"
    no = "n"
    choice = yes + no
    print ("I'm thinking of a number between 1 and 100. What is it?")
    print("You have 5 attempts")

    while attempts < 5:
        guess = int(input("Enter your number: "))
        if guess == number:
            print("You got it! Congrats!")
            choice = input("Do you want to play again? (y/n): ")
            if choice == no:
                print("Ok. Thanks for playing! =)")
            if choice == yes:
                guessing_game()
        elif guess < number:
            print("Nope! Too low! Try again.")
        elif guess > number:
            print("Nope! Too high! Try again.")

        attempts += 1

        if attempts == 5:
            print(f"Sorry, you ran out of attemtps. The number I was thinking was {number}.")

        elif guess < 0:
            print("Error: No negative numbers!")
            return
        elif guess > 100:
            print("Error: Cannot be greater than 100.")
            return

    choice = input("Do you want to play again? (y/n): ")

    if choice == no:
        print("Ok. Thanks for playing! =)")
    if choice == yes:
        guessing_game()
    
    
if __name__ == "__main__":
    guessing_game()
    
