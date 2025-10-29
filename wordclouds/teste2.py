# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
df = pd.read_csv("data/data_arrhythmia.csv", index_col=0)
print(df.head())
print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of wine in this dataset such as {}... \n".format(len(df.weight.unique()),", ".join(df.weight.unique()[0:5])))

print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.sex.unique()), ", ".join(df.sex.unique()[0:5])))