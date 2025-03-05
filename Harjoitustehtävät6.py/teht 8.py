def jaa_merkkijono(jono, merkki):
    for i in range(len(jono) - 2):
        osajono = jono[i : i + 3]
        if osajono[0] == merkki:
            print(osajono)

jono = input("Anna merkkijono: ")
merkki = input("Anna merkki: ")
jaa_merkkijono(jono, merkki)