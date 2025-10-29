# import image module from pillow
from PIL import Image

# open the image
Image1 = Image.open('./imagens/seta_mask.png')

# make a copy the image so that the
# original image does not get affected
for x in range(1,15):
    Image1copy = Image1.copy()
    # save the image
    Image1copy.save('./imagens/group/seta'+str(x)+'_mask.png')

print("FIM")