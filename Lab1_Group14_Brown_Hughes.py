from rock_paper_scissors import play_rock_paper_scissors as rps
from guessing_game import guessing_game as gg

if __name__ == "__main__":
    print("Hi Thaddeus!  Welcome to our GitHub Repository for Partner Lab 1 Collaboration")
    while True:
        user_input = input("Which game would you like to play? Number Guessing Game (1) | Rock Paper Scissors (2) | NOTHING! I'M TIRED OF YOUR GAMES (0): ")
        
        if user_input.isdigit() != True:
            print("OPERATOR ERROR: Input must be a number!")
            continue

        user_input = int(user_input)

        if user_input == 0:
            print("Okay, have a nice day!")
            break
        elif user_input == 1:
            gg() # place holder for guessing game
        elif user_input == 2:
            rps()
        else:
            print("OPERATOR ERROR: Inavlid option :p")
