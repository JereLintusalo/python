def pisin_sana(jono):
    sanat = jono.split()
    pisin = max(sanat, key=len)
    return pisin

jono = input("Anna merkkijono: ")
print("Pisimmän sanan pituus on: ", pisin_sana(jono))