import random

veljenpojat = ["Tupu", "Hupu", "Lupu"]
sisarentyttaret = ["Leenu", "Liinu", "Tiinu"]

random.shuffle(veljenpojat)
random.shuffle(sisarentyttaret)

parit = list(zip(veljenpojat, sisarentyttaret))

print("Peliparit:")
for pari in parit:
    print(f"{pari[0]} ja {pari[1]}")