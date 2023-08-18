# Navigator

# This project is a navigator that allows users to control a system using hand gestures and voice commands.

Files:

system_control_using_hand_gesture.py - This file contains the code for the hand gesture recognition system.
voice_assistant.py - This file contains the code for the voice assistant system.

How to Use
To use the navigator, first install the dependencies in the requirements.txt file. Then, run the following commands:

python system_control_using_hand_gesture.py
python voice_assistant.py

The hand gesture recognition system will start running in one terminal window. The voice assistant system will start running in another terminal window.

To control the system using hand gestures, make the appropriate gestures in front of the webcam. To control the system using voice commands, speak the appropriate commands into the microphone.

Contributing
Contributions to this project are welcome. Please submit your pull requests to the master branch.

# Steps are as follows :
## Steps for Hand Gesture
Step 1:Installing the anaconda
Step 2:Installing the python latest version
Step 3:Launch the vs code using the anaconda
Step 4:Open the folder where handgesture and voicegesture folder are stored.
Step 5:Steps for handgesture
       step 5(i): install the following libraries in terminal window 
                 pip install opencv-python
                 pip install mediapipe
                 pip install pyautogui
                 pip install ctypes
                 pip install comtypes
                 pip install pycaw
                 pip install screen-brightness-control
      step 5(ii):Run the Gesture_Controller.py file.

## Steps for voice-assistant
       step 6(a): install the following libraries in terminal window
                 pip install requests
                 pip install pyttsx3
                 pip install SpeechRecognition
                 pip install python-decouple
		 pip install pywhatkit
		 pip install wikipedia
 
       step 6(b) Create .env file and set the variables

       step 6(c): Run the main.py file.
                 
