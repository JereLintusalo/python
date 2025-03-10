teksti = "Tapahtuma-aikaan kesällä 2015 nuori mies teki töitä belgialaiselle yritykselle Helsingissä sekä eräissä muissa maissa. Verohallinto lähti siitä, että hän asuu pääosin Suomessa ja määräsi hänet maksamaan Ferrarista täkäläisen autoveron, 105786 euroa."

sanat = teksti.split()

yhdysviiva_sanat = [sana for sana in sanat if "-" in sana]

print(f"Yhdysviivalliset sanat: {yhdysviiva_sanat}")
print("Yhdysviivallisten sanojen määrä", len(yhdysviiva_sanat))