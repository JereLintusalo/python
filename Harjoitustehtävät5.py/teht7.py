month = 12

sade = [0] * month

print("Sademäärät!")

for index in range(month):
    print("Kuukausi #", index + 1, ": ", sep = " ", end=" ")
    sade[index] = float(input())

    summa = sum(sade)
    keskiarvo = summa / len(sade) if sade else 0
    pienin_maara = min(sade) 
    suurin_maara = max(sade)

    # Selvitetään kk (indexi + 1, koska lista alkaa nollasta)
    pienin_kk = sade.index(pienin_maara) + 1
    suurin_kk = sade.index(suurin_maara) + 1

print(f"Kokonais kuukausien sademäärä: {summa}")
print(f"Keskimääräinen sademäärä on: {keskiarvo:.2f}")
print(f"Pienin kuukausi sademäärä oli: {pienin_maara} (Kuukausi oli {pienin_kk})")
print(f"Suurin kuukausi sademäärä oli: {suurin_maara} (Kuukausi oli {suurin_kk})")

    
