import time
import random
import tkinter as tk

def generate_codes():
    t = option.get().lower()
    n = int(entry.get())
    result = ""

    if t == "minecraft":
        for x in range(n):
            result += g(4) + "-" + g(4) + "-" + g(4) + "\n"
    elif t == "paypal":
        for x in range(n):
            result += g(4) + "-" + g(4) + "-" + g(4) + "\n"
    elif t == "playstation":
        for x in range(n):
            result += g(4) + "-" + g(4) + "-" + g(4) + "\n"
    elif t == "amazon":
        for x in range(n):
            result += g(4) + "-" + g(6) + "-" + g(4) + "\n"
    elif t == "netflix":
        for x in range(n):
            result += g(4) + "-" + g(6) + "-" + g(4) + "\n"
    elif t == "steam":
        for x in range(n):
            result += g(4) + "-" + g(6) + "-" + g(5) + "\n"
    elif t == "fortnite":
        for x in range(n):
            result += g(5) + "-" + g(4) + "-" + g(4) + "\n"
    elif t == "robolox":
        for x in range(n):
            result += g(3) + "-" + g(3) + "-" + g(4) + "\n"
    elif t == "itunes":
        for x in range(n):
            result += g(16) + "\n"
    elif t == "ebay":
        for x in range(n):
            result += g(10) + "\n"
    elif t == "imvu":
        for x in range(n):
            result += g(10) + "\n"
    elif t == "webkinz":
        for x in range(n):
            result += g(8) + "\n"
    elif t == "pokemontgc":
        for x in range(n):
            result += g(3) + "-" + g(4) + "-" + g(3) + "-" + g(3) + "\n"
    elif t == "playstore":
        for x in range(n):
            result += g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "\n"
    elif t == "xbox":
        for x in range(n):
            result += g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "\n"

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result

window = tk.Tk()
window.title("MADE BY black__hat_.")

label_title = tk.Label(window, text="Made By black__hat_.")
label_title.pack()

label_card = tk.Label(window, text="Quelle carte cadaux voulez-vous générer ?")
label_card.pack()

option = tk.StringVar(window)
option.set("Minecraft")
dropdown_card = tk.OptionMenu(window, option, "Amazon", "Roblox", "Webkinz", "Fortnite", "IMVU", "Ebay",
                             "Netflix", "iTunes", "Paypal", "Visa", "PokemonTGC", "Playstation", "Steam",
                             "Xbox", "PlayStore", "Minecraft")
dropdown_card.pack()

label_quantity = tk.Label(window, text="Combien de codes voulez-vous générer ?")
label_quantity.pack()

entry = tk.Entry(window)
entry.pack()

button_generate = tk.Button(window, text="Générer", command=generate_codes)
button_generate.pack()

label_output = tk.Label(window, text="Codes générés :")
label_output.pack()

text_output = tk.Text(window, height=10, width=40)
text_output.pack()

window.mainloop()
