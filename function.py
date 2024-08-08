<<<<<<< HEAD
import numpy as np
import pandas as pd
import random as rand


data=pd.read_csv("main.csv",encoding="ISO-8859-1")
second_row=data.iloc[1]
a=rand.choice(second_row)

print(a)
=======

import numpy as np
import pandas as pd
import random as rand
import csv 


data=pd.read_csv("imdb1000.csv",encoding="ISO-8859-1", on_bad_lines='skip')
a=rand.randint(1,900)
film1=data.loc[a][1]

print(film1)
>>>>>>> 0261c0e1f7a506d69f2bf67bcaa9af99b08ff153
