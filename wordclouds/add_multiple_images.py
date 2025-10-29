from PIL import Image
#Read the two images

stru="seta"
image_list=[]
image_list_size=[]
image_start=Image.open("./imagens/group/timegame.png")
image_startr=image_start.resize((800,100))
image_final=Image.open("./imagens/group/ldfp.png")
image_finalr=image_final.resize((800,100))
for x in range(1,15):
    image_aux= Image.open("./imagens/group/"+stru+str(x)+"_mask.png")
    image = image_aux.resize((200, 200))
    image_size = image.size
    image_list.append(image)
    image_list_size.append(image_size)
    image_aux.close()


#resize, first image
print(type(image_list[0]))
print(image_list[0])
width, height = image_list[0].size
print(width,height)
print(image_list_size[0])

new_image = Image.new(mode='RGB',size=(4*image_list_size[0][0],
                    4*image_list_size[0][1]), color=(250,250,250))
#new_image.paste(image_startr,(0,0))
new_image.paste(image_list[0],(0,0))
new_image.paste(image_list[1],(200,0))
new_image.paste(image_list[2],(400,0))

new_image.paste(image_list[6],(600,100))

new_image.paste(image_list[3],(0,200))
new_image.paste(image_list[4],(200,200))
new_image.paste(image_list[5],(400,200))

#new_image.paste(image_finalr,(0,400))
new_image.paste(image_list[7],(0,400))
new_image.paste(image_list[8],(200,400))
new_image.paste(image_list[9],(400,400))

new_image.paste(image_list[13],(600,500))

new_image.paste(image_list[10],(0,600))
new_image.paste(image_list[11],(200,600))
new_image.paste(image_list[12],(400,600))


new_image.save("./imagens/group/merged_image_"+stru+".png","PNG")
new_image.show()
