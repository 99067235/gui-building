from tkinter import Radiobutton, Variable, messagebox, ttk
import tkinter as tk
import tkinter


window = tkinter.Tk()
question = 0
def checkAnswer(*args):
    global question
    if question == 0 and answer.get() != "":
        if answer.get() == "Ja":
            question = 1
            questionVar.set("Zitten er gaten in?")
        else:
            question = 2
            questionVar.set("Heeft de kaas blauwe schimmels?")
    elif question == 1 and answer.get() != "":
        if answer.get() == "Ja":
            question = 11
            questionVar.set("Is de kaas belachelijk duur?")
        else:
            question = 12
            questionVar.set("Is de kaas hard als steen?")
    elif question == 11 and answer.get() != "":
        if answer.get() == "Ja":
            messagebox.showinfo("Kaas", "Emmenthaler")
        else:
            messagebox.showinfo("Kaas", "Leerdammer")
    elif question == 12 and answer.get() != "":
        if answer.get() == "Ja":
            messagebox.showinfo("Kaas", "Pamnigiano Reggiano")
        else:
            messagebox.showinfo("Kaas", "Goudse kaas")
    elif question == 2 and answer.get() != "":
        if answer.get() == "Y":
            question = 21
            questionVar.set("Heeft de kaas een korst?")
        else:
            question = 22
            questionVar.set("Heeft de kaas een korst?")
    elif question == 21 and answer.get() != "":
        if answer.get() == "Y":
            messagebox.showinfo("Kaas", "Bleu de Rochbaron")
        else:
            messagebox.showinfo("Kaas", "Foumne d'Ambert")
    elif question == 22 and answer.get() != "":
        if answer.get() == "Y":
            messagebox.showinfo("Kaas", "Camembert")
        else:
            messagebox.showinfo("Kaas", "Mozzerella")



    answer.set("")
questionVar = tk.StringVar(value="Is de kaas geel?")
questionLabel = tk.Label(window, textvariable=questionVar).pack()
answer = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Ja", variable=answer, value="Ja")
r1.pack()
r2 = ttk.Radiobutton(window, text="Nee", variable=answer, value="Nee")
r2.pack()
answer.trace('w', checkAnswer)
window.mainloop()



# antwoord = input("is de kaas geel? Y/N").upper()
# if antwoord == "Y":
#     input("Zitten er gaten in?")
#     if antwoord == "Y":
#         input("Is de kaas belachelijk duur?")
#         if antwoord == "Y":
#             print("Emmenthaler")
#         if antwoord == "N":
#             print("Leerdammer")
#     if antwoord == "N":
#         input("Is de kaas hard als steen?")
#         if antwoord == "Y":
#             print("Pamnigiano Reggiano")
#         if antwoord == "N":
#             print("Goudse kaas")
# if antwoord == "N":
#     input("Heeft de kaas blauwe schimmels?")
#     if antwoord == "Y":
#         input("Heeft de kaas een korst?")
#         if antwoord == "Y":
#             print("Bleu de Rochbaron")
#         if antwoord == "N":
#             print("Foumne d'Ambert")
#     if antwoord == "N":
#         input("Heeft de kaas een korst?")
#         if antwoord == "Y":
#             print("Camembert")
#         if antwoord == "N":
#             print("Mozzerella")