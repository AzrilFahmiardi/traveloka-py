import os
import keyboard
import time


def pause():
    print("\nTekan Enter untuk kembali ke menu utama...")
    while keyboard.is_pressed('enter'):
        pass
    while not keyboard.is_pressed('enter'):
        time.sleep(0.05)
    while keyboard.is_pressed('enter'):
        pass

def pesawat(index):
    os.system("cls")
    print("pesawat")
    print("COMING SOON")
    
    pause()