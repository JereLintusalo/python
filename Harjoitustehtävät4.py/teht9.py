def korjaa_aika(minuutit, sekunnit):
    minuutit = max(0, minuutit)
    sekunnit = max(0, sekunnit)
    minuutit += sekunnit // 60
    sekunnit = sekunnit % 60

    if minuutit > 5:
        return 0, 0
    return minuutit, sekunnit

def get_minuutit(minuutit):
    return minuutit

def get_sekunnit(sekunnit):
    return sekunnit

def tulosta(minuutit, sekunnit):
    print(f"{minuutit}:{sekunnit:02}")

def lisaa_minuutti(minuutit, sekunnit):
    return korjaa_aika(minuutit + 1, sekunnit)

def vahenna_minuutit(minuutit, sekunnit):
    return korjaa_aika(minuutit - 1, sekunnit)

def lisaa_sekunti(minuutit, sekunnit):
    return korjaa_aika(minuutit, sekunnit + 1)

def vahenna_sekunti(minuutit, sekunnit):
    return korjaa_aika(minuutit, sekunnit - 1)

def main():
    try:
        minuutit = int(input("Anna minuutit: "))
        sekunnit = int(input("Anna sekunnit: "))

        minuutit, sekunnit = korjaa_aika(minuutit, sekunnit)
        tulosta(minuutit, sekunnit)

        print("Lisättiin minuutti: ", end=" ")
        tulosta(*lisaa_minuutti(minuutit, sekunnit))

        print("Vähennettiiin minuutti: ", end=" ")
        tulosta(*vahenna_minuutit(minuutit, sekunnit))

        print("Lisättiin sekunti: ", end=" ")
        tulosta(*lisaa_sekunti(minuutit, sekunnit))

        print("Vähennettiiin sekunti: ", end=" ")
        tulosta(*vahenna_sekunti(minuutit, sekunnit))
    
    except ValueError:
        print("Yritä uudelleen!")
        
    print("\nKiitos!")

main()


