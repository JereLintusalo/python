import random

def peli(p_valinta):
    kone_nro = random.randint(1, 3)

    if kone_nro == 1:
        kone_valinta = "Kivi"
    elif kone_nro == 2:
        kone_valinta = "Paperi"
    else:
        kone_valinta = "Sakset"

    if p_valinta == 1:
        p_valinta = "Kivi"
    elif p_valinta == 2:
        p_valinta = "Paperi"
    elif p_valinta == 3:
        p_valinta = "Sakset"
    else:
        print("Virheellinen valinta! Yritä uudelleen!")
        return True
    
    print(f"\nSinä valitsit: {p_valinta}")
    print(f"Kone valitsi: {kone_valinta}")
    
    if p_valinta == kone_valinta:
        print("Tasapeli! Yritä uudelleen!")
        return True
    
    if (p_valinta == "Kivi" and kone_valinta == "Sakset") or \
        (p_valinta == "Paperi" and kone_valinta == "Kivi") or \
        (p_valinta == "Sakset" and kone_valinta == "Paperi"):
        print("Pelaaja voitti!")
        return False
    
    else:
        print("Hävisit!")
        return False

def main():
    while True:
        print("\nMinkä esineen otat?:")
        print("1 = Kivi")
        print("2 = Paperi")
        print("3 = Sakset")

        valinta = input("Syötä valinta (1-3): ").capitalize()

        if valinta in ["1", "2", "3"]:
            if not peli(int(valinta)):
                break
        else:
            print("Virheellinen valinta.Yritä uudelleen.")
        
if __name__ == "__main__":
    main()