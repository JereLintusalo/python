from tkinter import *
import random


# Funktio, joka käsittelee seuraavan siirron
# Parametrit: rivi ja sarake, johon pelaaja yrittää asettaa merkin
def next_turn(row, column):
    
    global player

    # Tarkistetaan, onko painike tyhjä ja onko peli vielä kesken
    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            # Asetetaan nykyisen pelaajan merkki painikkeeseen
            buttons[row][column]['text'] = player

            # Tarkistetaan pelin tila
            if check_winner() is False:

                # Vaihdetaan vuoro toiselle pelaajalle
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
    
        else:

            # Asetetaan nykyisen pelaajan merkki painikkeeseen
            buttons[row][column]['text'] = player

            # Tarkistetaan pelin tila
            if check_winner() is False:
                # vaihdetaan vuoro toiselle pelaajalle
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

# Tarkistaa, onko joku voittanut pelin
def check_winner():
    
    # Tarkistetaan vaakarivit
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    # Tarkistetaa pystyrivit
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    # Tarkistetaan päädiagonaali
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    # Tarkistetaan vastakkainen diagonaali
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Tarkistetaan, onko peli tasan
    elif empty_spaces() is False:
        
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False

# Tarkistaa, onko pelilaudalla vielä tyhjiä ruutuja
def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

# Funktio aloittaa uuden pelin
def new_game():
    
    global player

    player = random.choice(players) # Valitaan satunnainen aloitusvuoro

    label.config(text=player+" turn")

    # Tyhjennetään pelilauta
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Luodaan pääikkuna
window = Tk()
window.title("Tic-Tac-Toe")

# Määritetään pelaajat ja asetetaan satunnainen aloitusvuoro
players = ["x","o"]
player = random.choice(players)

# Luodaan painikkeista 3x3-matriisina
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# Luodaan otsikkoteksti, joka kertoo vuorossa olevan pelaajan
label = Label(text= player + " turn", font=('consolas', 40))
label.pack(side="top")

# Reset-nappi uuden pelin aloittamiseksi
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Kehys pelilaudalle
frame = Frame(window)
frame.pack()

# Luodaan 3x3 pelilauta painikkeista
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width = 5, height = 2,
                                      command = lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row,column=column)

# Käynnistetään pääsilmukka
window.mainloop()