#Harjoitus 7
pisteet = int(input("Anna tenttipistemäärä: "))

if 0 <= pisteet <= 11:
    print("Arvosana: hylätty")
elif 12 <= pisteet <= 16:
    print("Arvosana: 1")
elif 17 <= pisteet <= 21:
    print("Arvosana: 2")
elif 22 <= pisteet <= 24:
    print("Arvosana: 3")
else:
    print("Virheellinen pistemäärä")