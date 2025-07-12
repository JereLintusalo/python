def main():
    tiedoston_nimi = "uutinen.txt"
    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            teksti = tiedosto.read()
    except FileNotFoundError:
        print("Tiedostoa 'uutinen.txt' ei löytynyt.")
        return

    sanat = teksti.split()
    pituudet = [len(sana.strip(".,!?():;\"")) for sana in sanat if sana.strip(".,!?():;\"")]

    if not pituudet:
        print("Tiedosto ei sisällä sanoja.")
        return

    sanamaara = len(sanat)
    keskipituus = sum(pituudet) / len(pituudet)
    pisin_pituus = max(pituudet)
    lyhin_pituus = min(pituudet)

    pisimmat_sanat = [sana for sana in sanat if len(sana.strip(".,!?():;\"")) == pisin_pituus]
    lyhimmat_sanat = [sana for sana in sanat if len(sana.strip(".,!?():;\"")) == lyhin_pituus]

    print(f"Sanojen lukumäärä: {sanamaara}")
    print(f"Sanojen keskipituus: {keskipituus:.2f}")
    print(f"Pisin sana/sanat ({pisin_pituus} kirjainta): {set(pisimmat_sanat)}")
    print(f"Lyhin sana/sanat ({lyhin_pituus} kirjainta): {set(lyhimmat_sanat)}")

main()