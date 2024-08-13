import pandas as pd
import random as rand
import time


print("\nMovie Guesser")
time.sleep(2)

while True:
    try: 
        isim=(input("İsminizi Giriniz:" ))
        if not(isim.isalpha()):
            raise ValueError
        
    except ValueError:
        print("Lütfen İsminizi Doğru Girdiğinizden Emin Olun")
    else:
        break
    
time.sleep(2)
print(f"Hoş Geldin {isim}!\n")
time.sleep(2)
print("IMDB Top1000 listesindeki filmlerden karşına çıkacak iki filmden hangisinin daha önce vizyona girdiğini doğru tahmin et, yıldızları topla, oyunu kazan!\n\nUnutma yalnızca 3 yanlış yapma hakkın var" )
time.sleep(3)
print("10, 25, 50, 100, 250, 500 skorlarından her birine ulaştığında bir yıldız kazanacaksın.\n")
time.sleep(1)
print("00--->Acemi Balık\n10--->Taze Fasulye\n25--->Sinemasever\n50--->Olgunlaşmış Karpuz\n100--->Haşlanmış Patates\n250--->Nuri Bilge Ceylan\n500--->FilmMaster\n")
time.sleep(2)
print("İyi Şanslar :)\n")

def game():
    can_sayisi=3
    skor=0
    yildiz_sayisi=0
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
        print(movie1.name,"vs",movie2.name,"\n")
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
            #TODO:SKOR sol üstte VE CAN HER ZAMAN SAĞ ÜSTTE NASIL YAZACAK
        elif guess!=answer:
            print("Yanlış!\n1 Can Kaybettin")
            can_sayisi-=1
            print("Skor:",skor,"Can Sayısı:",can_sayisi)
        elif skor==10:
            yildiz_sayisi+=1
        elif skor==25:
            yildiz_sayisi+=1
        elif skor==50:
            yildiz_sayisi+=1
        elif skor==100:
            yildiz_sayisi+=1
        elif skor==250:
            yildiz_sayisi+=1
        elif skor==500:
            yildiz_sayisi+=1
        #sol üstte yıldızlar görünecek
        a=b
        b=rand.randint(1,985)
    
    if can_sayisi==0:
        print("Ha ha öldün çık:)") 
        print("Skorunuz:",skor) 
        if skor==0:
            print("--Acemi Balık--")
        elif skor<10:
            print("--Taze Fasulye--\n")
        elif skor<25:
            print("--Sinemasever--")
        elif skor<50:
            print("--Olgunlaşmamış Karpuz--")
        elif skor<100:
            print("--Haşlanmış Patates--")
        elif skor<250:
            print("--Nuri Bilge Ceylan--")
        elif skor<500:
            print("--FilmMaster--")
    if skor>980:
            print("Sana sıfat bile vermiyoruz, gidip sosyalleşmeni ve çimene dokunmanı tavsiye ederiz :)")
#rondom film çıkabilir
      
game()