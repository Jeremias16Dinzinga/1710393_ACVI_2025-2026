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
comment="""
- a imagem, como mask, deve estar na pasta imagens 
- a imagem deve ser de extensão png
- deve existir um texto, extensao txt, texts com o mesmo nome da mascara
na pasta deve ser de extensão png\n
"""
print(comment+"\n")
str=input("Indique o nome da mask:")
try:
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if ("__file__") in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, "texts/"+str+".txt")).read()
    stop = input("stopwords <word1>,<word2>,<word3>:")
    set2 = {p.strip() for p in stop.split(',')}
    stopwords = STOPWORDS.union(set2)
    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg

    alice_mask = np.array(Image.open(path.join(d, "imagens/"+str+"_mask.png")))

    #stopwords = set(STOPWORDS)
    stopwords.add("THE END")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "imagens/"+str+".png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    #plt.figure()
    #plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    #plt.axis("off")
    plt.show()

except:
    print("Imagem ou texto nao encontrado")