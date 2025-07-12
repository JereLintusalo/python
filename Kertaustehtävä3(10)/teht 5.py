import random

def lataa_maat_ja_paakaupungit(tiedosto):
    maa_paakaupunki = {}
    with open(tiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            osat = rivi.strip().split(";")
            if len(osat) == 2:
                maa, paakaupunki = osat
                maa_paakaupunki[maa.strip()] = paakaupunki.strip()
    return maa_paakaupunki

def paakaupunkipeli():
    data = lataa_maat_ja_paakaupungit("maat.txt")
    kysyttavat = list(data.items())
    random.shuffle(kysyttavat)

    oikein = 0
    i = 0

    while oikein < 5 and i < len(kysyttavat):
        maa, paakaupunki = kysyttavat[i]
        vastaus = input(f"Mikä on {maa} pääkaupunki? ").strip()
        if vastaus.lower() == paakaupunki.lower():
            print("Oikein!")
            oikein += 1
        else:
            print(f"Väärin! Oikea vastaus on {paakaupunki}")
        i += 1

    if oikein >= 5:
        bonus = input("Haluatko kolme bonuskysymystä? (kyllä/ei): ").strip().lower()
        if bonus == "kyllä":
            for maa, paakaupunki in random.sample(kysyttavat[i:], 3):
                vastaus = input(f"Mikä on {maa} pääkaupunki? ").strip()
                if vastaus.lower() == paakaupunki.lower():
                    print("Oikein!")
                else:
                    print(f"Väärin! Oikea vastaus on {paakaupunki}")