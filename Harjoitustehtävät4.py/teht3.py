def lue_luku():
    luku = int(input("Anna luku: (-99 lopetttaa): "))
    return luku

def laske_tulo():
    tulo = 1
    eka_syote = True

    while True:
        luku = lue_luku()
        if luku == -99:
            break
        tulo *= luku
        eka_syote = False

    return tulo if not eka_syote else None

def tulosta(tulo):
    if tulo is None:
        print("Ei lskettavia lukuja.")
    else:
        print(f"Lukujen tulo on: {tulo}.")

def main():
    tulos = laske_tulo()
    tulosta(tulos)

main()