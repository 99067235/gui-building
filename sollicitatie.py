from pydoc import describe
import tkinter as ttk
import tkinter as tk
from tkinter import E, ttk
import tkinter
from tkinter import messagebox

window = tk.Tk()
window.geometry("340x250")
question = 0

def config(var1, var2):
    r1.configure(text=var1, value=var1)
    r2.configure(text=var2, value=var2)

def sorry():
    messagebox.showinfo("Sorry", "Sorry, u bent niet geschikt voor het beroep ruimtevuilnisman")
    window.destroy()

def destroy():
    passedWindow.destroy()

def checkAnswer(*args):
    global passedWindow
    passed = False
    global question, s1
    if question == 0 and answerSpin.get() != "":
        if answerSpin.get() >=4:
            question = 1
            questionVar.set("Bent u in het bezit van een diploma MBO 4 ondernemen?")
            r1.grid(column=1, row=4)
            r2.grid(column=1, row=5)
            s1.grid_forget()
        else:
            sorry()
    elif question == 1 and answerSpin.get() != "":
        if answerRadio.get() == "Ja":
            question = 2
            questionVar.set("Bent u in bezit van een geldig vrachtwagenrijbewijs?")
        else:
            sorry()
    elif question == 2 and answerSpin.get() != "":
        if answerRadio.get() == "Ja":
            question = 3
            questionVar.set("Bent u in bezit van een hoge hoed?")
        else:
            sorry()
    elif question == 3 and answerSpin.get() != "":
        if answerRadio.get() == "Ja":
            question = 4
            questionVar.set("Bent u man of vrouw? M/V")
            config("M", "V")
        else:
            sorry()
    elif question == 4 and answerSpin.get() !="":
        if answerRadio.get() == "M":
            question = 50
            questionVar.set("Heeft u een snor?")
            config("Y", "N")
        else:
            question = 51
            questionVar.set("Heeft u rood krulhaar?")
            config("Y", "N")

    ############################################# MAN #############################################
    elif question == 50:
        if answerRadio.get() == "Y":
            question = 60
            questionVar.set("Hoe breed bent u met snor?")
            r1.grid_forget()
            r2.grid_forget()
            s1.grid(column=1, row=1, ipadx=20, ipady=20, sticky="EW")
        else:
            sorry()
    elif question == 60:
        if answerSpin.get() >= 10:
            question = 70
            questionVar.set("Hoe lang bent u in cm?")
        else:
            sorry()
    elif question == 70:
        if answerSpin.get() >=150:
            question = 80
            questionVar.set("Hoeveel weegt u in kg?")
        else:
            sorry()
    elif question == 80:
        if answerSpin.get() >= 90:
            question = 90
            questionVar.set("Welke schoenmaat heeft u?")
        else:
            sorry()
    elif question == 90:
        if answerSpin.get() >= 40:
            question = 100
            questionVar.set("Hoeveel huisdieren heeft u?")
        else:
            sorry()
    elif question == 100:
        if answerSpin.get() >= 4:
            question = 110
            questionVar.set("Welke kleur vind u mooier: blauw of oranje?")
            s1.grid_forget()
            r1.grid(column=1, row=4)
            r2.grid(column=1, row=5)
            config("Blauw", "Oranje")
        else:
            sorry()
    elif question == 110:
        if answerRadio.get() == "Blauw":
            question = 120
            questionVar.set("Hoever kunt u springen in cm?")
            r1.grid_forget()
            r2.grid_forget()
            s1.grid(column=1, row=1, ipadx=20, ipady=20, sticky="EW")
        else:
            sorry()
    elif question == 120:
        if answerSpin.get() >= 100:
            passed = True
        else:
            sorry()
    ############################################# VROUW  #############################################
    elif question == 51:
        if answerRadio.get() == "Y":
            question = 61
            questionVar.set("Hoelang is uw krulhaar in cm?")
            r1.grid_forget()
            r2.grid_forget()
            s1.grid(column=1, row=1, ipadx=20, ipady=20, sticky="EW")
        else:
            sorry()
    elif question == 61:
        if answerSpin.get() >= 20:
            question = 70
            questionVar.set("Hoelang bent u in cm?")
        else:
            sorry()

    if passed == True:
        window.destroy()
        passedWindow = tk.Tk()
        passedLabel = tkinter.Label(passedWindow, text="Gefeliciteerd! U hebt het certificaat: Overleven met gevaarlijk personeel!").pack()
        exitButton = ttk.Button(passedWindow, text="Exit", command=destroy).pack()
    answerRadio.set("")



questionVar = tk.StringVar(value="Hoelang heeft u praktijkervaring met dieren-dressuur?")
questionLabel = tk.Label(window, textvariable=questionVar).grid(column=1, row=0, padx=20, pady=10)
answerRadio = tkinter.StringVar()
answerSpin = tkinter.IntVar()
s1 = ttk.Spinbox(window, from_=0, to="inf" ,textvariable=answerSpin, state='normal')
s1.grid(column=1, row=1, ipadx=20, ipady=20, sticky="EW")
r1 = ttk.Radiobutton(window, text="Ja", variable=answerRadio, value="Ja")
r1.grid(column=1, row=4)
r2 = ttk.Radiobutton(window, text="Nee", variable=answerRadio, value="Nee")
r2.grid(column=1, row=5)
r1.grid_forget()
r2.grid_forget()
checkButton = ttk.Button(window, text="Confirm", command=checkAnswer).grid(column=1, row=6, ipadx=20, ipady=10, sticky="EW")


window.mainloop()

###################################################################################### OUDE CODE #################################################################################################
# antwoord = int(input("Hoelang heeft u praktijkervaring met dieren-dressuur?"))
# geslaagd = False
# if antwoord >= 4:
#     antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N").upper()
#     if antwoord =="Y":
#         antwoord = input("Bent u in bezit van een geldig vrachtwagenrijbewijs? Y/N").upper()
#         if antwoord =="Y":
#             antwoord = input("Bent u in bezit van een hoge hoed? Y/N").upper()
#             if antwoord =="Y":
#                 antwoord = input("Bent u man of vrouw? M/V").upper()
#                 if antwoord =="M":
#                     antwoord = input("Heeft u een snor? Y/N").upper()
#                     if antwoord =="Y":
#                         antwoord = int(input("Hoe breed bent u met snor?"))
#                         if antwoord >= 10:
#                             antwoord = int(input("Hoelang bent u in cm?"))
#                             if antwoord >= 150:
#                                 antwoord = int(input("Hoeveel weegt u in kg?"))
#                                 if antwoord >= 90:
#                                     antwoord = float(input("Welke schoenmaat heeft u?"))
#                                     if antwoord >= 40:
#                                         antwoord = int(input("Hoeveel huisdieren heeft u?"))
#                                         if antwoord <= 4:
#                                             antwoord = (input("Welke kleur vind u mooier: blauw of oranje?"))
#                                             if antwoord == "blauw":
#                                                 antwoord = int(input("Hoever kunt u springen in cm?"))
#                                                 if antwoord >= 100:
#                                                     geslaagd = True
#                 if antwoord =="V":
#                     antwoord = input("heeft u rood krulhaar? Y/N").upper()
#                     if antwoord =="Y":
#                         antwoord = int(input("Hoelang is uw rode krulhaar in cm?"))
#                         if antwoord >= 20:
#                             antwoord = int(input("Hoelang bent u in cm?"))
#                             if antwoord >= 150:
#                                 antwoord = int(input("Hoeveel weegt u in kg?"))
#                                 if antwoord >= 90:
#                                     antwoord = float(input("Welke schoenmaat heeft u?"))
#                                     if antwoord >= 40:
#                                         antwoord = int(input("Hoeveel huisdieren heeft u?"))
#                                         if antwoord <= 4:
#                                             antwoord = (input("Welke kleur vind u mooier: blauw of oranje?"))
#                                             if antwoord == "blauw":
#                                                 antwoord = int(input("Hoever kunt u springen in cm?"))
#                                                 if antwoord >= 100:
#                                                     geslaagd = True
# if geslaagd == True:
#     print("Gefeliciteerd! U hebt het certificaat: Overleven met gevaarlijk personeel!")
# else:
#     print("Sorry, maar u bent niet geschikt voor het beroep ruimtevuilnisman")