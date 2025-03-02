# Quiz Game - Tietovisa

# Lista kysymyksistä ja vastausvaihtoehdoista
questions = [
    {
        "prompt": "Mikä on Suomen pääkaupunki?",  # Kysymys
        "options": ["A. Turku", "B. Tampere", "C. Helsinki", "D. Oulu"],  # Vastausvaihtoehdot
        "answer": "C"  # Oikea vastaus
    },
    {
        "prompt": "Mikä on toinen kieli, mitä Kanadassa puhutaan?",
        "options": ["A. Saksa", "B. Ranska", "C. Italia", "D. Espanja"],
        "answer": "B"
    },
    {
        "prompt": "Mikä on pienin luku?",
        "options": ["A. 9", "B. 8", "C. 11", "D. 3"],
        "answer": "D"
    },
    {
        "prompt": "Kuka on tehnyt Mona Lisan?",
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Albert Edelfelt", "D. Pablo Picasso"],
        "answer": "A"
    }
]

def run_quiz(questions):
    """
    Suorittaa visan, jossa pelaaja vastaa kysymyksiin ja saa pisteitä oikeista vastauksista.
    """
    score = 0  # Alustetaan pisteet

    for question in questions:  # Käydään kaikki kysymykset läpi
        print(question["prompt"])  # Tulostetaan kysymys
        for option in question["options"]:  # Tulostetaan vastausvaihtoehdot
            print(option)

        # Pyydetään käyttäjältä vastaus ja varmistetaan, että se on isoilla kirjaimilla
        answer = input("Anna vastauksesi (A, B, C vai D): ").upper()

        # Tarkistetaan, onko vastaus oikein
        if answer == question["answer"]:
            print("Oikein, jippiii!\n")
            score += 1  # Lisätään piste, jos vastaus on oikein
        else:
            print(f"Väärin! Oikea vastaus oli {question['answer']}\n")  # Tulostetaan oikea vastaus

    # Tulostetaan lopputulos
    print(f"Sait {score} kysymystä oikein {len(questions)}:stä kysymyksestä!")

# Käynnistetään peli
run_quiz(questions)