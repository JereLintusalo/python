import json

def lataa_tiedot(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    except (IOError, json.JSONDecodeError):
        return {}

def tallenna_tiedot(tiedostonimi, syntymapaivat):
    with open(tiedostonimi, "w", encoding="utf-8") as tiedosto:
        json.dump(syntymapaivat, tiedosto, ensure_ascii=False, indent=4)

def nayta_menu():
    print("\nValitse toiminto:")
    print("1 - Etsi syntymäpäivä")
    print("2 - Lisää uusi syntymäpäivä")
    print("3 - Muuta syntymäpäivää")
    print("4 - Poista syntymäpäivä")
    print("5 - Lopeta ohjelma")

def katsele(syntymapaivat):
    nimi = input("Anna henkilön nimi: ")
    print(syntymapaivat.get(nimi, "Syntymäpäivää ei löytynyt."))

def lisaa(syntymapaivat, tiedostonimi):
    nimi = input("Anna henkilön nimi: ")
    paiva = input("Anna syntymäpäivä (pp.kk.vvvv): ")
    syntymapaivat[nimi] = paiva
    tallenna_tiedot(tiedostonimi, syntymapaivat)
    print("Syntymäpäivä lisätty.")

def paivita(syntymapaivat, tiedostonimi):
    nimi = input("Anna henkilön nimi: ")
    if nimi in syntymapaivat:
        paiva = input("Anna uusi syntymäpäivä (pp.kk.vvvv): ")
        syntymapaivat[nimi] = paiva
        tallenna_tiedot(tiedostonimi, syntymapaivat)
        print("Syntymäpäivä päivitetty.")
    else:
        print("Nimeä ei löytynyt.")

def poista(syntymapaivat, tiedostonimi):
    nimi = input("Anna poistettavan henkilön nimi: ")
    if nimi in syntymapaivat:
        del syntymapaivat[nimi]
        tallenna_tiedot(tiedostonimi, syntymapaivat)
        print("Syntymäpäivä poistettu.")
    else:
        print("Nimeä ei löytynyt.")

def main():
    tiedostonimi = "syntymapaivat.json"
    syntymapaivat = lataa_tiedot(tiedostonimi)
    while True:
        nayta_menu()
        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            katsele(syntymapaivat)
        elif valinta == "2":
            lisaa(syntymapaivat, tiedostonimi)
        elif valinta == "3":
            paivita(syntymapaivat, tiedostonimi)
        elif valinta == "4":
            poista(syntymapaivat, tiedostonimi)
        elif valinta == "5":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

main()