# Math test - turvallinen versio ilman eval-funktiota

import random  # Satunnaislukujen ja operaattorien valintaan
import time  # Ajastukseen, jotta voidaan mitata suoritusaika
import operator  # Turvallisiin laskutoimituksiin ilman evalia

# Mahdolliset operaattorit ja niitä vastaavat funktiot
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

# Määritellään pienin ja suurin luku, joita voidaan käyttää laskuissa
MIN_OPERAND = 3
MAX_OPERAND = 12

# Määritetään, kuinka monta laskutehtävää käyttäjän täytyy ratkaista
TOTAL_PROBLEMS = 10

def generate_problem():
    """
    Luo satunnaisen matemaattisen ongelman turvallisesti.
    Palauttaa laskutoimituksen merkkijonona ja oikean vastauksen.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Ensimmäinen luku
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Toinen luku
    operator_symbol, operation = random.choice(list(OPERATORS.items()))  # Satunnainen operaattori

    expr = f"{left} {operator_symbol} {right}"  # Rakennetaan lasku merkkijonona
    answer = operation(left, right)  # Lasketaan tulos turvallisesti ilman evalia
    return expr, answer

# Lasketaan väärin vastattujen tehtävien määrä
wrong = 0

# Käynnistetään peli painamalla enteriä
input("Press enter to start!")
print("----------------------")

# Aloitetaan ajanotto
start_time = time.time()

# Käydään läpi kaikki määritellyt laskutehtävät
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Luodaan uusi tehtävä
    
    while True:
        # Pyydetään käyttäjää syöttämään vastaus
        guess = input(f"Problem #{i + 1}: {expr} = ")
        
        # Tarkistetaan, onko vastaus oikein
        if guess.isdigit() or (guess.startswith("-") and guess[1:].isdigit()):  # Varmistetaan, että vastaus on numero
            if int(guess) == answer:
                break  # Jos oikein, siirrytään seuraavaan tehtävään
        
        wrong += 1  # Lisätään väärien vastausten laskuriin yksi

# Lopetetaan ajanotto ja lasketaan kokonaisaika
end_time = time.time()
total_time = end_time - start_time  # Kokonaisaika sekunneissa

print("--------------------------")
print(f"Nice work! You finished in {total_time:.2f} seconds!")  # Tulostetaan suoritusaika
