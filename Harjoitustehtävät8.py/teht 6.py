try:
    with open("numbers.txt", "r") as tiedosto:
        summa = 0
        lkm = 0
        for rivi in tiedosto:
            try:
                luku = int(rivi.strip())
                summa += luku
                lkm += 1
            except ValueError:
                print(f"Virheellinen luku: {rivi.strip()}")
        if lkm > 0:
            keskiarvo = summa / lkm
            print(f"Keskiarvo: {keskiarvo:.2f}")
        else:
            print("Ei lukuja tiedostossa.")
except FileNotFoundError:
    print("Tiedostoa 'numbers.txt' ei löytynyt.")