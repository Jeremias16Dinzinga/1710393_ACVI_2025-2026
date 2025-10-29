import collections
import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud, STOPWORDS

all_headlines = input("Escreva um texto: ")
stop = input("stopwords <word1>,<word2>,<word3>:")
set2 = {p.strip() for p in stop.split(',')}
stopwords = STOPWORDS.union(set2)
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      max_words=1000).generate(all_headlines)
rcParams['figure.figsize'] = 10, 10
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
filtered_words = [word for word in all_headlines.split() if word not in stopwords]
counted_words = collections.Counter(filtered_words)
words = []
counts = []
for letter, count in counted_words.most_common(10):
    words.append(letter)
    counts.append(count)
colors = cm.rainbow(np.linspace(0, 1, 10))
rcParams['figure.figsize'] = 10, 10
plt.title('Top words in the headlines vs their count')
plt.xlabel('Count')
plt.ylabel('Words')
plt.barh(words, counts, color=colors)
plt.show()
print("\n ******************")
print(words)
print("\n ******************")
print(counts)