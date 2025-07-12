import random

def main():
    print("Tervetuloa 10-kertotaulun testiin!")
    jatka = "kyllä"

    while jatka.lower() == "kyllä":
        luku = random.randint(1, 10)
        oikea_vastaus = luku * 10

        try:
            vastaus = int(input(f"Paljon on {luku} x 10? "))
            if vastaus == oikea_vastaus:
                print("Oikein!")
            else:
                print(f"Väärin. Oikea vastaus on {oikea_vastaus}.")
        except ValueError:
            print("Virheellinen syöte! Kirjoita vain numeroita.")

        jatka = input("Haluatko jatkaa? (kyllä/ei): ")

main()