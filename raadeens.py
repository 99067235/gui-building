from tkinter import ttk
import tkinter
import random
from tkinter import messagebox

def askRetry(guessed):
    global amountOfTries, randomNumber, window
    retry = messagebox.askquestion("Information", f"You {guessed} the number.\nDo you want to guess a new number?")
    if retry:
        randomNumber = random.randint(0,1000)
        amountOfTries = 0
        infoVar.set("Guess the number between 0 and 1000")
    else:
        window.destroy()

amountOfTries = 0
def numberCheck():
    global amountOfTries,randomNumber
    try:
        if numberVar.get() >= 0 and numberVar.get() <= 1000:
            if randomNumber == numberVar.get() and amountOfTries < 10:
                askRetry("guessed")
            elif numberVar.get() < randomNumber and amountOfTries < 10:
                infoVar.set("The number is higher")
                amountOfTries += 1
            elif numberVar.get() > randomNumber and amountOfTries < 10:
                infoVar.set("The number is lower")
                amountOfTries += 1
            else:
                askRetry("didn't guess")
        else:
            infoVar.set("Please type a number between 0 and 1000")
    except:
        infoVar.set("Please type a number")
window = tkinter.Tk()
randomNumber = random.randint(0,1000)
infoVar = tkinter.StringVar(value="Guess the number between 0 and 1000")
infoLabel = tkinter.Label(window, textvariable=infoVar).pack()
numberVar = tkinter.IntVar()
guessBox = ttk.Entry(window, textvariable=numberVar).pack()
guessButton = tkinter.Button(window, text="Guess", command=numberCheck).pack()
window.mainloop()


# import random
# rondes = 0
# score = 0

# while rondes <= 20:
#     rondes = rondes + 1
#     guesses = 0
#     number = random.randint(0, 100)

#     print("Take a guess")
#     while guesses <= 9:
#         guess = int(input(""))
#         guesses = guesses + 1
        
#         if guess < number + 20 and guess > number -20:
#             print("Je bent heel warm")
#         elif guess < number + 50 and guess > number -50:
#             print("Je bent warm")
        
#         if guess < number:
#             print("Je moet hoger raden")
#         elif guess > number:
#             print("Je moet lager raden")
#         else:
#             print("Je hebt het getal geraden!") 
#             score = score + 1
#             print(score)
#             break
#     antwoord = input("Wil je nog een keer gokken? J/N ") .upper()
#     if antwoord == "J":
#         print("")
#     else:
#         break