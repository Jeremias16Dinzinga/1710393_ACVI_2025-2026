# import image module from pillow
from PIL import Image

# open the imagens
path=input("Image you want replicate? ")
num_copias=int(input("How many copies? "))
try:
    Image1 = Image.open(path)

    # make a copy the image so that the
    # original image does not get affected
    
    for x in range(1,num_copias):
        Image1copy = Image1.copy()
        # save the image
        Image1copy.save('./imagens/group/seta'+str(x)+'_mask.png')

except:
    print("ficheiros não existe")
print("FIM")