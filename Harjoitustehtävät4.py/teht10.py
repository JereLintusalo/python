import time

def korjaa_aika(minuutit, sekunnit):
    if sekunnit < 0:
        minuutit -= 1
        sekunnit += 60

    minuutit = max(0, minuutit)  #estää negatiiviset minuutit
    sekunnit = max(0, sekunnit)  # estää negatiiviset sekunnit
    minuutit += sekunnit // 60   #muuntaa ylimenevät sekunnit minuuteiksi
    sekunnit = sekunnit % 60     #jätää vain alle 60 sekuntia

    if minuutit > 5 or (minuutit == 5 and sekunnit > 0):  #Estää yli 5min ajan
        return False, False
    return minuutit, sekunnit    #palautetaan korjatut minuutit ja sekunnit

def get_minuutit(minuutit):
    return minuutit

def get_sekunnit(sekunnit):
    return sekunnit

def tulosta(minuutit, sekunnit):
    print(f"{minuutit}:{sekunnit:02}") #varmistaa että tulostaa aina kahdella nro

def lisaa_minuutti(minuutit, sekunnit):
    return korjaa_aika(minuutit + 1, sekunnit) # lisää minuutin ja tarkistaa rajoitukset

def vahenna_minuutti(minuutit, sekunnit):
    return korjaa_aika(minuutit - 1, sekunnit)

def lisaa_sekunti(minuutit, sekunnit):
    return korjaa_aika(minuutit, sekunnit + 1)  #lisää sekunnin ja korjaa ajan (jos tarve)

def vahenna_sekunti(minuutit, sekunnit):
    return korjaa_aika(minuutit, sekunnit - 1)  #vähentää sekunnin ja tarkistaa ajan

def main():
    while True:
        try:
            minuutit = int(input("Anna minuutit: "))  # Pyytää käyttäjältä minuutit
            sekunnit = int(input("Anna sekunnit: "))  # Pyytää käyttäjältä sekunnit
            
            minuutit, sekunnit = korjaa_aika(minuutit, sekunnit)  # Korjaa syötetyn ajan
            if minuutit is False:
                print("Maksimiaika on 5 minuuttia. Yritä uudelleen!")
                continue

            tulosta(minuutit, sekunnit)  # Tulostaa syötetyn ajan
        
            print("Ajastin käy...")
            while minuutit > 0 or sekunnit > 0:
                time.sleep(1)  # Odottaa 1 sekunnin
                minuutit, sekunnit = vahenna_sekunti(minuutit, sekunnit)
                tulosta(minuutit, sekunnit)
            
            print("Aika kului loppuun!")    
        except ValueError:
            print("Yritä uudelleen!")  # Jos käyttäjä syöttää muuta kuin numeroita, ohjelma pyytää syöttämään uudelleen

        print("\nKiitos!")  # Lopuksi kiitosviesti

main() 