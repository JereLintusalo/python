# Hirsipuu-peli (Hangman)

import random  # Satunnaisesti valittavan sanan valitsemiseen

# Lista mahdollisista sanoista, jotka voivat olla mitä tahansa.
# Jos sanat ovat pidempiä, voi olla hyvä lisätä yritysten määrää.
words = ["python", "java", "javascript", "html"]

# Valitaan satunnaisesti yksi sana listasta
chosen_word = random.choice(words)

# Luodaan näkyviin aluksi vain alaviivat (_), yksi jokaiselle kirjaimelle
word_display = ['_' for _ in chosen_word]

# Määritetään, montako virheellistä arvauksia pelaajalla on ennen häviämistä
attempts = 8

# Peli jatkuu, kunnes pelaaja on joko arvannut kaikki kirjaimet tai yritykset loppuvat
while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))  # Tulostetaan nykyinen sanan tila
    guess = input("Guess a letter: ").lower()  # Pyydetään pelaajaa arvaamaan kirjain

    # Tarkistetaan, esiintyykö arvattu kirjain sanassa
    if guess in chosen_word:
        # Käydään sana läpi ja paljastetaan kaikki oikeat kirjaimet
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Korvataan alaviiva oikealla kirjaimella
    else:
        print("That letter doesn't appear in the word!")
        attempts -= 1  # Vähennetään yrityksiä yhdellä

# Pelin lopputulos
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")  # Pelaaja voitti
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")  # Pelaaja hävisi
