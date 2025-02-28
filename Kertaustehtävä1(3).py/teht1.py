import random

vastaus = random.randint(-100, 100)
vastaus = -99

lukujen_maara = 0
lukujen_summa = 0
parilliset = 0
parittomat = 0

while True:
            luku = int(input("Anna jokin luku (-100-100): "))
            if luku == vastaus:
                print("Kiitti ja moi")
                break
            lukujen_maara += 1
            lukujen_summa += luku

            if luku % 2 == 0: 
                parilliset += 1
            else:
                parittomat += 1

if lukujen_maara > 0:
    keskiarvo = lukujen_summa / lukujen_maara
else:
    keskiarvo = 0

print(f"Lukujen määrä: {lukujen_maara}")
print(f"Lukujen summa: {lukujen_summa}")
print(f"Lukujen keskiarvo: {keskiarvo:.2f}")
print(f"Parillisia lukuja oli {parilliset}")
print(f"Parittomia lukuja oli {parittomat}")


        