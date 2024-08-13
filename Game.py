import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import random as rand
import requests
from io import BytesIO

Image.MAX_IMAGE_PIXELS = None
df = pd.read_csv('IMDb_dataset.csv', delimiter=';', on_bad_lines='skip')

class Game:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.rights_left = 0
        self.stars = 0
        self.player_name = ""
        self.difficulty = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(fill='both', expand=True)

        self.welcome_label = tk.Label(self.welcome_frame, text="Hoşgeldin!", font=("Helvetica", 20))
        self.welcome_label.pack(pady=20)

        self.explanation_label = tk.Label(self.welcome_frame, text="IMDB Top1000 listesindeki filmlerden karşına çıkacak iki filmden hangisinin önce vizyona girdiğini doğru tahmin et, \n yıldızları topla, oyunu kazan!", font=("Helvetica", 18))
        self.explanation_label.pack(pady=10)

        self.rules_label = tk.Label(self.welcome_frame, text="10, 25, 50, 100, 250, 500 skorlarından her birine ulaştığında bir yıldız kazanacaksın. \n00--->Acemi Balık\n10--->Taze Fasulye\n25--->Sinemasever\n50--->Olgunlaşmış Karpuz\n100--->Haşlanmış Patates\n250--->Nuri Bilge Ceylan\n500--->FilmMaster", font=("Helvetica", 16))
        self.rules_label.pack(pady=10)

        self.name_label = tk.Label(self.welcome_frame, text="İsminiz:", font=("Helvetica", 14))
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.welcome_frame, font=("Helvetica", 14))
        self.name_entry.pack(pady=10)

        self.difficulty_label = tk.Label(self.welcome_frame, text="Zorluk Seçin:", font=("Helvetica", 14))
        self.difficulty_label.pack(pady=10)

        self.difficulty_var = tk.StringVar(value="Kolay")

        self.easy_button = tk.Radiobutton(self.welcome_frame, text="Kolay", variable=self.difficulty_var, value="Kolay", font=("Helvetica", 14))
        self.easy_button.pack()

        self.medium_button = tk.Radiobutton(self.welcome_frame, text="Orta", variable=self.difficulty_var, value="Orta", font=("Helvetica", 14))
        self.medium_button.pack()

        self.hard_button = tk.Radiobutton(self.welcome_frame, text="Zor", variable=self.difficulty_var, value="Zor", font=("Helvetica", 14))
        self.hard_button.pack()

        self.start_button = tk.Button(self.welcome_frame, text="Başla", command=self.start_game, font=("Helvetica", 14))
        self.start_button.pack(pady=20)

        self.game_frame = tk.Frame(self.root)

        self.movie1_label = tk.Label(self.game_frame, text="", font=("Helvetica", 16))
        self.movie1_label.grid(row=0, column=0, padx=40, pady=20, sticky="n")

        self.movie1_image = tk.Label(self.game_frame)
        self.movie1_image.grid(row=1, column=0, padx=40, pady=20, sticky="n")

        self.movie2_label = tk.Label(self.game_frame, text="", font=("Helvetica", 16))
        self.movie2_label.grid(row=0, column=1, padx=40, pady=20, sticky="n")

        self.movie2_image = tk.Label(self.game_frame)
        self.movie2_image.grid(row=1, column=1, padx=40, pady=20, sticky="n")

        self.guess1_button = tk.Button(self.game_frame, text="Seç", command=lambda: self.check_guess(1), font=("Helvetica", 14))
        self.guess1_button.grid(row=2, column=0, pady=20, sticky="n")

        self.guess2_button = tk.Button(self.game_frame, text="Seç", command=lambda: self.check_guess(2), font=("Helvetica", 14))
        self.guess2_button.grid(row=2, column=1, pady=20, sticky="n")

        self.score_label = tk.Label(self.game_frame, text="Skor: 0", font=("Helvetica", 16))
        self.score_label.grid(row=3, columnspan=2, pady=20, sticky="s")

        self.rights_label = tk.Label(self.game_frame, text=f"Kalan Hak: {self.rights_left}", font=("Helvetica", 16))
        self.rights_label.grid(row=4, columnspan=2, pady=20, sticky="s")

        self.star_label = tk.Label(self.game_frame, text=f"Stars: {self.stars}", font=("Helvetica", 16))
        self.star_label.grid(row=5, columnspan=2, pady=20, sticky="s")

    def load_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            image = image.resize((250, 350), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            messagebox.showinfo("Error", f"Fotoğraf yüklenemedi :( {e}")
            return

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("Input Error", "Lütfen İsminizi Doğru Girdiğinizden Emin Olun.")
            return
        
        self.difficulty = self.difficulty_var.get()
        
        
        if self.difficulty == "Kolay":
            self.rights_left = 9
        elif self.difficulty == "Orta":
            self.rights_left = 6
        else:
            self.rights_left = 3

        self.score = 0
        self.stars = 0
        self.update_rights_label()
        
        self.welcome_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.next_round()

    def next_round(self):
        a = rand.randint(1, len(df) - 15)
        b = rand.randint(1, len(df) - 15)
        
        self.movie1 = {
            "name": df.loc[a]["Series_Title"],
            "year": df.loc[a]["Released_Year"],
            "poster": df.loc[a]["Poster_Link"],
            "rating": df.loc[a]["IMDB_Rating"]
        }
        self.movie2 = {
            "name": df.loc[b]["Series_Title"],
            "year": df.loc[b]["Released_Year"],
            "poster": df.loc[b]["Poster_Link"],
            "rating": df.loc[b]["IMDB_Rating"]
        }
        
        if self.movie1["year"] == self.movie2["year"]:
            b = rand.randint(1, len(df) - 15)

        self.movie1_label.config(text=self.movie1["name"])
        self.movie2_label.config(text=self.movie2["name"])
        
        img1 = self.load_image(self.movie1["poster"])
        img2 = self.load_image(self.movie2["poster"])
        
        if img1:
            self.movie1_image.config(image=img1)
            self.movie1_image.image = img1  
        else:
            self.movie1_image.config(text="Görsel bulunamadı")
            
        if img2:
            self.movie2_image.config(image=img2)
            self.movie2_image.image = img2  
        else:
            self.movie2_image.config(text="Görsel bulunamadı")
        
        self.update_score_label()

    def check_guess(self, guess):
        global score, rights_left, stars
        def answer():
            if self.movie1["year"] < self.movie2["year"]:
                return 1
            else:
                return 2
        
        if guess == answer():
            self.score += 1
            result = "Tebrikler, doğru!"
        else:
            self.rights_left -= 1
            result = "Ups, yanlış cevap!"
        
        
        movie1_details = (f"{self.movie1['name']}:\nReleased Year: {self.movie1['year']}\n"
                          f"IMDb Rating: {self.movie1['rating']}")
        movie2_details = (f"{self.movie2['name']}:\nReleased Year: {self.movie2['year']}\n"
                          f"IMDb Rating: {self.movie2['rating']}")

        messagebox.showinfo(result, f"{result}\n\n{movie1_details}\n\nVS\n\n{movie2_details}")

        self.update_score_label()
        self.update_rights_label()
        self.update_star_label()

        if self.rights_left == 0:
            self.show_final_message()
            self.game_frame.pack_forget()
            self.welcome_frame.pack(fill='both', expand=True)
        else:
            self.next_round()
    def update_star_label(self):
        if self.score in [10, 25, 50, 100, 250, 500]:
            self.stars += 1
        self.star_label.config(text=f"Stars: {self.stars}")

    def show_final_message(self):
        if self.score == 0:
            title = "Acemi Balık'sın"
        elif self.score < 10:
            title = "--Taze Fasulye--"
        elif self.score < 25:
            title = "--Sinemasever--"
        elif self.score < 50:
            title = "--Olgunlaşmamış Karpuz--"
        elif self.score < 100:
            title = "--Haşlanmış Patates--"
        elif self.score < 250:
            title = "--Nuri Bilge Ceylan--"
        elif self.score < 500:
            title = "--FilmMaster--"
        elif self.score > 980:
            title = "Sana sıfat bile vermiyoruz, gidip sosyalleşmeni ve çimene dokunmanı tavsiye ederiz :)"
        else:
            title = "Great Job!"

        messagebox.showinfo("Game Over", f"{self.player_name}, {title}\nSkorun: {self.score}.\nStars: {self.stars}")

    def update_score_label(self):
        self.score_label.config(text=f"Skor: {self.score}")

    def update_rights_label(self):
        self.rights_label.config(text=f"Kalan Hak: {self.rights_left}")

root = tk.Tk()
root.title("IMDb Tahmin Oyunu")
root.geometry("950x780")

game = Game(root)

root.mainloop()

   
