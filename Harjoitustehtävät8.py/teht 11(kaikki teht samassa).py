# Python-ohjelma: Tiedostotehtävät valikolla

def tiedoston_alku():
    nimi = input("Anna tiedoston nimi: ")
    try:
        with open(nimi, "r") as f:
            rivit = f.readlines()
            for rivi in rivit[:5]:
                print(rivi.strip())
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")
    
def rivinumerot():
    nimi = input("Anna tiedoston nimi: ")
    try:
        with open(nimi, "r") as f:
            for i, rivi in enumerate(f, 1):
                print(f"{i}: {rivi.strip()}")
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")

def korkein_pistemaara():
    try:
        with open("scores.txt", "r") as f:
            korkein = -1
            paras_nimi = ""
            lkm = 0
            for rivi in f:
                osat = rivi.strip().split()
                if len(osat) >= 2:
                    nimi = " ".join(osat[:-1])
                    try:
                        pisteet = int(osat[-1])
                        lkm += 1
                        if pisteet > korkein:
                            korkein = pisteet
                            paras_nimi = nimi
                    except ValueError:
                        continue
            if lkm > 0:
                print(f"Korkein pistemäärä: {paras_nimi} {korkein}")
                print(f"Tietueita: {lkm}")
            else:
                print(f"Ei tietueita tiedostossa.")
    except FileNotFoundError:
        print("scores.txt ei löytynyt.")

def numeroiden_summa():
    try:
        with open("numbers.txt", "r") as f:
            summa = 0
            for rivi in f:
                try:
                    summa += int(rivi.strip())
                except ValueError:
                    continue
            print(f"Summa: {summa}")
    except FileNotFoundError:
        print("numbers.txt ei löytynyt.")

def numeroiden_keskiarvo():
    try:
        with open("numbers.txt", "r") as f:
            summa = 0
            lkm = 0
            for rivi in f:
                try:
                    luku = int(rivi.strip())
                    summa += luku
                    lkm += 1
                except ValueError:
                    continue
            if lkm > 0:
                print(f"Keskiarvo: {summa / lkm:.2f}")
            else:
                print("Ei lukuja tiedostossa.")
    except IOError:
        print("Virhe tiedoston käsittelyssä.")

def kirjoita_sanoja():
    n = int(input("Kuinka monta sanaa haluat kirjoittaa? "))
    with open("sanat.txt", "w") as f:
        for i in range(n):
            sana = input(f"Anna sana {i+1}: ")
            f.write(sana + "\n")
    print("Sanat tallennettu.")

def lue_sanaluettelu():
    try:
        with open("sanat.txt", "r") as f:
            sanat = [r.strip() for r in f if r.strip()]
            if sanat:
                print(f"Sanojen lukumäärä: {len(sanat)}")
                print(f"Pisin sana: {max(sanat, key=len)}")
                keski = sum(len(s) for s in sanat) / len(sanat)
                print(f"Keskimääräinen pituus: {keski:.2f}")
            else:
                print("Tiedosto on tyhjä.")
    except FileNotFoundError:
        print("sanat.txt ei löytynyt.")

def golf_tallennus():
    n = int(input("Kuinka monta pelaajaa? "))
    with open("golf.txt", "w") as f:
        for i in range(n):
            nimi = input("Pelaajan nimi: ")
            pisteet = input("Pisteet: ")
            f.write(f"{nimi},{pisteet}\n")
    print("Pelaajat tallennettu.")

def golf_luku():
    try:
        with open("golf.txt", "r") as f:
            for rivi in f:
                osat = rivi.strip().split(",")
                if len(osat) == 2:
                    print(f"{osat[0]}: {osat[1]}")
    except FileNotFoundError:
        print("golf.txt ei löytynyt.")

def valikko():
    while True:
        print("\n1. Tiedoston alku")
        print("2. Rivinumerot")
        print("3. Korkein pistemäärä")
        print("4. Numeroiden summa")
        print("5. Numeroiden keskiarvo")
        print("6. Kirjoita sanaluettelo")
        print("7. Lue sanaluettelo")
        print("8. Golf: kirjoita tiedostoon")
        print("9. Golf: lue tiedostoa")
        print("0. Lopeta")
        valinta = input("Valitse toiminto: ")

        if valinta == "1":
            tiedoston_alku()
        elif valinta == "2":
            rivinumerot()
        elif valinta == "3":
            korkein_pistemaara()
        elif valinta == "4":
            numeroiden_summa()
        elif valinta == "5":
            numeroiden_keskiarvo()
        elif valinta == "6":
            kirjoita_sanoja()
        elif valinta == "7":
            lue_sanaluettelu()
        elif valinta == "8":
            golf_tallennus()
        elif valinta == "9":
            golf_luku()
        elif valinta == "0":
            print("Lopetetaan...")
            break
        else:
            print("Virheellinen valinta.")

# Ohjelman käynnistys
valikko()