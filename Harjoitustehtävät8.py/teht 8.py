try:
    with open("sanat.txt", "r") as tiedosto:
        sanat = [rivi.strip() for rivi in tiedosto if rivi.strip()]
        if sanat:
            lkm = len(sanat)
            pisin = max(sanat, key=len)
            keskipituus = sum(len(s) for s in sanat) / lkm
            print(f"Sanojen lukumäärä: {lkm}")
            print(f"Pisin sana: {pisin}")
            print(f"Sanojen keskimääräinen pituus: {keskipituus:.2f}")
        else:
            print("Tiedosto on tyhjä.")
except FileNotFoundError:
    print("Tiedostoa 'sanat.txt' ei löytynyt.")