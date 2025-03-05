def laske_esiintymat(mj):
    merkit = []
    maarat = []

    for merkki in mj:
        if merkki.isalpha():
            if merkki in merkit:
                indeksi = merkit.index(merkki)
                maarat[indeksi] += 1
            else:
                merkit.append(merkki)
                maarat.append(1)

    return merkit, maarat

def main():
    merkkijono = input("Anna merkkijono: ")
    merkit, maarat = laske_esiintymat(merkkijono)
    for i in range(len(merkit)):
        print(f"{merkit[i]}: {maarat[i]}")

main()    