def sanojen_esiintyvyys(sanalista):
    esiintymiset = []
    for sana in sanalista:
        loytyi = False
        for pari in esiintymiset:
            if pari[0] == sana:
                pari[1] += 1
                loytyi = True
                break
        if not loytyi:
            esiintymiset.append([sana, 1])
    
    for sana, maara in esiintymiset:
        print(f"{sana}: {maara}")

sanalista =  ["omena", "banaani", "omena", "kirsikka", "klementiini",
              "omena", "banaani"]
sanojen_esiintyvyys(sanalista)