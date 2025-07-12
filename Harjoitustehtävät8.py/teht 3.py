tiedoston_nimi = input("Anna tiedoston nimi: ")

try:
    with open(tiedoston_nimi, "r") as tiedosto:
        for numero, rivi in enumerate(tiedosto, start=1):
            print(f"{numero}: {rivi.strip()}")
except FileNotFoundError:
    print("Tiedostoa ei löytynyt.")