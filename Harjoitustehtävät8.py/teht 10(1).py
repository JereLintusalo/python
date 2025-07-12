tiedoston_nimi = "golf.txt"
pelaajia = int(input("Kuinka monta pelaajaa haluat syöttää? "))

with open(tiedoston_nimi, "w") as tiedosto:
    for i in range(pelaajia):
        nimi = input(f"Anna pelaajan {i+1} nimi: ")
        pisteet = input(f"Anna {nimi} pisteet: ")
        tiedosto.write(f"{nimi},{pisteet}\n")
        
print("Pelaajatiedot tallennettu tiedostoon.")