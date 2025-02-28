import random

pisteet_pelaaja1 = 0
pisteet_pelaaja2 = 0
tavoite = 50

while pisteet_pelaaja1 < tavoite and pisteet_pelaaja2 < tavoite:
    input("Pelaaja 1, paina Enter heittääksesi noppaa...")
    heitto1 = random.randint(1, 6)
    pisteet_pelaaja1 += heitto1
    print(f"Pelaaja 1 heitti: {heitto1}, yhteispisteet: {pisteet_pelaaja1}")
    
    input("Pelaaja 2, paina Enter heittääksesi noppaa...")
    heitto2 = random.randint(1, 6)
    pisteet_pelaaja2 += heitto2
    print(f"Pelaaja 2 heitti: {heitto2}, yhteispisteet: {pisteet_pelaaja2}")
    print("-----------------------------------")

if pisteet_pelaaja1 >= tavoite and pisteet_pelaaja2 >= tavoite:
    print("Tasapeli! Molemmat saavuttivat 50 pistettä yhtä aikaa.")
elif pisteet_pelaaja1 >= tavoite:
    print("Pelaaja 1 voitti!")
elif pisteet_pelaaja2 >= tavoite:
    print("Pelaaja 2 voitti!")