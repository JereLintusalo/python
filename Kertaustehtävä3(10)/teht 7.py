tiedoston_nimi = "teksti.txt"

try:
    with open(tiedoston_nimi, "r") as tiedosto:
        sisalto = tiedosto.read()
        if not sisalto.strip():
            print("Tiedosto on tyhjä.")
        else:
            print("Tiedoston sisältö:")
            print(sisalto)
except FileNotFoundError:
    print("Tiedostoa ei löytynyt.")