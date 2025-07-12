tiedosto_nimi = "sanat.txt"
maara = int(input("Kuinka monta sanaa haluat kirjoittaa tiedostoon? "))

with open(tiedosto_nimi, "w") as tiedosto:
    for i in range(maara):
        sana = input(f"Anna sana {i+1}: ")
        tiedosto.write(sana + "\n")
print("Sanat on tallennettu tiedostoon.")