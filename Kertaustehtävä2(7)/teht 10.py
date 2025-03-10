import random

def kysy_raja(teksti):
    while True:
        try:
            arvo = int(input(teksti))
            return arvo
        except ValueError:
            print("Virhe! Anna kelvollinen kokonaisluku.")


def laske_tulo(kertoja, kerrottava):
    return kertoja * kerrottava


def main():
    print("Kertolasku on muotoa kertoja * kerrottava.")

    kertoja_alaraja = kysy_raja("Anna kertojan alaraja: ")
    kertoja_ylaraja = kysy_raja("Anna kertojan yläraja: ")
    kerrottavan_alaraja = kysy_raja("Anna kerrottavan alaraja: ")
    kerrottavan_ylaraja = kysy_raja("Anna kerrottavan yläraja: ")

    kertoja = random.randint(kertoja_alaraja, kertoja_ylaraja)
    kerrottava = random.randint(kerrottavan_alaraja, kerrottavan_ylaraja)

    print(f"Nyt kertolasku voisi olla esim. {kertoja} * {kerrottava}")

    tulo = laske_tulo(kertoja, kerrottava)
    print(f"Tämän laskun tulos on: {tulo}")


main()