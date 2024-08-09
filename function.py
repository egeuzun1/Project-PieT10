import pandas as pd
import random as rand
import time



print("Movie Guesser")
time.sleep(2)
print("Hoş Geldinn")
time.sleep(2)
print("IMDB Top1000 listesindeki filmlerden karşına çıkacak iki filmden hangisinin daha önce vizyona girdiğini doğru tahmin et yıldızları topla oyunu kazan! \n Unutma yalnızca 3 yanlış yapma hakkın var" )
#10 25 50 100 250 500 980
print("10, 25, 50, 100, 250, 500 skorlarından her birine ulaştığında bir yıldız kazanacaksın.")
time.sleep(2)
print("İyi Şanslar :)")


def game():
    can_sayisi=3
    skor=0
    a=rand.randint(1,985)
    b=rand.randint(1,985)
    while can_sayisi>0:
        movie=pd.read_csv("imdb1000.csv",encoding="ISO-8859-1", on_bad_lines='skip')
        
        if movie.loc[a]["year"]==movie.loc[b]["year"]:
            b=rand.randint(1,900)
        class movie1:
            poster=movie.loc[a]["Link"]
            name=movie.loc[a]["name"]
            year=movie.loc[a]["year"]
            
        class movie2:
            poster=movie.loc[b]["Link"]
            name=movie.loc[b]["name"]
            year=movie.loc[b]["year"]
        print(movie1.name,"vs",movie2.name)
        guess=int(input("Hangisi daha önce çıkan bir filmdir?(1. Film için 1, ikincisi için 2 yazınız.)")) #TODO: tıklayarak nasıl olacak, tryexcept kullanarak
        def answer():
            if movie1.year<movie2.year:
                return 1
            else:
                return 2
        if guess==answer():
            print("Doğru!\n+1 Puan")
            skor+=1
            print(movie1.year,movie2.year)
            print("Skor:",skor,"Can Sayısı:",can_sayisi)
            #TODO:SKOR VE CAN HER ZAMAN SAĞ ÜSTTE NASIL YAZACAK
        elif guess!=answer:
            print("Yanlış!\n1 Can Kaybettin")
            can_sayisi-=1
            print("Skor:",skor,"Can Sayısı:",can_sayisi)
        a=b
        b=rand.randint(1,985)
    
    if can_sayisi==0:
        print("Ha ha öldün çık:)")
        print(skor)
        print("0--->Acemi Balık \n 10--->Taze Fasulye \n 25--->Sinemasever \n 50--->Olgunlaşmış Karpuz \n 100--->Haşlanmış Patates \n 250--->Nuri Bilge Ceylan \n 500--->FilmMaster \n 980-->Kanka git sosyalleş")  
#10 25 50 100 250 500 980
#rondom film çıkabilir
      
game()


