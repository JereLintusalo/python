tiedoston_nimi = "nimi.txt"
maara = int(input("Kuinka monta nimeä haluat antaa?: "))

with open(tiedoston_nimi, "w") as tiedosto:
    for i in range(maara):
        etunimi = input(f"Anna etunimi {i+1}: ")
        sukunimi = input(f"Anna sukunimi {i+1}: ")
        kk = input(f"Anna syntymäkuukausi {i+1}: ")
        tiedosto.write(f"{etunimi} {sukunimi} {kk}")

print("Nimet tallennettu!")
print(etunimi, sukunimi, kk)
