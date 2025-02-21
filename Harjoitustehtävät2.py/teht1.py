summa1 = 0
while True:
    
    luku1 = int(input("Anna luku (Jos syötät luvun -1, ohjelma tulostaa summan): "))

    if luku1 == -1:
        break
    summa1 += luku1

print(f"Lukujen summa {summa1}")

