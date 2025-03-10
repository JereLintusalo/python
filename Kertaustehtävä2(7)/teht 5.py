questions = [
    {
        "prompt": "Mikä on Suomen pääkaupunki?",
        "options": ["A. Turku", "B. Tampere", "C. Helsinki", "D. Oulu"],
        "answer": "C"
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
    },
    {
        "prompt": "Mitkä värit on Suomen lipussa?",
        "options": ["A. Punainen ja Musta", "B. Sininen ja Valkoinen", "C. Keltainen ja Sininen", "D. Vihreä ja Valkoinen"],
        "answer": "B"
    }
]

def suorita_peli(questions):
    tulos = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        vastaus = input("Anna vastauksesi (A, B, C vai D): ").upper()

        if vastaus == question["answer"]:
            print("Oikein!\n")
            tulos += 1
        else:
            print(f"Väärin! Oikea vastaus oli {question['answer']}\n")
    print(f"Sait {tulos} kysymystä oikein {len(questions)}:stä kysymyksestä!")

suorita_peli(questions)

