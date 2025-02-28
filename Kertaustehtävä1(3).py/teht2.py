import random

vaihtoehdot = ["Kruuna", "Klaava", "Pystyasento", "Kaninkolo"]
todennakoisyydet = [0.4, 0.4, 0.05, 0.15]

for i in range(10):
    tulos = random.choices(vaihtoehdot, todennakoisyydet)[0]
    print(f"Heitto {i+1}: {tulos}")


#Tehty toisella tapaa (if)
for i in range(10):
    arpa = random.random()

    if arpa < 0.4:
        tulos = "Kruuna"
    elif arpa < 0.4:
        tulos = "Klaava"
    elif arpa < 0.85:
        tulos = "Pystyasento"
    else:
        tulos = "Kaninkolo"
    
    print(f"Heitto {i+1}: {tulos}")