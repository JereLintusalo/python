# Tee ohjelma, joka arpoo satunnaisluvun väliltä 1-100.
#  Ohjelman käyttäjän pitää arvata luku. 
#Ohjelma antaa vihjeitä, onko arvattu luku liian suuri tai pieni. 

def main():
    import random

    vastaus = random.randint(1, 100)
    print(vastaus)
    
    while True:
        try:
            luku = int(input("Anna jokin luku (1-100): "))
            if luku == vastaus:
                print("Löysit oikean luvun!")
                break
            elif luku < vastaus:
                print("Luku on isompi")
            else:
                print("Luku on pienempi")

        except ValueError:
            print("Anna uusi nro!")

       

main()