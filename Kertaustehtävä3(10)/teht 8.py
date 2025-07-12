tiedoston_nimi = "teksti.txt"
maara = int(input("Kuinka monta nimeä haluat antaa?: "))

with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
    for i in range(maara):
        etunimi = input(f"Anna etunimi {i+1}: ").strip()
        sukunimi = input(f"Anna sukunimi {i+1}: ").strip()
        kk = input(f"Anna syntymäkuukausi {i+1}: ").strip()

        if not etunimi or not sukunimi:
            print("Etunimi tai sukunimi on NULL, ei tallenneta.")
            continue

        if not kk:
            print("Syntymäkuukausi puuttuu – tallennetaan silti ilman kuukautta.")

        tiedosto.write(etunimi + "\n")
        tiedosto.write(sukunimi + "\n")
        tiedosto.write((kk if kk else "Ei tiedossa") + "\n")

print("Tallennus valmis.")
