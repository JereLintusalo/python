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

def lisaa(syntymapaivat):
    nimi = input("Anna henkilön nimi: ")
    paiva = input("Anna syntymäpäivä (pp.kk.vvvv): ")
    syntymapaivat[nimi] = paiva
    print("Syntymäpäivä lisätty.")

def paivita(syntymapaivat):
    nimi = input("Anna henkilön nimi: ")
    if nimi in syntymapaivat:
        paiva = input("Anna uusi syntymäpäivä (pp.kk.vvvv): ")
        syntymapaivat[nimi] = paiva
        print("Syntymäpäivä päivitetty.")
    else:
        print("Nimeä ei löytynyt.")

def poista(syntymapaivat):
    nimi = input("Anna poistettavan henkilön nimi: ")
    if nimi in syntymapaivat:
        del syntymapaivat[nimi]
        print("Syntymäpäivä poistettu.")
    else:
        print("Nimeä ei löytynyt.")

def main():
    syntymapaivat = {}
    while True:
        nayta_menu()
        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            katsele(syntymapaivat)
        elif valinta == "2":
            lisaa(syntymapaivat)
        elif valinta == "3":
            paivita(syntymapaivat)
        elif valinta == "4":
            poista(syntymapaivat)
        elif valinta == "5":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")
main()