import tkinter
import tkinter as ttk
from tkinter import ttk
my_formatter = "{0:.2f}"

def receipt():
    formattedLarge = my_formatter.format(largeVar.get()*large)
    formattedMedium = my_formatter.format(mediumVar.get()*medium)
    formattedSmall = my_formatter.format(smallVar.get()*small)
    total = smallVar.get()*small + mediumVar.get()*medium + largeVar.get()*large
    formattedTotal = my_formatter.format(total)

    window.destroy()
    receiptWindow = tkinter.Tk()
    bonLabel = tkinter.Label(receiptWindow, text=f"RECEIPT:\nSmall pizza's: €{formattedSmall}\nMedium pizza's: €{formattedMedium}\nLarge pizza's: €{formattedLarge}\nTotal: €{formattedTotal}", font=('Helvatical bold',10)).pack()

small = 3.99
medium = 5.00
large = 6.00

window = tkinter.Tk()
window.title("Pizza's bestellen")

pricesLabel = tkinter.Label(window, text=f"Prices:\nSmall: {small}\nMedium: {medium}\nLarge: {large}\n").pack()
smallinfoLabel = tkinter.Label(window, text="How much small pizza's do you want?").pack()
smallVar = tkinter.IntVar()
amountSmall = ttk.Spinbox(window, from_=0, to=float("inf"), textvariable=smallVar).pack()

mediuminfoLabel = tkinter.Label(window, text="How much medium pizza's do you want?").pack()
mediumVar = tkinter.IntVar()
amountMedium = ttk.Spinbox(window, from_=0, to=float("inf"), textvariable=mediumVar).pack()

largeinfoLabel = tkinter.Label(window, text="How much large pizza's do you want?").pack()
largeVar = tkinter.IntVar()
amountLarge = ttk.Spinbox(window, from_=0, to=float("inf"), textvariable=largeVar).pack()


checkOutButton = tkinter.Button(window, text="Checkout", command=receipt).pack()
window.mainloop()

# small = 3.99
# medium = 5.00
# large = 6.00

# #klant krijgt de prijzen te zien.
# print("""Prijzen in euro's
# small = 3.99
# medium = 5
# large = 6""")

# def kassabon():
#     my_formatter = "{0:.2f}"
#     formatted_total = my_formatter.format(aantalSmall * small + aantalMedium * medium + aantalLarge * large)
#     print("--------------------------------------")
#     print("| Uw bestelling:")
#     print(f"| {aantalSmall} small: ","€", formatted_prijssmall)
#     print(f"| {aantalMedium} medium: €", formatted_prijsmedium)
#     print(f"| {aantalLarge} large: ","€",formatted_prijslarge)
#     print("|")
#     print("| Totaalprijs = €", formatted_total)
#     print("--------------------------------------")
# def pizza():
#     my_formatter = "{0:.2f}"
#     global aantalSmall, aantalMedium, aantalLarge, formatted_prijslarge, formatted_prijsmedium, formatted_prijssmall
#     try:
#         aantalSmall = float(input("Hoeveel small pizza's wil je? "))
#         prijssmall = aantalSmall * small
#         formatted_prijssmall = my_formatter.format(prijssmall)
#         print("Dit kost", formatted_prijssmall)

#         aantalMedium = float(input("Hoeveel medium pizza's wil je? "))
#         prijsmedium = aantalMedium * medium
#         formatted_prijsmedium = my_formatter.format(prijsmedium)
#         print("Dit kost", formatted_prijsmedium)

#         aantalLarge = float(input("Hoeveel large pizza's wil je? "))
#         prijslarge = aantalLarge * large
#         formatted_prijslarge = my_formatter.format(prijslarge)
#         print("Dit kost", formatted_prijslarge)

#         kassabon()

        
#     except ValueError:
#         print("Vul a.u.b. een getal in.")
#         print()
#         pizza()

# pizza()