import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("cleaned.csv")

'''
80:20 train test split
'''
train, test = train_test_split(df, test_size=.2, random_state=42, stratify=df['FLAG'])

train.to_csv("train.csv")
test.to_csv("test.csv")
