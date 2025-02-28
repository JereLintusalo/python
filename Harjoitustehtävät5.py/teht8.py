luvut = 20

luku = [0] * luvut

print("Lukusi!")

for index in range(luvut):
    print("Numero #", index + 1, ": ", sep = " ", end=" ")
    luku[index] = int(input())

    summa = sum(luku)
    keskiarvo = summa / len(luku) if luku else 0
    pienin_nro = min(luku) 
    suurin_nro = max(luku)

print(f"Listan numeroiden summa on: {summa}")
print(f"Listan numeroiden keskiarvo on: {keskiarvo:.2f}")
print(f"Listan pienin nro on: {pienin_nro}")
print(f"Listan suurin nro on: {suurin_nro}")