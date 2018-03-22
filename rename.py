import os

path = './'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        newnamelist = file.split('.')
        print newnamelist[0]
        print newnamelist[1]
        if newnamelist[1].find('py') == -1:
         	newname = newnamelist[0] + '.jpg'
         	os.rename(os.path.join(path,file),os.path.join(path,newname))
