from tkinter import * # Voi käyttää Tk, Button, Label, Canvas jne. (ilman tk.Button jne)
import subprocess # Mahdollistaa ulkoisten ohjelmien ajamisen eli tässä tapauksessa pelien
import tkinter as tk # Voi käyttää Tk lyhenteitä

# Tuodaan peli tiedostot tälle sivulle
def open_ristinolla():
    subprocess.Popen(["python", "ristinolla.py"])
def open_matopeli():
    subprocess.Popen(["python", "matopeli.py"])

def main():
    page_width = 800 # Sivun leveys
    page_height = 500 # Sivun korkeus

    root = tk.Tk()
    root.title("Pelit") #Sivun nimi
    root.geometry("300x200") #Sivun koko
    root.configure(bg="#e0e0e0") #Sivun taustaväri

    # Asetetaan ikkunan koko ja keskitetään näyttöön
    root.geometry(f"{page_width}x{page_height + 150}")
    root.update()

    # Haetaan ikkunan nykyinen leveys ja korkeus
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Haetaan näytön koko (leveys ja korkeus)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Lasketaan x- ja y-koordinaatit, jotta ikkuna asetetaan keskelle näyttöä
    x = int((screen_width / 2 ) - (window_width / 2))
    y = int((screen_height / 2 ) - (window_height / 2))

    # Asetetaan ikkuna keskelle näyttöä
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Otsikko tekstit ja värit
    label1 = Label(text="Tervetuloa!\n Tässä on muutama peli!", font=('consolas', 30), bg="#e0e0e0")
    label1.pack(pady=(20, 10))
    label2 = Label(text="\nVoit pelata kumpaa haluat!", font=("consolas", 20), bg="#e0e0e0")
    label2.pack(pady=(0, 20))

    # Painikkeide koot ja värit ja missä sijaitsee
    button_frame = Frame(root, bg="#e0e0e0")
    button_frame.pack(fill="x", pady=10)
    left_frame = Frame(button_frame, bg="#e0e0e0")
    left_frame.pack(side="left", expand=True)
    rigth_frame = Frame(button_frame, bg="#e0e0e0")
    rigth_frame.pack(side="right", expand=True)

    # Kaksi painiketta ja niiden tekstit ja koot ja "import" siihen peliin
    xo_button = Button(left_frame, text="Ristinolla", font=("consolas", 20), command=open_ristinolla)
    xo_button.pack()
    snake_button = Button(rigth_frame, text="Matopeli", font=("consolas", 20), command=open_matopeli)
    snake_button.pack()

    # Sivun keskellä oleva teksti
    middle_label = Label(text="Lisää pelejä tulossa...", font=("consolas", 18), bg="#e0e0e0")
    middle_label.pack(fill="x", pady=120)

    # Sivun alareunan teksti ja koko
    author_label = Label(text="Tekijä: Jere Lintusalo", font=("consolas", 12), bg="#e0e0e0")
    author_label.pack(side="bottom", pady=10)

    # Sivun piirtoalusta ja taustaväri harmaa
    #Luo Canvas-olion, joka on osa Tkintterin käyttöliittymää ja 
    # määrittelee sen koon
    canvas = Canvas(root, height=page_height, width=page_width, bg="#e0e0e0")
    
    # lisää Canvas pääikkunaan ja (root) ja varmistaa ympärille 
    # jää 20 pikseliä tyhjää tilaa ylle ja alle
    canvas.pack(pady=20)

    # Käynnistys
    root.mainloop()

# Ajaa vain jos tiedosto suoritetaan suoraan
if __name__ == "__main__":
    main()