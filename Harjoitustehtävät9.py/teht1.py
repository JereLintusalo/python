import random

def luo_tiedosto():
    vastaukset = [
        "Kyllä, tietysti!",
        "Epäilemättä, kyllä.",
        "Voit luottaa siihen.",
        "Varmasti!",
        "Kysy myöhemmin.",
        "En ole varma.",
        "En voi kertoa sinulle juuri nyt.",
        "Kerron sinulle päiväuneni jälkeen.",
        "Ei missään nimessä!",
        "En usko.",
        "Epäilemättä, ei.",
        "Vastaus on selvästi EI."
    ]
    with open("taikapallon_vastaukset.txt", "w", encoding="utf-8") as tiedosto:
        for vastaus in vastaukset:
            tiedosto.write(vastaus + "\n")

def lue_vastaukset():
    try:
        with open("taikapallon_vastaukset.txt", "r", encoding="utf-8") as tiedosto:
            return [rivi.strip() for rivi in tiedosto.readlines()]
    except IOError:
        print("Virhe: Tiedostoa ei löydy.")
        return []
    
def taikapallo():
    vastaukset = lue_vastaukset()
    if not vastaukset:
        return
    
    while True:
        kysymys = input("Kysy kysymys (tai kirjoita 'lopeta' lopettaaksesi): ")
        if kysymys.lower() == "lopeta":
            break
        print(random.choice(vastaukset))

luo_tiedosto()
taikapallo()