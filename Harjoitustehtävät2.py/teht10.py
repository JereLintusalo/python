while True:
    try:
        n = int(input("Anna Fibonaccin luvun n arvo: "))
        
        if n < 0:
            print("Anna positiivinen kokonaisluku.")
        else:
            break
    except ValueError:
        print("Virheellinen syöte! Anna kokonaisluku.")

a, b = 0, 1  
i = 0

while i <= n:
    print(f"F({i}) = {a}")
    a, b = b, a + b 
    i += 1 
            