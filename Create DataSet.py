#create dataset
import os
from shutil import copyfile, rmtree, move



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
            
            
for writer in os.listdir('dataset'):
    if len(os.listdir('dataset/'+writer))<2:
        rmtree('dataset/'+writer)
        
        
        
writers= os.listdir('dataset')
for writer in writers:
    for i,image in enumerate(os.listdir('dataset/'+writer)):
        os.rename('dataset/'+writer+'/'+image,'dataset/'+writer+'/'+str(i+1)+'.png')
        
        
writers= os.listdir('dataset')
writersWith2=[]
writersWithMoreThan2=[]
for writer in writers:
    if len(os.listdir('dataset/'+writer)) >2:
        writersWithMoreThan2.append(writer)
    else:
        writersWith2.append(writer)
for i in range(601):
    rand1=np.random.randint(0,len(writersWith2))
    rand2=rand1
    while rand2 == rand1:
        rand2=np.random.randint(0,len(writersWith2))
    rand3=np.random.randint(0,len(writersWithMoreThan2))
    
    name1=np.random.randint(1, 4)
    name2=name1
    while name2==name1:
        name2=np.random.randint(1, 4)
    name3=name1
    while name3==name1 or name3==name2:
        name3=np.random.randint(1, 4)
    os.mkdir('new data/'+str(i+1).zfill(2))
    copytree('dataset/'+writersWith2[rand1], 'new data/'+str(i).zfill(2)+'/'+writersWith2[rand1])
    os.rename('new data/'+str(i).zfill(2)+'/'+writersWith2[rand1],'new data/'+str(i).zfill(2)+'/'+str(name1))
    copytree('dataset/'+writersWith2[rand2], 'new data/'+str(i).zfill(2)+'/'+writersWith2[rand2])
    os.rename('new data/'+str(i).zfill(2)+'/'+writersWith2[rand2],'new data/'+str(i).zfill(2)+'/'+str(name2))
    copytree('dataset/'+writersWithMoreThan2[rand3], 'new data/'+str(i).zfill(2)+'/'+writersWithMoreThan2[rand3])
    os.rename('new data/'+str(i).zfill(2)+'/'+writersWithMoreThan2[rand3],'new data/'+str(i).zfill(2)+'/'+str(name3))
    
    

data=os.listdir('new data')
data=sorted(data)
trueTestLabels=[]
for folder in data:
    for subfolder in os.listdir('new data/'+folder):
        if len(os.listdir('new data/'+folder+'/'+subfolder)) >=3:
            length=len(os.listdir('new data/'+folder+'/'+subfolder))+1
            move('new data/'+folder+'/'+subfolder+'/'+'3.png','new data/'+folder+'/'+'test.png')
            print(subfolder)
            trueTestLabels.append(subfolder)
            for i in range(4,length):
                os.remove('new data/'+folder+'/'+subfolder+'/'+str(i)+'.png')
print(trueTestLabels)
