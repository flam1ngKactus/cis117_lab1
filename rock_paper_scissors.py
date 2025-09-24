from random import randint

def play_rock_paper_scissors():
    """Plays a game of Rock-Paper-Scissors against the computer."""
    # Dictionary to map numbers to choices for easier display
    choices = {1: "paper", 2: "scissors", 3: "rock"}

    # Get the computer's choice
    computer_choice = randint(1, 3)
    computer_choice_name = choices[computer_choice]

    # Get the player's choice with input validation
    while True:
        try:
            player_choice = int(input("Enter your choice: 1. paper, 2. scissors, 3. rock: "))
            if player_choice in choices:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player_choice_name = choices[player_choice]
    
    # Display the choices
    print(f"\nYou chose: {player_choice_name}")
    print(f"The computer chose: {computer_choice_name}\n")

    # Determine the winner based on the game rules
    if player_choice == computer_choice:
        print("It's a tie!")
        
    # change statement to player_choice_name == "scissors" and computer_choice_namex == "paper"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("The computer wins!")