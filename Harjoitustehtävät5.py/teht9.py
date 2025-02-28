def main():
    charge_accounts = [
    1234567, 2345678, 3456789, 4567890, 
    5678901,6789012, 7890123, 8901234, 9012345, 
    1123456,2234567, 3345678, 4456789, 5567890, 
    6678901,7789012, 8890123, 9901234, 1012345, 
    2123456,3234567, 4345678, 5456789, 6567890, 
    7678901,8789012, 9890123, 1090123, 2190123, 3290123
    ]

    etsi = int(input("Syötä tilinumerosis: "))

    if etsi in charge_accounts:
        print("Numero on kelvollinen!")
    else:
        print("Numero on virheellinen!")

main()