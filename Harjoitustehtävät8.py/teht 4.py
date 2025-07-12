try:
    with open("scores.txt", "r") as tiedosto:
        korkein_piste = -1
        paras_nimi = ""
        tietueita = 0

        for rivi in tiedosto:
            osat = rivi.strip().split()
            if len(osat) >= 2:
                nimi = " ".join(osat[:-1])
                try:
                    pisteet = int(osat[-1])
                    tietueita += 1
                    if pisteet > korkein_piste:
                        korkein_piste = pisteet
                        paras_nimi = nimi
                except ValueError:
                    print(f"Virheellinen pistemäärä rivillä: {rivi.strip()}")

        if tietueita > 0:
            print(f"Korkein pistemäärä: {paras_nimi} {korkein_piste}")
            print(f"Tietuiden lukumäärä: {tietueita}")
        else:
            print("Ei tietueita käsiteltäväksi.")
except FileNotFoundError:
    print("Tiedostoa 'scores.txt' ei löytynyt.")