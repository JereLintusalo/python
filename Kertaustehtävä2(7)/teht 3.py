teksti = "Varmaan tarvitsen vähän happea kun tässä on menty aika haipakkaa sanotaan viimeiset kuusi vuotta. Kisoissa olin monta vuotta putkeen, ja kesät olivat aika lyhyitä."

sanat = teksti.split()

pitkat_sanat = [sana for sana in sanat if len(sana) >= 7]

print(f"Pitkät sanat: {pitkat_sanat}")



