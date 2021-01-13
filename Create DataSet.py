#create dataset
import os
from shutil import copyfile
os.mkdir('dataset') 
folders=[]
xmls= os.listdir('xml')
for xml in xmls:
    f = open("xml/"+xml, "r")
    image=xml.split('.')[0]
    if(image[0] not in ['a','b','c','d']):
        continue
    writer=''
    for i,x in enumerate(f):
        if i==4:
            l=x.split(' ')[9].split('=')[1]
            writer+=l[1]+l[2]+l[3]
            if writer not in folders:
                os.mkdir('dataset/'+writer)
                folders.append(writer)
            copyfile('formsA-D/'+image+'.png', 'dataset/'+writer+'/'+image+'.png')
            break
