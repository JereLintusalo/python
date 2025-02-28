def laske_summa(eka, toka):
    return eka + toka

def laske_miinus(eka, toka):
    return eka - toka

def laske_tulo(eka, toka):
    return eka * toka
    
def laske_jako(eka, toka):
    if toka == 0:
        return "Nollalla ei voi jakaa!"
    return eka / toka

def main():
    luku1 = float(input("Anna eka luku: "))
    luku2 = float(input("Anna toinen luku: "))

    print(f"{luku1} + {luku2} = {laske_summa(luku1, luku2)}")
    print(f"{luku1} - {luku2} = {laske_miinus(luku1, luku2)}")
    print(f"{luku1} * {luku2} = {laske_tulo(luku1, luku2)}")
    print(f"{luku1} / {luku2} = {laske_jako(luku1, luku2)}")

main()