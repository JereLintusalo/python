def suurin_luku():
    luku1 = float(input("Anna eka luku: "))
    luku2 = float(input("Anna toka luku: "))
    luku3 = float(input("Anna kolmas luku: "))

    suurin = max(luku1, luku2, luku3)
    print(f"Suurin luku on: {suurin}")

def lukujen_tulo():
    luku1 = float(input("Anna eka luku: "))
    luku2 = float(input("Anna toka luku: "))

    tulo = luku1 * luku2
    print(f"Lukujen tulo on: {tulo}")

def ostosten_summa():
    ostokset = []
    while True:
        hinta = input("Anna ostosten hinta (tai 'lopeta' lopettaaksesi): ")
        if hinta.lower() == 'lopeta':
            break
        try:
            ostokset.append(float(hinta))
        except ValueError:
            print("Virheellinen syöte, anna luku.")
    
    summa = sum(ostokset)
    print(f"Ostosten summa on: {summa}")

def main():
    while True:
        print("\nValitse vaihtoehto:")
        print("1 = Luvuista suurin")
        print("2 = Lukujen tulo")
        print("3 = Ostosten summa")
        print("0 = Lopeta")

        valinta = input("Syötä valintasi: ")

        if valinta == "1":
            suurin_luku()
        elif valinta == "2":
            lukujen_tulo()
        elif valinta == "3":
            ostosten_summa()
        elif valinta == "0":
            print("Ohjelma lopetetaan")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")
        
if __name__ == "__main__":
    main()