try:
    with open("numbers.txt", "r") as tiedosto:
        summa = 0
        for rivi in tiedosto:
            try:
                luku = int(rivi.strip())
                summa += luku
            except ValueError:
                print(f"Virheellinen luku rivillä: {rivi.strip()}")
        print(f"Lukujen summa on: {summa}")
except FileNotFoundError:
    print("Tiedostoa 'numbers.txt' ei löytynyt.")