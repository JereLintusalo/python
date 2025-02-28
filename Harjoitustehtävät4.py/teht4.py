def suurin_pienin(eka, toka, kolmas, neljas):
    suurin = eka
    pienin = eka

    if toka > suurin:
        suurin = toka
    if kolmas > suurin:
        suurin = kolmas
    if neljas > suurin:
        suurin = neljas

    if toka < pienin:
        pienin = toka
    if kolmas < pienin:
        pienin = kolmas
    if neljas < pienin:
        pienin = neljas

    return suurin, pienin

def main():
    while True:
        try:

            luku1 = int(input("Anna eka luku: "))
            luku2 = int(input("Anna toka luku: "))
            luku3 = int(input("Anna kolmas luku: "))
            luku4 = int(input("Anna neljäs luku: "))

            suurin, pienin = suurin_pienin(luku1, luku2, luku3, luku4)
            print(f"Suurin luku: {suurin}")
            print(f"Pienin luku: {pienin}")

        except ValueError:
            print("Yritä uudelleen!")
        
main()