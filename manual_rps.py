import random

words = ['rock', 'paper', 'scissors'] #list of options for the game

def get_computer_choice(word_list) -> str:
    computer_selection = random.choice(word_list)   # computer randomly selects its choice
    return computer_selection                       # the choice is returned

def get_user_choice() -> str :          
    u_choice = input("rock, paper or scissors?:")   # asks the user for a choice
    return u_choice                                 # returns the user's choice
  
def get_winner(computer_choice, user_choice):       # finds the winner given the two inputs

    print(f"Computer chose {computer_choice}")      # prints the computer's choice

    if computer_choice == 'rock' and user_choice == 'paper':    # conditions to find the winner
        print('You win')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('Computer wins')    
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print('Computer wins')
    elif computer_choice == 'scissors' and user_choice == 'rock':
        print('You win')    
    elif computer_choice == 'paper' and user_choice == 'scissors':
        print('You win')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print('Computer wins')   
    elif computer_choice == user_choice:
        print("It's a draw !!")     

def play():                                     # function to play the game
    c_choice = get_computer_choice(words)       # calling the function for computer's choice
    u_choice = get_user_choice()                # calling the function for user's choice
    get_winner(c_choice, u_choice)              # calling the function to find winner

play()                                          # finally calling the function to play the game!


