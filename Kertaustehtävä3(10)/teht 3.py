tiedoston_nimi = "nimi1.txt"
maara = int(input("Kuinka monta nimeä haluat antaa?: "))

with open(tiedoston_nimi, "w") as tiedosto:
    for i in range(maara):
        kokonimi = input(f"Anna kokonimi {i+1}: ")
        kk = input(f"Anna syntymäkuukausi {i+1}: ")
        tiedosto.write(f"{kokonimi} {kk}")

print("Nimet tallennettu!")
print(kokonimi, kk)