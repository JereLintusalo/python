#Harjoitus 3
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
valinta = input("Haluatko tulostaa (s)uuremman vai (p)ienemmän luvun? (s/p): ").strip().lower()

if valinta == "s":
    if luku1 > luku2:
        print("Suurempi luku on:", luku1)
    elif luku2 > luku1:
        print("Suurempi luku on:", luku2)
    else:
        print("Luvut ovat yhtä suuria:", luku1)

elif valinta == "p":
    if luku1 < luku2:
        print("Pienempi luku on:", luku1)
    elif luku2 < luku1:       
        print("Pienempi luku on:", luku2)
    else:
        print("Luvut ovat yhtä suuria:", luku1)
else:
    print("Virheellinen valinta!")