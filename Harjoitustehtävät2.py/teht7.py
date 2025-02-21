def main():
    import random

    paras_tulos = None
    huonoin_tulos = None

    while True:
        print("\nValitse toiminto: ")
        print("1) Arvaa uusi luku: ")
        print("2) Lopeta")

        valinta = input("Valintasi: ")

        if valinta == "2":
            print("Kiitos pelaamisesta!")
            break
        elif valinta != "1":
            print("Pelataan uudestaan!")
            continue


        vastaus = random.randrange(1, 101)
        arvausten_maara = 0
        print(vastaus)
    
        while True:
            try:
                luku = int(input("Anna jokin luku (1-100): "))
                if luku < 1 or luku > 100:
                    print("Anna luku väliltä 1-100!")
                    continue 
                arvausten_maara += 1

                if luku == vastaus:
                    print("Löysit oikean luvun!")

                    if paras_tulos is None or arvausten_maara < paras_tulos:
                        paras_tulos = arvausten_maara
                    if huonoin_tulos is None or arvausten_maara > paras_tulos:
                        huonoin_tulos = arvausten_maara
                    break
                elif luku < vastaus:
                    print("Luku on isompi")
                else:
                    print("Luku on pienempi")

            except ValueError:
                print("Anna uusi nro!")
        
        print(f"\nPelitilastot: ")
        print(f"Parhain tulos: {paras_tulos} arvausta")
        print(f"Huonoin tulos: {huonoin_tulos} arvausta")

main()