from tkinter import * # Graafisen käyttäliittymän rakentamiseen
import random
import os # Voi käsitellä tiedotoja, hakemitoja ja suorittaa käyttöjärjestelmään liittyviä tehtäviä

# Pelin asetukset
GAME_WIDTH = 1000 # Pelialueen leveys
GAME_HEIGHT = 550 # pelialueen korkeus
SPEED = 110 # Madon liikkumisnopeus (millisekunteina)
SPACE_SIZE = 50 # Yhden ruudun koko
BODY_PARTS = 3 # Madon alkupituus
SNAKE_COLOR = "#A52A2A" # Madon väri (ruskea)
FOOD_COLOR = "#FF0000" # Ruokapallon väri (punainen)

# Tiedoston nimi top-3 pisteille
HIGHSCORES_FILE = "highscores.txt"

# Luodaan pääikkuna
window = Tk()
window.title("Matopeli") # Sivun-nimi
window.resizable(False, False) # Ei sallita ikkunan koon muuttamista

# Luodaan piirtoalue (Canvas)
canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.place(x=0, y=76)

game_started = False # Seuraa, onko peli käynnissä
start_button = None # Alustetaan start-nappi

def draw_green_grid():
    # Piirtää vihreän ruudukon pelialueelle satunnaisilla sävyillä
    rows = GAME_HEIGHT // SPACE_SIZE
    cols = GAME_WIDTH // SPACE_SIZE

    for i in range(rows):
        for j in range(cols):
            green_shade = random.randint(100, 120) # Satunnainen vihreän sävy
            color = (f'#00{green_shade:02X}00')  #RGB (0, X, 0)

            x1, y1 = j * SPACE_SIZE, i * SPACE_SIZE
            x2, y2, = x1 + SPACE_SIZE, y1 + SPACE_SIZE

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

draw_green_grid()  #Piirrä ruudukko ennen muita elementtejä

# Pisteiden seuranta
pisteet = 0 # Pisteet lähtee nollasta
direction = "down" # Madon aloitussuunta

# Pisteiden näyttö
label = Label(window, text="Pisteet: {}".format(pisteet), font=("consolas", 40))
label.place(x=10, y=10)
    

def update_score_position():
    # Keskittää pistetaulukon pelialueen yläosaan ja päivittää sen automaattisesti
    label.update_idletasks()  
    label.place(x=(GAME_WIDTH - label.winfo_width()) / 2, y=10)  # Asetetaan keskelle
    window.after(10, update_score_position)

update_score_position() # Aloitetaan päivitys

class Snake:
    # Madonluokka, joka vastaa käärmeen luomisesta ja sen kehon hallinnasta
    def __init__(self):
        self.body_size = BODY_PARTS # Käärmeen alkupituus
        self.coordinates = [] # koordinaatit listana
        self.squares = [] # Canvasin piirto-objektit

        # Madon aloituskoordinaatit
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Piirretäänn madon ruumiinosat pelialueelle
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    # Ruokaluokka, joka luo uuden ruoan satunnaiseen kohtaan pelialueella
    def __init__(self):
        
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) -1) * SPACE_SIZE

        self.coordinates =[x, y]

        self.food_item = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    # Päivittää pelitilanteen jokaisella vuorolla.
    # Mato liikkuu, syö ruokaa ja tarkistetaan törmäykset

    global pisteet
    x, y = snake.coordinates[0] # Madon pään sijainti

    # Päivitetään madon suunta
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Lisätään uusi pään sijainti listaan
    snake.coordinates.insert(0, (x, y))

    # Piirretään uusi pään osa
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Tarkistetaan, osuuko mato ruokaan
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global pisteet

        pisteet += 1

        label.config(text="Pisteet: {}".format(pisteet))

        canvas.delete("food") # Poistetaan vanha ruoka

        food = Food() # Luodaan uusi ruoka

        # Lisäpisteitä, jos pisteitä on vähintään 11
        if pisteet >= 11:   #kun saat 10 pistettä saat jatkossa 5 pistettä per "omena" 
                                # mato silti saa vain yhden "palan" lisää
            pisteet += 4

            label.config(text="Pisteet: {}".format(pisteet))

            canvas.delete("food")

            food = Food()

    else:
        # Poistetaan madon viimeinen pala, jos ei syönyt ruokaa
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # Tarkistetaan törmäykset
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food) # Aikataulutetaan seuraava vuoro


def change_direction(new_direction):
    # Vaihtaa käärmeen suunnan, jos se ei ole vastakkainen nykyiseen suuntaan.
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    # Tarkistaa, törmääkö käärme seinään tai itseensä.

    x, y = snake.coordinates[0] # Madon pään sijainti

    # Seinään törmäys
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y <0 or y >= GAME_WIDTH:
        return True
    
    # Itseensä törmäys
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False


# Voi lukea tiedoston ja järjestää paremmuus järjestykseen
def read_highscores():
    try:
        with open(HIGHSCORES_FILE, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
            return sorted(scores, reverse=True)[:3]
    except (FileNotFoundError, ValueError):
        return []
    

# Tallentaa tiedostoon top-3 pisteet
def write_highscores(scores):
    try:
        with open(HIGHSCORES_FILE, "w") as file:
            for score in sorted(scores, reverse=True)[:3]:
                file.write(str(score) + "\n")
    except Exception as e:
        print(f"Virhe tallennattaessa pisteitä: {e}")
    

def game_over():
    # Päättää pelin, poistaa kaiken pelialueelta ja näyttää pelin loppumisviestin.
    global game_started
    canvas.delete(ALL)
    canvas.configure(bg="black")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="Peli loppui!", fill="red", tag="gameover")

    highscores = read_highscores() # Lukee saadut pisteet, kun hävitty peli
    highscores.append(pisteet) # Lisää pisteet fileen, jos top-3
    write_highscores(highscores) # Kirjoittaa fileen

    def return_to_start():
        canvas.delete(ALL)
        show_start_screen()
    window.after(2000, show_start_screen) # Palaa aloitusruutuun
    game_started = False


# Näyttää aloitus ruudun ennen pelin alkua
def show_start_screen():
    canvas.delete("all")
    canvas.configure(bg="#DDFFDD")
    draw_green_grid()


    # Aloitus sivulle näkyy top-3 tulokset, tekstien värit ja koot
    highscores = read_highscores()
    top_text = "Top 3 tulosta: \n"
    for i, score in enumerate(highscores):
        top_text += f"{i+1}. {score} pisteet\n"
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, font=('consolas', 24), text=top_text.strip(), fill="darkblue")


    # Aloitusruudun tekstit
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50, text="Tervetuloa Matopeliin!", font=("consolas", 50), fill="darkblue")

    # Start-nappi
    start_button = Button(window, text="Aloita peli", font=("consolas", 30), bg="#44AA44", fg="white", command=start_game)
    start_button.place(x=GAME_WIDTH / 2 - 100, y=GAME_HEIGHT / 2 + 70, width=200, height=50)
    canvas.create_window(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 50, window=start_button)


# Pelin aloitus
def start_game():
    global pisteet, direction
    pisteet = 0
    direction = "down"
    canvas.delete("all")

    draw_green_grid()
    label.config(text="Pisteet: 0")
    snake = Snake()
    food = Food()
    next_turn(snake, food)


def main():
    # Asetetaan ikkunan koko ja keskitetään näyttöön
    window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT + 200}")
    window.update()

    # Haetaan ikkunan nykyinen leveys ja korkeus
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Haetaan näytön koko (leveys ja korkeus)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Lasketaan x- ja y-koordinaatit, jotta ikkuna asetetaan keskelle näyttöä
    x = int((screen_width / 2 ) - (window_width / 2))
    y = int((screen_height / 2 ) - (window_height / 2))

    # Asetetaan ikkuna keskelle näyttöä
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Näppäinsidonnat ohjaukseen
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    # Näytetään aloitusruut
    show_start_screen()

    window.mainloop()

main()