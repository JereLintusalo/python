import random
print("Arvaa väri! (Sininen, Punainen, Vihreä, Musta tai Valkoinen)")

def arvaa_vari():
    vari = random.choice(["Sininen", "Punainen", "Vihreä", "Musta", "Valkoinen"])
    for yritys in range(1, 4):
        arvaus = input(f"Arvaus {yritys}/3: Minkä värin kone valitsi? ").capitalize()
        if arvaus == vari:
            return 4 - yritys
    return 0

pisteet = 0
for kierros in range(1, 5):
    print(f"\nKierros {kierros}/4")
    pisteet += arvaa_vari()

print(f"\nPeli ohi! Pisteesi oli: {pisteet}")