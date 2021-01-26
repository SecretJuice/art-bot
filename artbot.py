from playsound import playsound
import serial
import random
import os

ser = serial.Serial("COM3", 9600)

def play_random_from_folder(folder_name, asyncInt):

    random_file = random.choice(os.listdir(folder_name))
    playsound(f"{folder_name}/{random_file}", asyncInt)

while True:
    play_random_from_folder(ser.readline().decode('utf-8').strip(), 0)
