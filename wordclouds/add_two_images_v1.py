from PIL import Image
#Read the two images
path1=input("caminho 1-imagem")
path2=input("caminho 2-imagem")
image1 = Image.open(path1)
# print(type(image1))
#image1.show()
image2 = Image.open(path2)
#image2.show()
#resize, first image
image1 = image1.resize((200, 200))
image2 = image2.resize((200, 200))
image1_size = image1.size
image2_size = image2.size

new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("imagens/merged_image.png","PNG")
new_image.show()