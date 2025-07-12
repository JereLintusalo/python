import json

def lataa_tiedot(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    except (IOError, json.JSONDecodeError):
        return {}

def tallenna_tiedot(tiedostonimi, data):
    with open(tiedostonimi, "w", encoding="utf-8") as tiedosto:
        json.dump(data, tiedosto, ensure_ascii=False, indent=4)

def nayta_menu():
    print("\nValitse toiminto:")
    print("1 - Etsi syntymäpäivä")
    print("2 - Lisää uusi ystävä")
    print("3 - Muuta syntymäpäivää")
    print("4 - Poista ystävä")
    print("5 - Näytä harrastuksen mukaan")
    print("6 - Lopeta ohjelma")

def katsele(data):
    nimi = input("Anna henkilön nimi: ")
    if nimi in data:
        print(f"Syntymäpäivä: {data[nimi]['syntymapaiva']}, Harrastukset: {', '.join(data[nimi]['harrastukset'])}")
    else:
        print("Tietoja ei löytynyt.")

def lisaa(data, tiedostonimi):
    nimi = input("Anna henkilön nimi: ")
    paiva = input("Anna syntymäpäivä (pp.kk.vvvv): ")
    harrastukset = input("Anna harrastukset pilkulla erotettuna: ").split(",")
    data[nimi] = {"syntymapaiva": paiva, "harrastukset": [h.strip() for h in harrastukset]}
    tallenna_tiedot(tiedostonimi, data)
    print("Tieto lisätty.")

def paivita(data, tiedostonimi):
    nimi = input("Anna henkilön nimi: ")
    if nimi in data:
        paiva = input("Anna uusi syntymäpäivä (pp.kk.vvvv): ")
        data[nimi]["syntymapaiva"] = paiva
        tallenna_tiedot(tiedostonimi, data)
        print("Syntymäpäivä päivitetty.")
    else:
        print("Nimeä ei löytynyt.")

def poista(data, tiedostonimi):
    nimi = input("Anna poistettavan henkilön nimi: ")
    if nimi in data:
        del data[nimi]
        tallenna_tiedot(tiedostonimi, data)
        print("Tieto poistettu.")
    else:
        print("Nimeä ei löytynyt.")

def nayta_harrastuksen_mukaan(data):
    harrastus = input("Anna harrastus: ")
    loydetyt = [nimi for nimi, tiedot in data.items() if harrastus in tiedot["harrastukset"]]
    if loydetyt:
        print("Henkilöt, jotka harrastavat tätä:", ", ".join(loydetyt))
    else:
        print("Ei löytynyt ketään, jolla olisi tämä harrastus.")

def main():
    tiedostonimi = "ystavat.json"
    data = lataa_tiedot(tiedostonimi)
    while True:
        nayta_menu()
        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            katsele(data)
        elif valinta == "2":
            lisaa(data, tiedostonimi)
        elif valinta == "3":
            paivita(data, tiedostonimi)
        elif valinta == "4":
            poista(data, tiedostonimi)
        elif valinta == "5":
            nayta_harrastuksen_mukaan(data)
        elif valinta == "6":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

main()