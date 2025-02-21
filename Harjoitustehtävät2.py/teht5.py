alaraja = int(input("Anna alarajaluku: "))
ylaraja = int(input("Anna ylärajaluku: "))

while True:
    luku = int(input(f"Anna luku välillä [{alaraja}-{ylaraja}]: "))
    if alaraja <= luku <= ylaraja:
        break
    print("Luku ei ole lukualueen sisällä, yritä uudelleen.")

keskikohta = (alaraja + ylaraja) / 2
if luku < keskikohta:
    print("Luku on lähempänä alarajaa. Anna kolme negatiivista lukua.")
    summa = 0
    for i in range(3):
        while True:
            neg_luku = int(input(f"Anna negatiivinen luku ({i+1}/3): "))
            if neg_luku < 0:
                summa += neg_luku
                break
            print("Luvun on oltava negatiivinen")
    print(f"Negatiivisten lukujen summa on {summa}")
else:
    print("Luku on lähempänä ylärajaa, ei tehdä mitään")