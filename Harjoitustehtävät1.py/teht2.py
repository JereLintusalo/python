#Harjoitus 2
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))

if luku1 > luku2:
    print(luku1, "on suurempi")
elif luku2 > luku1:
    print(luku2, "on suurempi")
elif luku1 == luku2:
    print("Luvut ovat yhtäsuuret")