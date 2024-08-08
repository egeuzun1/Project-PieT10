
import numpy as np
import pandas as pd
import random as rand
import csv 


data=pd.read_csv("imdb1000.csv",encoding="ISO-8859-1", on_bad_lines='skip')
a=rand.randint(1,900)
film1=data.loc[a][1]

print(film1)
