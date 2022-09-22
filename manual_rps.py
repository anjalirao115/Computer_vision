import random

words = ['rock', 'rock', 'rock']

def get_computer_choice(word_list) -> str:
    computer_selection = random.choice(word_list)
    return computer_selection

c_choice = get_computer_choice(words)  
#print(c_choice)  

def get_user_choice() -> str :
    u_choice = input("rock, paper or scissors?:")
    return u_choice

u_choice = get_user_choice()
#print(u_choice)

def get_winner(computer_choice, user_choice):
    #print(f"Computer chose {c_choice}")
    print(f"Computer chose {get_computer_choice(words)}")

    #user_choice = get_user_choice()

    if get_computer_choice(words) == 'rock' and u_choice == 'paper':
        print('user wins')
    #elif computer_choice == 'paper' and user_choice=='rock':
        #print('computer wins')    
    #elif computer_choice == 'rock' and user_choice=='scissors':
        #print('computer wins')
    #elif computer_choice == 'scissors' and user_choice=='rock':
        #print('user wins')    
    #elif computer_choice == 'paper' and user_choice=='scissors':
        #print('user wins')
    #elif computer_choice == 'scissors' and user_choice=='paper':
        #print('computer wins')   
    #elif computer_choice == user_choice:
        #print("It's a draw !!")     
       
get_winner(c_choice, u_choice)



