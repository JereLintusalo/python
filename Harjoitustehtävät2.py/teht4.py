print("Positiiviset neljällä jaolliset luvut alle 1000(For:lla):")

for luku in range(4, 1000, 4):
    print(luku, end=", ")

#Sama while:llä
print("\n")
print("Positiiviset neljällä jaolliset luvut alle 1000 (While:lla):")

luku = 4
while luku < 1000:
    print(luku, end=", ")
    luku += 4