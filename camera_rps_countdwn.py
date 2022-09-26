import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

import random

words = ['rock', 'paper', 'scissors'] #list of options for the game

def get_computer_choice(word_list) -> str:          # function to get computer's choice
    computer_selection = random.choice(word_list)   # computer randomly selects its choice
    return computer_selection                       # the choice is returned

def get_user_choice() -> str :                      # function to get user's manual choice
    u_choice = input("rock, paper or scissors?:")   # asks the user for a choice
    return u_choice                                 # returns the user's choice

def countdown():                                    # function to initiate countdown
    tstart = time.time()                            # recording start time of code
    time_jump = 1                                   # time jump by 1 second
    time_left = 4                                   # duration of countdown in seconds

    while time.time()<=tstart+time_left+3:          # countdown prints within a time duration 
        if time.time()>=tstart+time_jump:           # counntdown begins
            print(f"Game starts in {time_left} seconds")
            time_jump += 1                          # time jumps by 1, 2, 3.. seconds from tstart
            time_left -= 1                          # time left decreases by 1

    return tstart                                   # taking out this tstart to limit the camera opening duration
 
def get_camera_choice() -> str:                     # function to get user's choice using camera
    tstart = countdown()                            # starting countdown and reading tstart
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        print(prediction)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        if time.time()>tstart+8:                # camera closes 8 seconds after tstart with a countdown of 4 seconds
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    prediction = prediction[0]                  # reading the model prediction

    if np.argmax(prediction) == 0:              # defining and printing the user's choice 
        u_choice = "rock"
        print("You chose rock")
    elif np.argmax(prediction) == 1:
        u_choice = "paper"
        print("You chose paper")    
    elif np.argmax(prediction) == 2:
        u_choice = "scissors"
        print("You chose scissors")    
    elif np.argmax(prediction) == 3:
        u_choice = "nothing"
        print("You chose nothing")    

    return u_choice                                 # returning the user's choice
  
def get_winner(computer_choice, user_choice):       # finds the winner given the two inputs

    user_wins = 0                                   # variables defined to get three victories
    computer_wins = 0                               # variables defined to get three victories

    print(f"Computer chose {computer_choice}")      # revealing the computer's choice

    if computer_choice == 'rock' and user_choice == 'paper':    # defining game logic and finding winner
        user_wins += 1
        print('You win')
    elif computer_choice == 'paper' and user_choice == 'rock':
        computer_wins += 1
        print('Computer wins')    
    elif computer_choice == 'rock' and user_choice == 'scissors':
        computer_wins += 1
        print('Computer wins')
    elif computer_choice == 'scissors' and user_choice == 'rock':
        user_wins += 1
        print('You win')    
    elif computer_choice == 'paper' and user_choice == 'scissors':
        user_wins += 1
        print('You win')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        computer_wins += 1
        print('Computer wins')   
    elif computer_choice == user_choice:
        print("It's a draw !!")     

    return user_wins, computer_wins             # returned wins:::: 1 wins, 0 looses

def play():                                     # function to play the game
    c_choice = get_computer_choice(words)       # calling the function for computer's choice
    u_choice = get_camera_choice()              # calling for user's camera choice
    #u_choice = get_user_choice()               # calling the function for user's manual choice
    user_wins,computer_wins = get_winner(c_choice, u_choice)              # calling the function to find winner
    return user_wins, computer_wins


# Finallly playing the game repeatedly until three victories are achieved:

user_win_list = []          # collecting winning records in a list
computer_win_list= []       # collecting winning records in a list

while True:
    u, c = play()           # u for user, c for computer
    print(u,c)
    user_win_list.append(u)
    computer_win_list.append(c)
    user_sum = sum(user_win_list)
    computer_sum = sum(computer_win_list)

    if user_sum==3 or computer_sum==3:
        break

    if user_sum == 3:
        print("You win !!")

    if computer_sum == 3:
        print("Computer wins !!")    

    
