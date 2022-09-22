import random

words = ['rock', 'paper', 'scissors']

def get_computer_choice(word_list) -> str:
    computer_selection = random.choice(word_list)
    return computer_selection 

def get_user_choice() -> str :
    u_choice = input("rock, paper or scissors?:")
    return u_choice

def get_winner(computer_choice, user_choice):

    computer_choice = get_computer_choice(words)
    user_choice = get_user_choice()

    print(f"Computer chose {computer_choice}") 

    if computer_choice == 'rock' and user_choice == 'paper':
        print('user wins')
    elif computer_choice == 'paper' and user_choice=='rock':
        print('computer wins')    
    elif computer_choice == 'rock' and user_choice=='scissors':
        print('computer wins')
    elif computer_choice == 'scissors' and user_choice=='rock':
        print('user wins')    
    elif computer_choice == 'paper' and user_choice=='scissors':
        print('user wins')
    elif computer_choice == 'scissors' and user_choice=='paper':
        print('computer wins')   
    elif computer_choice == user_choice:
        print("It's a draw !!")     
       
get_winner(c_choice, u_choice)



