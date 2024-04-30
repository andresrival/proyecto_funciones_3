import os
from tkinter import N
import keyboard

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    number = 0
    while number <= 50:
        clear_terminal()
        print("Número actual:", number)
        if keyboard.is_pressed('n'):
            number += 1

if __name__ == "__main__":
    main()
