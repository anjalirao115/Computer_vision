#%%
'''
This code is written for Computer Vision project. 
The code runs Rock, Paper, Scissors (RPS) game in two ways:
First way: the user selects his/her choice from rock, paper or scissors by giving his/her input on terminal
Second way: the user records his/her choice using hand gestures shown in webcam window.
'''

import cv2
from keras.models import load_model
import numpy as np
import time
import random


class Rps:
    def __init__(self):
        self.user = 0
        self.computer = 0

    def get_computer_choice(self,word_list) -> str:          # function to get computer's choice
        self.computer_selection = random.choice(word_list)   # computer randomly selects its choice
        return self.computer_selection                       # the choice is returned


    def get_user_choice(self) -> str :                      # function to get user's manual choice
        self.u_choice = input("Pick one: rock, paper or scissors: ")   # asks the user for a choice
        return self.u_choice                                 # returns the user's choice


    def get_winner(self, computer_choice, user_choice) -> tuple:       # finds the winner given the two inputs

        self.user_wins = 0                                   # variable defined to record victories in numbers
        self.computer_wins = 0                               # variable defined to record victories in numbers

        print(f"Computer chose {computer_choice}.")      # revealing the computer's choice

        if computer_choice == 'rock' and user_choice == 'paper':    # defining game logic and finding winner
            self.user_wins += 1
            print('You win this round')
        elif computer_choice == 'paper' and user_choice == 'rock':
            self.computer_wins += 1
            print('Computer wins this round.')    
        elif computer_choice == 'rock' and user_choice == 'scissors':
            self.computer_wins += 1
            print('Computer wins this round.')
        elif computer_choice == 'scissors' and user_choice == 'rock':
            self.user_wins += 1
            print('You win this round.')    
        elif computer_choice == 'paper' and user_choice == 'scissors':
            self.user_wins += 1
            print(f"You win this round.")
        elif computer_choice == 'scissors' and user_choice == 'paper':
            self.computer_wins += 1
            print(f"Computer wins this round.")   
        elif computer_choice == user_choice:
            print(f"This round is a draw !!")     

        return self.user_wins, self.computer_wins             # returns wins:::: 1 wins, 0 looses

    def countdown(self):                                    # function to initiate countdown
        self.tstart = time.time()                            # recording start time of countdown
        self.time_jump = 1                                   # time jump by 1 second
        self.time_left = 4                                   # duration of countdown in seconds

        while time.time()<=self.tstart+self.time_left+3:          # countdown prints within a time duration 
            if time.time()>=self.tstart+self.time_jump:           # counntdown begins
                print(f"Game starts in {self.time_left} seconds")
                self.time_jump += 1                          # time jumps by 1, 2, 3.. seconds from tstart
                self.time_left -= 1                          # time left decreases by 1


    def get_camera_choice(self) -> str:                     # function to get user's choice using camera

        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.time_start = time.time() 

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            #cv2.putText(frame, "hi", (100,100))
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if time.time()>self.tstart+15:                # camera closes 15 seconds after tstart
                break
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        prediction = prediction[0]                  # reading the model prediction

        if np.argmax(prediction) == 0:              # defining and printing the user's choice 
            self.u_choice = "rock"                  # 0, 1, 2, 3 are labels for four classes of models
            print("You chose rock")
        elif np.argmax(prediction) == 1:
            self.u_choice = "paper"
            print("You chose paper")    
        elif np.argmax(prediction) == 2:
            self.u_choice = "scissors"
            print("You chose scissors")    
        elif np.argmax(prediction) == 3:
            self.u_choice = "nothing"
            print("You chose nothing")    

        return self.u_choice                                 # returning the user's choice
    

def play():
    user_wins = 0
    computer_wins = 0

    n_wins = 3

    print("\nThis is a Rock-Paper-Scissors game.")
    print(f"Winner will be the one who gets {n_wins} victories \n")
    mode = input("\nSelect your input mode \n Type m for manual \n Type c for camera:  ")

    while True:
        game = Rps()                                # game is an instance of Rps class
        
        game.countdown()                            # making the instance do a task defined in the class
        game.get_computer_choice(word_lists)        
        c_choice = game.get_computer_choice(word_lists) # reading the output from function

        if mode=='m':
            u_choice = game.get_user_choice()               # to play game without camera
        if mode=='c':
            u_choice = game.get_camera_choice()             # to play game with camera

        winner = game.get_winner(c_choice, u_choice)

        user_wins = user_wins + winner[0]
        computer_wins = computer_wins + winner[1]

        print(f"The game score is You: {user_wins} and Computer: {computer_wins}")
        print()

        if user_wins==n_wins or computer_wins==n_wins:
            break

    if user_wins==n_wins:
        print("You win the game.\n")  

    else:
        print("Computer wins the game.\n")          


if __name__ == '__main__':
    word_lists = ['rock', 'paper', 'scissors']
    play()