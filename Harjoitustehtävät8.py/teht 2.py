tiedoston_nimi = input("Anna tiedoston nimi: ")

try: 
    with open(tiedoston_nimi, "r") as tiedosto:
        rivit = tiedosto.readlines()
        for rivi in rivit[:5]:
            print(rivi.strip())
except FileNotFoundError:
    print("Tiedostoa ei löytynyt.")