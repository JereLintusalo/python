# Noppapeli - Ensimmäisenä 50 pistettä saanut voittaa

import random  # Tarvitaan satunnaiseen nopanheittoon

def roll():
    """
    Heittää noppaa ja palauttaa satunnaisen luvun väliltä 1-6.
    """
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)  # Arvotaan satunnainen numero
    return roll

# Pyydetään pelaajien lukumäärä ja varmistetaan, että se on kelvollinen (2-4)
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():  # Varmistetaan, että syöte on numero
        players = int(players)
        if 2 <= players <= 4:
            break  # Kelvollinen pelaajamäärä -> jatketaan peliin
        else:
            print("Must be between 2 - 4 players.")  # Virheilmoitus
    else:
        print("Invalid, try again!")  # Virheilmoitus, jos syöte ei ole numero

# Pelin voittoon vaadittu pistemäärä
max_score = 50

# Pelaajien pistetaulukko, alussa kaikilla 0 pistettä
player_score = [0 for _ in range(players)]

# Peli jatkuu, kunnes joku saavuttaa max_score:n
while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print(f"Your total score is: {player_score[player_idx]}\n")

        current_score = 0  # Tämän kierroksen pisteet

        # Pelaaja voi heittää noppaa niin kauan kuin haluaa, mutta 1:sen heittäminen nollaa kierroksen pisteet
        while True:
            should_roll = input("Would you like to roll (y)? ")  # Kysytään, haluaako pelaaja heittää
            if should_roll.lower() != "y":  # Jos vastaus ei ole 'y', siirrytään seuraavaan pelaajaan
                break

            value = roll()  # Heitetään noppaa
            if value == 1:
                print("You rolled a 1! Turn done!")  # Jos nopan tulos on 1, menetetään kierroksen pisteet
                current_score = 0
                break
            else:
                current_score += value  # Muut arvot lisätään kierroksen pisteisiin
                print(f"You rolled a: {value}")

            print(f"Your score this turn is: {current_score}")

        # Kierroksen pisteet lisätään pelaajan kokonaistulokseen
        player_score[player_idx] += current_score
        print(f"Your total score is: {player_score[player_idx]}")

# Selvitetään voittaja
max_score = max(player_score)
winning_idx = player_score.index(max_score)  # Haetaan voittajan indeksi listasta
print(f"Player number {winning_idx + 1} is the winner with a score of: {max_score}")

