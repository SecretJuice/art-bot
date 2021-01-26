from playsound import playsound # playsound is a supposedly cross platform library that does nothing but plays a sound file. It's limited, but it's very simple and fufilled my needs
import serial # serial is the library used to look for input from the serial bus (aka, what you're actually looking for if you're here)
import random # used to randomly select a file
import os # used to get files in a path

ser = serial.Serial("COM3", 9600) # 'ser' is a variable set to Serial("COM3", 9600); COM3 being the port arduino is connected to and 9600 being the baud rate (same as arduino)

def play_random_from_folder(folder_name, asyncInt): # play_random_from_folder() accepts a folder_name string and an integer for whether or not to halt the code during audio playback

    random_file = random.choice(os.listdir(folder_name)) # chooses random file from specified folder string
    playsound(f"{folder_name}/{random_file}", asyncInt) # using the path (including folder name and name of file) to play the sound

while True:
    play_random_from_folder(ser.readline().decode('utf-8').strip(), 0) # calls the play_random_from_folder() function, passing in the current line from the serial bus that's been decoded from byte format and stripped of escape characters
