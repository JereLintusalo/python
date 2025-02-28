import random

def roll(number_of_throws):
    heitot = [random.randint(1, 6) for _ in range(number_of_throws)]
    return sorted(heitot)

while True:
    try:
        number_of_throws = int(input("Anna positiivinen kokonaisluku (nopan heittojen määrä): "))
        if number_of_throws > 0:
            break
        else:
            print("Syötteen täytyy olla positiivinen kokonaisluku.")
    except ValueError:
        print("Virheellinen syöte! Yritä uudelleen!")

tulokset = roll(number_of_throws)
print(f"Lajiteltu heittotulos: {tulokset}")