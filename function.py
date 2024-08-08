import numpy as np
import pandas as pd
import random as rand


data=pd.read_csv("main.csv")
second_row=data.iloc[1]
a=rand.choice(second_row)

print(a)