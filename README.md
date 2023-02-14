# Computer Vision : for Rock-Paper-Scissors game


## Milestone 1
As a first step, an image project model is created using [Teachable-Machine](https://teachablemachine.withgoogle.com/). The model is created to have four different classes: Rock, Paper, Scissors, Nothing.

Each class is trained with hundreds of images of a person (me, in this case) showing each option to the camera. The "Nothing" class represents the lack of option in the image. The model is then downloaded, and the two files
1. keras_model.h5
2. labels.txt : a text file containing the labels

are provided here in the repository.

This model is used to make a game which allows users to play Rock-Paper-Scissors against the Computer.

## Milestone 2

I created a conda environment and installed opencv-python, tensorflow, and ipykernel. The code is run in this environment. All the requirements to set up this environment are saved in 'requirements.txt' provided here in the repository. These dependencies for the environment can be easily installed using the command:

pip install requirements.txt

## Milestone 3
The basic logic of the game is developed to find the winner provided the user's and computer's choice. The code is provided here. 

```
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

play() 
```


## Milestone 4

The code is further developed using the above mentioned logic and the following features are included:

1. Displayed a countdown before starting a game
2. The game is repeated until either the computer or the user wins three rounds

By this stage, the user selects his/her input (rock, paper, or scissors) by manually typing it on the terminal. The function 'get_user_choice' performs this task. 

## Milestone 5

The code is further developed to accept the user's choice using webcam. A method 'get_camera_choice' performs this task. The user gestures his/her choice in the webcam window and model predicts the input and compares it with the computer's choice in the game logic to find the winner.

The final code 'rps.py' integrates both the ways in which a user can input his/her choice. When the code is run, it first asks the user if he/she wants to play in manual (type m) or camera (type c) mode. Once the mode is selected, the code call the methods 'get_user_choice' or 'get_camera_choice' accordinly and the game begins!