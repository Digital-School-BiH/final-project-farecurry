import tkinter as tk
import random

# šeširi
šešir1 = ["Real Madrid, Španija", "Manchester City, Engleska", "Bayern Munchen, Njemačka", "Barcelona, Španija",
          "Liverpool, Engleska", "PSG, Francuska", "Napoli, Italija", "Benfica, Portugal"]

šešir2 = ["Inter Milan, Italija", "Atletico Madrid, Španija", "BVB, Njemačka", "Arsenal, Engleska",
          "Leipzig, Njemačka", "Porto, Portugal", "Juventus, Italija", "Chelsea, Engleska"]

šešir3 = ["Ajax, Holandija", "Milan, Italija", "Roma, Italija", "Sevilla, Španija",
          "Sporting, Portugal", "Šahtar, Ukrajina", "Totenhem, Engleska", "Marsej, Francuska"]

šešir4 = ["Galata, Turska", "Fener, Turska", "Crvena Zvezda, Srbija", "Sarajevo, Bosna",
          "Celtic, Škotska", "Feyenord, Holandija", "Stuttgart, Njemačka", "Atalanta, Italija"]

šeširi = [šešir1, šešir2, šešir3, šešir4]

imena_grupa = ["Grupa A", "Grupa B", "Grupa C", "Grupa D", "Grupa E", "Grupa F", "Grupa G", "Grupa H"]
grupe = [[] for _ in range(8)]

# Funkcije
def u_grupi_je_drzava(grupa, drzava):
    for tim in grupa:
        _, drzava_tima = tim.split(", ")
        if drzava_tima == drzava:
            return True
    return False

def izvuci_sesir(sesir, grupe):
    random.shuffle(sesir)
    slobodne_grupe = list(range(8))  # grupe koje još trebaju tim iz ovog šešira
    for tim in sesir:
        ime, drzava = tim.split(", ")
        random.shuffle(slobodne_grupe)  # promiješamo grupe da bude nasumično

        postavljen = False
        for idx in slobodne_grupe:
            if not u_grupi_je_drzava(grupe[idx], drzava):
                nacrtaj_tim(idx, tim)   # prvo nacrtaj na ekranu
                grupe[idx].append(tim)  # onda dodaj tim u grupu
                slobodne_grupe.remove(idx)  # ta grupa više nije slobodna za ovaj šešir
                postavljen = True
                break

def pokreni_izvlacenje():
    global trenutni_sesir
    if trenutni_sesir < 4:
        izvuci_sesir(šeširi[trenutni_sesir], grupe)
        trenutni_sesir += 1
    else:
        dugme.config(state="disabled")
        label_status.config(text="Žrijeb završen!")

def nacrtaj_tim(grupa_idx, tim):
    x = 50 + grupa_idx * 150
    y = 130 + (len(grupe[grupa_idx]) - 1) * 50

    # pravougaonik
    canvas.create_rectangle(x, y, x+140, y+40, fill="white", outline="black")
    canvas.create_text(x+70, y+20, text=tim.split(",")[0], font=("Helvetica", 10, "bold"))

# UI
root = tk.Tk()
root.title("Liga Šampiona Žrijeb")
root.geometry("1300x700")

label_naslov = tk.Label(root, text="UEFA DRAW - LIGA ŠAMPIONA", font=("Helvetica", 20, "bold"))
label_naslov.pack(pady=10)

canvas = tk.Canvas(root, width=1300, height=600, bg="lightblue")
canvas.pack()

# Nacrta imena grupa
for i in range(8):
    x = 50 + i * 150
    canvas.create_text(x+70, 50, text=imena_grupa[i], font=("Helvetica", 14, "bold"))

# Dugme za izvlačenje
dugme = tk.Button(root, text="Izvuci šešir", font=("Helvetica", 14), command=pokreni_izvlacenje)
dugme.pack()

# Label za status
label_status = tk.Label(root, text="", font=("Helvetica", 14))
label_status.pack()

trenutni_sesir = 0

root.mainloop()






