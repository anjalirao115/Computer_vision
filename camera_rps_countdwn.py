import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

import random

words = ['rock', 'paper', 'scissors'] #list of options for the game

def get_computer_choice(word_list) -> str:
    computer_selection = random.choice(word_list)   # computer randomly selects its choice
    return computer_selection                       # the choice is returned

def get_user_choice() -> str :          
    u_choice = input("rock, paper or scissors?:")   # asks the user for a choice
    return u_choice                                 # returns the user's choice

def countdown():
    tstart = time.time()
    time_jump = 1    # time jumps by 1 second
    time_left = 4   

    while time.time()<=tstart+time_left+3:
        if time.time()>=tstart+time_jump:
            print(f"Game starts in {time_left} seconds")
            time_jump += 1
            time_left -= 1

    return tstart        
 
def get_camera_choice() -> str:
    tstart = countdown()
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        #tstart=countdown()
        cv2.waitKey(1)
        # Press q to close the window
        print(prediction)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        if time.time()>tstart+8:
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    prediction = prediction[0]

    if np.argmax(prediction) == 0:
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

    return u_choice    
  
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
    u_choice = get_camera_choice()              # calling for user's camera choice
    #u_choice = get_user_choice()                # calling the function for user's choice
    get_winner(c_choice, u_choice)              # calling the function to find winner

play()                                          # finally calling the function to play the game!
    