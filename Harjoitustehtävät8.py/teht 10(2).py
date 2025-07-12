try:
    with open("golf.txt", "r") as tiedosto:
        print("Pelaajat ja pisteet:")
        for rivi in tiedosto:
            osat = rivi.strip().split(",")
            if len(osat) == 2:
                nimi, pisteet = osat
                print(f"{nimi}: {pisteet}")
except FileNotFoundError:
    print("Tiedostoa 'golf.txt' ei löytynyt.")