def lue_tiedosto():
    try:
        tiedosntonimi = input("Anna tiedoston nimi: ")
        with open(tiedosntonimi, "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()
            while True:
                try:
                    rivinumero = int(input("Anna rivinumero, jonka haluat nähdä (0 lopettaa): "))
                    if rivinumero == 0:
                        break
                    print(rivit[rivinumero - 1].strip())
                except ValueError:
                    print("Virhe: Anna kelvollinen numero.")
                except IndexError:
                    print("Virhe: Rivinumero on liian suuri tai pieni.")

    except IOError:
        print("Virhe: Tiedostoa ei löydy tai sitä ei voi avata.")

lue_tiedosto()