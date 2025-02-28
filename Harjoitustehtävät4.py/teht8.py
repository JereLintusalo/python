def korjaa_aika(minuutit, sekunnit):
    minuutit = max(0, minuutit)
    sekunnit = max(0, sekunnit)
    minuutit += sekunnit // 60
    sekunnit = sekunnit % 60

    if minuutit >= 5:
        return 0, 0
    
    return minuutit, sekunnit

def get_minuutit(minuutit):
    return minuutit

def get_sekunnit(sekunnit): 
    return sekunnit

def tulosta(minuutit, sekunnit):
    print(f"{minuutit}:{sekunnit:02}") #varmistaa että tulostaa aina kahdella nro

def main():
    for kierros in range(1, 6):
        while True: 
            try:
                print(f"\nKierros {kierros}/5")
                minuutit = int(input("Anna minuutit: "))
                sekunnit = int(input("Anna sekunnit: "))

                minuutit, sekunnit = korjaa_aika(minuutit, sekunnit)
                tulosta(get_minuutit(minuutit), get_sekunnit(sekunnit))
                break
            except ValueError:
                print("Yritä uudelleen!")
    print("\nAika kysely päättyi 5 kierroksen jälkeen. Kiitos!")

main()


def get_min(min, sek):
    min = max(0, min)
    min += sek // 60
    return min if min < 5 else 0

def get_sek(sek):
    sek = max(0, sek)
    return sek % 60

def tulosta(min, sek):
    print(f"{min}:{sek}")

def main():
    for kierros in range(1, 6):
        while True:
            try:
                print(f"\nKierros {kierros}/5")
                min = int(input("Anna minuutit: "))
                sek = int(input("Anna sekunnit: "))

                min = get_min(min, sek)
                sek = get_sek(sek)

                if min == 0:
                    sek = 0
                
                tulosta(min, sek)
                break
            except ValueError:
                print("Yritä uudelleen!")
    print("\nAika kysely päättyi 5 kierroksen jälkeen. Kiitos!")

main()