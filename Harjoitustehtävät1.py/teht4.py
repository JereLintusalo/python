#Harjoitus 4
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

if luku1 <= luku2 and luku1 <= luku3:
    if luku2 <= luku3:
        print("Luvut pienimmästä suurimpaan: ", luku1, luku2, luku3)
    else:
        print("Luvut pienimmästä suurimpaan: ", luku1, luku3, luku2)
elif luku2 <= luku1 and luku2 <= luku3:
    if luku1 <= luku3:
        print("Luvut pienimmästä suurimpaan: ", luku2, luku1, luku3)
    else:
        print("Luvut pienimmästä suurimpaan: ", luku2, luku3, luku1)
else:
    if luku1 <= luku2:
        print("Luvut pienimmästä suurimpaan: ", luku3, luku1, luku2)
    else:
        print("Luvut pienimmästä suurimpaan: ", luku3, luku2, luku1)