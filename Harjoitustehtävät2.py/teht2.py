summa1 = 0
edellinen_luku = None

while True:
    luku1 = int(input("Syötä luku: "))
    if luku1 == edellinen_luku:
        break
    summa1 += luku1
    edellinen_luku = luku1

print(f"Syötettyjen lukujen summa: {summa1}")

    

