import tkinter as ttk
import tkinter as tk
window = tk.Tk()


rondes = 0
score = 0
import random


while rondes <= 20:
    rondes = rondes + 1
    guesses = 0
    number = random.randint(0, 100)

    print("Take a guess")
    while guesses <= 9:
        guess = int(input(""))
        guesses = guesses + 1
        
        if guess < number + 20 and guess > number -20:
            print("Je bent heel warm")
        elif guess < number + 50 and guess > number -50:
            print("Je bent warm")
        
        if guess < number:
            print("Je moet hoger raden")
        elif guess > number:
            print("Je moet lager raden")
        else:
            print("Je hebt het getal geraden!") 
            score = score + 1
            print(score)
            break
    antwoord = input("Wil je nog een keer gokken? J/N ") .upper()
    if antwoord == "J":
        print("")
    else:
        break