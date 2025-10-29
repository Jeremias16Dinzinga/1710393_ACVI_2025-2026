from PIL import Image
#Read the two images
#image1 = Image.open('images/elephant.jpg')
#!/usr/bin/env python
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

for x in range(1,15):

    stru="seta"
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    y=str(x)
    text = open(path.join(d, "texts/group/"+stru+y+".txt")).read()


    alice_mask = np.array(Image.open(path.join(d, "imagens/"+stru+"_mask.png")))

    stopwords = set(STOPWORDS)
    stopwords.add("THE_END")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "imagens/group/"+stru+str(x)+"_mask.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    #plt.figure()
    #plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    #plt.axis("off")
    # plt.show()
