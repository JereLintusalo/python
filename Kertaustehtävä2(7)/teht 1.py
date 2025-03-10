def matriisi(nimi):
    koko == 3
    print(f"\ntuloksena {koko}x{koko} matriisi seuraavasti\n")
    for i in range(koko):
        rivi = "".join(nimi[(i + j) % len(nimi)] for j in range(koko))
        print(rivi)
      
mj = input("Anna nimi ja nro: ")
try:
    nimi, numero = mj.rsplit(" ", 1)
    koko = int(numero)
    if int(numero) == 3:
        matriisi(nimi)
    else:
        print("Virhe: Numero tulee olla 3.")
except ValueError:
    print("Virheellinen syöte!") 

