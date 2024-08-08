
import numpy as np
import pandas as pd
import random as rand


data=pd.read_csv("main-dataset.csv")
second_row=data.iloc[2]
a=rand.choice(second_row)

print(a)
