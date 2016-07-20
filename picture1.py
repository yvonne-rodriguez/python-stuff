from PIL import Image

im=Image.open("image.jpg") 

pixels= im.getdata()
data_list= list(pixels)

darkblue = (0, 51, 76)
red = (217, 26, 33)
lightblue = (112, 150, 158)
yellow = (252, 227, 166)
newlist = []

#new_im = Image.new("RGB", (512, 512))

    


for data in data_list:
    r= data [0]
    b= data [1]
    g= data[2]
    x=r+b+g
    if x<=182:
        new=darkblue
    if 182<x<=364:
        new=red
    if 364<x<=546:
        new=lightblue
    if x>546:
        new= yellow
    newlist.append(new)
    
im.putdata(newlist)
im.show()