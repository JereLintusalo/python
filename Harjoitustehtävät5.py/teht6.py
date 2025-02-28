import random

lotto_nro = [random.randint(1, 40) for _ in range(7)]

print("Lottorivi:")
for number in lotto_nro:
    print(number, end=" ")