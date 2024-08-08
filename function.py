
import numpy as np
import pandas as pd
import random as rand
import csv 


movie=pd.read_csv("imdb1000.csv",encoding="ISO-8859-1", on_bad_lines='skip')
a=rand.randint(1,900)
b=rand.randint(1,900)

class movie1:
    #Poster linkini ekleyemedik:()
    name=movie.loc[a]["name"]
    year=movie.loc[a]["year"]
    

class movie2:
    #Poster linkini ekleyemedik:(
    name=movie.loc[b]["name"]
    year=movie.loc[b]["year"]


def game(movie1,movie2):
    print(movie1,"vs",)


       




