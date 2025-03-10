def matriisi(nimi, koko):
    print(f"\ntuloksena {koko}x{koko} matriisi seuraavasti\n")
    for i in range(koko):
        rivi = "".join(nimi[(i + j) % len(nimi)] for j in range(koko))
        print(rivi)
      
mj = input("Anna nimi ja nro (1-10): ")
try:
    nimi, numero = mj.rsplit(" ", 1)
    koko = int(numero)
    if 1 <= koko <= 10:
        matriisi(nimi, koko)
    else:
        print("Virhe: Numero tulee olla väliltä 1-10.")
except ValueError:
    print("Virheellinen syöte!") 