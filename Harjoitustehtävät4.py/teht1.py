def lue_luku():
    return int(input("Anna luku: "))

def laske_summa(eka, toka):
    return eka + toka

def on_parillinen(summa):
    return summa % 2 == 0

def main():

    luku1 = lue_luku()
    luku2 = lue_luku()
    summa = laske_summa(luku1, luku2)

    if on_parillinen(summa):
        print(f"Lukujen {luku1} ja {luku2} summa {summa} on parillinen.")
    else:
        print(f"Lukujen {luku1} ja {luku2} summa {summa} on pariton.")

main()