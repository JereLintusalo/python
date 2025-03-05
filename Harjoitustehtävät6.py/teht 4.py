mj = "Esimerkkinä tämä jono"

def poista_vokaalit(merkkijono):
    vokaalit = "aeiouyäöAEIOUYÄÖ"
    return "".join([merkki for merkki in merkkijono if merkki not in vokaalit])

def main():
    merkkijono = "Esimerkkinä tämä jono"
    print(poista_vokaalit(merkkijono))

main()