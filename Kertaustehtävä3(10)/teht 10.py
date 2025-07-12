pisteet = {}

def lisaa_pisteet(pelaaja, maara):
    if pelaaja in pisteet:
        pisteet[pelaaja] += maara
    else:
        pisteet[pelaaja] = maara

pelien_maara = int(input("Kuinka monta peliä pelattiin? "))

for i in range(pelien_maara):
    print(f"\nPeli {i+1}")
    p1 = input("Pelaaja 1: ").strip()
    p2 = input("Pelaaja 2: ").strip()
    tulos = input("Kuka voitti? (nimi tai 'tasapeli'): ").strip()

    if tulos.lower() == "tasapeli":
        lisaa_pisteet(p1, 1)
        lisaa_pisteet(p2, 1)
    elif tulos == p1:
        lisaa_pisteet(p1, 3)
        lisaa_pisteet(p2, 0)
    elif tulos == p2:
        lisaa_pisteet(p1, 0)
        lisaa_pisteet(p2, 3)
    else:
        print("Tuntematon tulos, ei pisteitä jaettu.")

print("\nLopulliset pisteet:")
for pelaaja, pist in pisteet.items():
    print(f"{pelaaja}: {pist} pistettä")

maksimi = max(pisteet.values())
voittajat = [pelaaja for pelaaja, pist in pisteet.items() if pist == maksimi]

print("\nEniten pisteitä kerännyt/keränneet:")
for v in voittajat:
    print(f"{v} ({maksimi} pistettä)")
